#!/usr/bin/env python3
"""
Orchestrator - Network Pre-Flight Validation Engine & Automated Deployment
Coordinates YAML parsing, Pydantic schema validation, network state checks,
report generation, and Ansible playbook deployment.
"""
from pathlib import Path
import sys
import argparse
import subprocess
import yaml

# Ensure local imports and virtualenv packages work
sys.path.insert(0, str(Path(__file__).resolve().parent))
for sp in (Path(__file__).resolve().parent.parent / ".venv/lib").glob("python*/site-packages"):
    if sp.exists() and str(sp) not in sys.path:
        sys.path.insert(0, str(sp))


def load_yaml(path: Path | str) -> dict:
    """Load and parse a YAML file."""
    with open(path, "r") as f:
        return yaml.safe_load(f)


from models import Vlan_interface_structure, Vlan_structure
from pydantic import ValidationError

from validator import (
    INVENTORY_VLAN as DEFAULT_VLAN_FILE,
    INVENTORY_VLAN_AND_INTERFACE as DEFAULT_IFACE_FILE,
    INVENTORY_VALIDATOR as INVENTORY_FILE,
    PLAYBOOK_FILE,
)

from VLAN_and_Interface_validation import (
    ValidationReport,
    ValidationIssue,
    Severity,
    duplicate_VLAN_ID_check,
    duplicate_VLAN_NAME_check,
    Access_and_allowed_vlan_exisitence_check,
    Native_VLAN_check,
    VLAN_creation_check,
    VLAN_exist_check,
    VLAN_name_conflict_check,
    Interface_existence_check,
)
from device_state_parser import (
    All_devices_VLAN_details,
    All_devices_Interface_Summary,
    All_device_trunking_Interfaces,
)


def validate_yaml_schema(vlans_yaml: dict, interface_yaml: dict, report: ValidationReport) -> ValidationReport:
    """
    Stage 1 Validation:
    Validate YAML schema, datatypes, and reserved VLANs using Pydantic models.
    Any datatype mismatch or range error is added to Report as Severity.ERROR.
    """
    # 1. Validate VLAN definitions (VLANs.yaml)
    for device, vlan_list in vlans_yaml.get("VLANS", {}).items():
        if not isinstance(vlan_list, list):
            continue
        for each_vlan in vlan_list:
            if not isinstance(each_vlan, dict):
                continue
            try:
                Vlan_structure(**each_vlan)
            except ValidationError as e:
                for err in e.errors():
                    field_name = err["loc"][0] if err["loc"] else "VLAN"
                    clean_msg = err["msg"].replace("Value error, ", "")
                    report.add(ValidationIssue(
                        severity=Severity.ERROR,
                        message=f"{clean_msg} (field '{field_name}')",
                        device=device,
                        resource="VLAN Schema",
                        expected="Valid VLAN ID (1-4094, non-reserved) and name",
                        actual=f"Invalid value: {err.get('input')}"
                    ))

    # 2. Validate Interface definitions (VLAN_interfaces.yaml)
    for device, iface_list in interface_yaml.get("interfaces", {}).items():
        if not isinstance(iface_list, list):
            continue
        for each_interface in iface_list:
            if not isinstance(each_interface, dict):
                continue
            try:
                Vlan_interface_structure(**each_interface)
            except ValidationError as e:
                for err in e.errors():
                    field_name = err["loc"][0] if err["loc"] else "Interface"
                    clean_msg = err["msg"].replace("Value error, ", "")
                    iface_name = each_interface.get("name", "Unknown")
                    report.add(ValidationIssue(
                        severity=Severity.ERROR,
                        message=f"{clean_msg} on interface {iface_name}",
                        device=device,
                        resource="Interface Schema",
                        expected="Valid interface configuration",
                        actual=f"Invalid value: {err.get('input')}"
                    ))

    return report


def run_validation(vlan_inventory_file: Path, interface_inventory_file: Path, report_ok: bool = True) -> ValidationReport:
    """
    Full Validation Pipeline:
    - Stage 1: Pydantic Schema, Datatypes & Reserved VLAN Validation
    - Stage 2: Network State & Business Logic Validation
    """
    vlan_yaml = load_yaml(vlan_inventory_file)
    interface_yaml = load_yaml(interface_inventory_file)

    report = ValidationReport()

    # Stage 1: Schema & Types
    validate_yaml_schema(vlan_yaml, interface_yaml, report)

    # Stage 2: Network State & Business Logic
    duplicate_VLAN_ID_check(vlan_yaml, report)
    duplicate_VLAN_NAME_check(vlan_yaml, report)
    VLAN_name_conflict_check(vlan_yaml, All_devices_VLAN_details, report)
    VLAN_creation_check(vlan_yaml, All_devices_VLAN_details, report)
    VLAN_exist_check(vlan_yaml, All_devices_VLAN_details, report)
    Native_VLAN_check(interface_yaml, report)
    Access_and_allowed_vlan_exisitence_check(vlan_yaml, interface_yaml, All_devices_VLAN_details, report)
    Interface_existence_check(
        interface_yaml,
        All_devices_Interface_Summary,
        report,
        report_ok=report_ok,
    )
    return report


