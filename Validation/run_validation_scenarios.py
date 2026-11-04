#!/usr/bin/env python3
"""
Validation Scenarios Runner
Tests both the 'with_issues' and 'resolved' inventories against the validation engine.
"""
from pathlib import Path
import sys
import argparse
import subprocess

# Ensure local imports and virtualenv packages work
sys.path.insert(0, str(Path(__file__).resolve().parent))
for sp in (Path(__file__).resolve().parent.parent / ".venv/lib").glob("python*/site-packages"):
    if sp.exists() and str(sp) not in sys.path:
        sys.path.insert(0, str(sp))

from orchestrator import load_yaml, validate_yaml_schema
from VLAN_and_Interface_validation import (
    ValidationReport,
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

from validator import (
    INVENTORY_VLAN as DEFAULT_VLAN_FILE,
    INVENTORY_VLAN_AND_INTERFACE as DEFAULT_IFACE_FILE,
    INVENTORY_VALIDATOR as INVENTORY_FILE,
    PLAYBOOK_FILE,
)


def run_validation(vlan_inventory_file: Path, interface_inventory_file: Path, report_ok: bool = True) -> ValidationReport:
    """Run the complete suite of validations against the given YAML inventory files."""
    vlan_yaml = load_yaml(vlan_inventory_file)
    interface_yaml = load_yaml(interface_inventory_file)

    report = ValidationReport()

    # Stage 1: Pydantic Schema, Datatypes & Reserved VLAN Validation
    validate_yaml_schema(vlan_yaml, interface_yaml, report)

    # Stage 2: Network State & Logic Validation
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

    # Group issues by severity
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
        description="Validation Runner - Pre-flight network validation & automated deployment"
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Simulate validation and display report without applying changes",
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

    vlan_file = args.vlan_file
    iface_file = args.interface_file
    target_dir = vlan_file.parent

    # Run validation on the YAML files
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
