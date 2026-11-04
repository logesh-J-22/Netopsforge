import yaml
from pathlib import Path
from models import Vlan_interface_structure, Vlan_structure
from pydantic import ValidationError


def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def validate_yaml_schema(vlans_yaml: dict, interface_yaml: dict, report) -> None:
    """
    Validate YAML schema, datatypes, and reserved VLANs using Pydantic.
    Any datatype mismatch or range error is added to Report as Severity.ERROR.
    """
    from VLAN_and_Interface_validation import ValidationIssue, Severity
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


def main():
    from VLAN_and_Interface_validation import ValidationReport
    from validator import INVENTORY_VLAN, INVENTORY_VLAN_AND_INTERFACE

    vlans = load_yaml(INVENTORY_VLAN)
    Vlans_interface = load_yaml(INVENTORY_VLAN_AND_INTERFACE)

    report = ValidationReport()
    validate_yaml_schema(vlans, Vlans_interface, report)

    number_of_error = 1
    for issue in report.issues:
        print(f"###########################  Error No.{number_of_error} in {issue.device} ({issue.resource})   ###########################")
        print("Error Severity:", issue.severity.value)
        print("Error Message:", issue.message)
        print("Error Expected:", issue.expected)
        print("Error Actual:", issue.actual)
        print("###############################################################")
        number_of_error += 1


if __name__ == "__main__":
    main()