def display_results(title: str, report: ValidationReport):
    """Format and display validation report in console."""
    print("=" * 80)
    print(f" {title.upper()} ")
    print("=" * 80)

    severity_counts = {}
    for issue in report.issues:
        sev = issue.severity.value
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    print(f"Summary of Severities: {severity_counts}")
    print(f"Has Blocking Issues (ERROR / CONFLICT): {report.has_blocking_issues}")
    print("-" * 80)

    # Group issues by severity order
    order = [Severity.ERROR, Severity.CONFLICT, Severity.WARNING, Severity.CHANGE, Severity.OK]
    for sev in order:
        matching = [i for i in report.issues if i.severity == sev]
        if not matching:
            continue
        print(f"\n>>> [{sev.value}] Count: {len(matching)}")
        for idx, item in enumerate(matching, 1):
            print(f"  {idx}. [{item.device}] {item.resource}: {item.message}")


def run_playbook(vlan_dir: Path | None = None) -> int:
    """Execute the Ansible playbook Ansible/Playbook/VLAN.yaml."""
    cmd = [
        "ansible-playbook",
        "-i", str(INVENTORY_FILE),
        str(PLAYBOOK_FILE),
    ]
    if vlan_dir:
        cmd.extend(["-e", f"vlan_dir={vlan_dir}"])

    print("\n" + "=" * 80)
    print(" EXECUTING ANSIBLE PLAYBOOK: VLAN.yaml ")
    print("=" * 80)
    print(f"Command: {' '.join(cmd)}\n")

    result = subprocess.run(cmd, cwd=str(PLAYBOOK_FILE.parent.parent))
    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Network Orchestrator - Pre-flight validation & automated deployment"
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Simulate validation and display report without applying changes",
    )
    parser.add_argument(
        "--vlan-dir",
        type=Path,
        default=None,
        help="Path to directory containing VLANs.yaml and VLAN_interfaces.yaml",
    )
    parser.add_argument(
        "-v",
        "--vlan-file",
        type=Path,
        default=DEFAULT_VLAN_FILE,
        help=f"Path to VLANs inventory YAML file (default: {DEFAULT_VLAN_FILE})",
    )
    parser.add_argument(
        "-i",
        "--interface-file",
        type=Path,
        default=DEFAULT_IFACE_FILE,
        help=f"Path to VLAN interfaces inventory YAML file (default: {DEFAULT_IFACE_FILE})",
    )
    
    args = parser.parse_args()

    if args.vlan_dir:
        vlan_file = args.vlan_dir / "VLANs.yaml"
        iface_file = args.vlan_dir / "VLAN_interfaces.yaml"
        target_dir = args.vlan_dir
    else:
        vlan_file = args.vlan_file
        iface_file = args.interface_file
        target_dir = vlan_file.parent

    # Run validation pipeline
    title = f"Validation Report ({vlan_file.name}, {iface_file.name})"
    report = run_validation(vlan_file, iface_file, report_ok=True)
    display_results(title, report)

    # Dry-run mode: report simulation status and exit without running playbook
    if args.dry_run:
        print("\n" + "=" * 80)
        status = "PASSED (NO BLOCKING ISSUES)" if not report.has_blocking_issues else "BLOCKING ISSUES FOUND"
        print(f" [DRY-RUN MODE] Pre-flight simulation completed: {status}")
        print(" [DRY-RUN MODE] Skipping playbook execution as requested.")
        print("=" * 80)
        sys.exit(0 if not report.has_blocking_issues else 1)

    # Live execution mode: check for blocking issues
    if report.has_blocking_issues:
        print("\n" + "=" * 80)
        print(" [BLOCKED] PLAYBOOK EXECUTION ABORTED DUE TO BLOCKING ISSUES")
        print("=" * 80)
        print("Blocking issues (ERROR / CONFLICT) were detected in the inventory.")
        print("The Ansible playbook 'VLAN.yaml' was NOT executed.")
        print("Please resolve the blocking issues listed above before deploying.\n")
        sys.exit(1)

    # Validation passed: proceed with Ansible playbook
    print("\n" + "=" * 80)
    print(" [PASSED] NO BLOCKING ISSUES DETECTED - PROCEEDING WITH PLAYBOOK")
    print("=" * 80)
    print("Applying VLAN and Interface configurations via Ansible playbook: VLAN.yaml...\n")
    exit_code = run_playbook(vlan_dir=target_dir)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
