from pathlib import Path
from temp_file import All_devices_VLAN_details,All_devices_Interface_Summary,All_devices_Interface_Details
from validator import INVENTORY_VLAN,INVENTORY_VLAN_AND_INTERFACE
from pprint import pprint
from orchestrator import load_yaml
from dataclasses import dataclass,field
from enum import Enum
from collections import Counter

VLAN_YAML_Contents=load_yaml(INVENTORY_VLAN)
VLAN_INTERFACE_YAML_Contents=load_yaml(INVENTORY_VLAN_AND_INTERFACE)
# pprint(VLAN_YAML_Contents)
# pprint(VLAN_INTERFACE_YAML_Contents)

# class Errors:
#     def duplicate_vlan_id(self):
#         pass
#     def duplucate_vlan_name(self):
#         pass
#     def Interface_vlan_exist_check(self):
#         pass

class Severity(Enum):
    ERROR = "Error"
    CONFLICT = "CONFLICT"
    WARNING = "WARNING"
    CHANGE = "CHANGE"
    OK = "OK"

@dataclass
class ValidationIssue:
    severity: Severity
    message: str
    device: str | None = None
    resource: str | None = None
    expected: str | None = None
    actual: str | None = None

@dataclass
class ValidationReport:
    issues: list[ValidationIssue] = field(
        default_factory=list
    )

    def add(self, issue: ValidationIssue):
        self.issues.append(issue)

    @property
    def has_blocking_issues(self) -> bool:
        return any(
            issue.severity in {
                Severity.ERROR,
                Severity.CONFLICT,
            }
            for issue in self.issues
        )
def duplicate_VLAN_ID_check(VLAN_YAML_Contents,Report) -> ValidationReport:
    
    # devices=list(VLAN_YAML_Contents["VLANS"].keys())
    for device in VLAN_YAML_Contents["VLANS"]:
        device_Inventory=VLAN_YAML_Contents["VLANS"][device]
        # pprint(device_Inventory)
        IDs= [items["id"] for items in device_Inventory]
        # print(IDs)
        duplicate_removed_IDs=list(set(IDs))
        if len(IDs) != len(duplicate_removed_IDs):
            Repeating_VLAN_IDS= {num: count for num, count in Counter(IDs).items() if count>1}
            # print(Repeating_VLAN_IDS.items())
            for VLAN_ID, count in Repeating_VLAN_IDS.items():
                VLAN_NAME=[items["name"] for items in device_Inventory if items["id"]==VLAN_ID]
                VLAN_details=" | ".join(f"VLAN {VLAN_ID} -> {name}" for name in VLAN_NAME)
                # print(VLAN_details)
                Report.add(ValidationIssue(
                    severity=Severity.ERROR,
                    message=f"Duplicate VLAN ID found in device {device}",
                    device=device,
                    resource="VLAN",
                    expected="Unique VLAN ID",
                    actual=f"Duplicate VLAN ID: {VLAN_details} "
                ))
def duplicate_VLAN_NAME_check(VLAN_YAML_Contents,Report) -> ValidationReport:
    for device in VLAN_YAML_Contents["VLANS"]:
            device_Inventory=VLAN_YAML_Contents["VLANS"][device]
            # pprint(device_Inventory)
            Names= [items["name"].lower() for items in device_Inventory]
            # print(Names)
            duplicate_removed_Names=list(set(Names))
            if len(Names) != len(duplicate_removed_Names):
                Repeating_VLAN_NAMES= {num: count for num, count in Counter(Names).items() if count>1}
                # print(Repeating_VLAN_NAMES.items())
                for VLAN_NAME, count in Repeating_VLAN_NAMES.items():
                    VLAN_ID=[items["id"] for items in device_Inventory if items["name"].lower()==VLAN_NAME]
                    # print(VLAN_ID)
                    VLAN_details=" | ".join(f"VLAN {id} -> {VLAN_NAME}" for id in VLAN_ID)
                    # print(VLAN_details)
                    Report.add(ValidationIssue(
                        severity=Severity.ERROR,
                        message=f"Duplicate VLAN Name found in device {device}",
                        device=device,
                        resource="VLAN",
                        expected="Unique VLAN Names",
                        actual=f"Duplicate VLAN Name: {VLAN_details} "
                    ))

    
def Access_and_allowed_vlan_exisitence_check(VLAN_YAML_Contents,VLAN_INTERFACE_YAML_Contents,All_devices_VLAN_details,Report):
        # pprint(VLAN_YAML_Contents)
                # Need to get the VLAN detaills in hte device in the precheck, so the  variable will be made 
        
        for device in VLAN_YAML_Contents["VLANS"]:
            access_vlan_list=[]
            allowed_vlan_list=[]
            device_vlan=[]
            device_Inventory=VLAN_YAML_Contents["VLANS"][device]
            device_VLAN_Inventory_list=[item['id'] for item in device_Inventory]
            # print(device_VLAN_Inventory_list)
            for device_vlan_details in All_devices_VLAN_details:
                if device in device_vlan_details:
                    device_vlan=[int(vlan) for vlan in device_vlan_details[device].keys()]
                    # print(device_vlan)
            for device_name,device_interface_details in VLAN_INTERFACE_YAML_Contents["interfaces"].items():
                if device == device_name:
                    for item in device_interface_details:
                        if 'access_vlan' in item:
                            access_vlan_list.append(item["access_vlan"])
                        else:
                            allowed_vlan_list.append(item["allowed_vlans"])
            Normalized_allowed_vlan_list=[item for sublist in allowed_vlan_list for item in sublist]
            Duplicate_removed_Normalized_allowed_vlan_list=list(set(Normalized_allowed_vlan_list))
            # print(Duplicate_removed_Normalized_allowed_vlan_list)
            for vlan in Duplicate_removed_Normalized_allowed_vlan_list:
                if (vlan not in device_VLAN_Inventory_list) and (vlan not in device_vlan):
                    Report.add(ValidationIssue(
                                            severity=Severity.ERROR,
                                            message=f"Interface VLAN must exist in the VLAN inventory/device",
                                            device=device,
                                            resource="Interface VLAN",
                                            expected=f"allowed VLAN {vlan} exist in the device or its present in the inventory ",
                                            actual=f"allowed VLAN {vlan} neither exist in the device nor added in the inventory to create it"
                                        ))
            for vlan in access_vlan_list:
                if (vlan not in device_VLAN_Inventory_list) and (vlan not in device_vlan):
                    Report.add(ValidationIssue(
                                                severity=Severity.ERROR,
                                                message=f"Interface VLAN must exist in the VLAN inventory/device",
                                                device=device,
                                                resource="Interface VLAN",
                                                expected=f"access VLAN {vlan} exist in the device or its present in the inventory ",
                                                actual=f"access VLAN {vlan} neither exist in the device nor added in the inventory to create it"
                                            ))

                    

            # print(f"{device}",access_vlan_list)
            # print(f"{device}",allowed_vlan_list)
            


            # All_devices_Interface_Details


def Native_VLAN_check(VLAN_INTERFACE_YAML_Contents,Report):
    print("Native VLAN check")
    for device_name,device_interface_details in VLAN_INTERFACE_YAML_Contents["interfaces"].items():
        for interface in device_interface_details:
            if 'native_vlan' in interface:
                if interface["native_vlan"] != 999:
                    Report.add(ValidationIssue(
                        severity=Severity.ERROR,
                        message=f"Native VLAN must be 999 for the Trunk allowed VLAN {interface.get('allowed_vlans')}",
                        device=device_name,
                        resource="Native VLAN",
                        expected="Native VLAN 999",
                        actual=f"Native VLAN {interface['native_vlan']} on interface {interface.get('name')} is not 999"
                    ))




def VLAN_creation_check(VLAN_YAML_Contents=None, All_devices_VLAN_details=None, Report=None) -> ValidationReport:
    print("VLAN creation check")
    if Report is None:
        if All_devices_VLAN_details is not None:
            arg1, arg2 = VLAN_YAML_Contents, All_devices_VLAN_details
            Report = arg2
            if isinstance(arg1, (str, Path)) or (isinstance(arg1, dict) and "VLANS" in arg1):
                VLAN_YAML_Contents = arg1
                All_devices_VLAN_details = globals().get("All_devices_VLAN_details", [])
            else:
                All_devices_VLAN_details = arg1
                VLAN_YAML_Contents = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)
        else:
            Report = VLAN_YAML_Contents
            VLAN_YAML_Contents = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)
            All_devices_VLAN_details = globals().get("All_devices_VLAN_details", [])

    if isinstance(VLAN_YAML_Contents, (str, Path)):
        VLAN_YAML_Contents = load_yaml(VLAN_YAML_Contents)
    elif VLAN_YAML_Contents is None:
        VLAN_YAML_Contents = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)

    if All_devices_VLAN_details is None:
        All_devices_VLAN_details = globals().get("All_devices_VLAN_details", [])

    for device in VLAN_YAML_Contents.get("VLANS", {}):
        device_Inventory = VLAN_YAML_Contents["VLANS"][device]
        device_vlan = []

        if isinstance(All_devices_VLAN_details, dict):
            if device in All_devices_VLAN_details:
                device_vlan = [int(vlan) for vlan in All_devices_VLAN_details[device].keys() if str(vlan).isdigit()]
        elif isinstance(All_devices_VLAN_details, list):
            for device_vlan_details in All_devices_VLAN_details:
                if device in device_vlan_details:
                    device_vlan = [int(vlan) for vlan in device_vlan_details[device].keys() if str(vlan).isdigit()]

        seen_vlans = set()
        for item in device_Inventory:
            if isinstance(item, dict):
                vlan_id = item.get("id")
                vlan_name = item.get("name")
            else:
                vlan_id = int(item)
                vlan_name = None

            if vlan_id is None or vlan_id in seen_vlans:
                continue
            seen_vlans.add(vlan_id)

            if vlan_id not in device_vlan:
                name_str = f" ({vlan_name})" if vlan_name else ""
                Report.add(ValidationIssue(
                    severity=Severity.CHANGE,
                    message=f"VLAN {vlan_id}{name_str} needs to be created on device {device}",
                    device=device,
                    resource="VLAN Creation",
                    expected=f"VLAN {vlan_id}{name_str} exists on device {device}",
                    actual=f"VLAN {vlan_id}{name_str} is not present on device {device} and will be created"
                ))

    return Report


vlan_creation_check = VLAN_creation_check


def main():
    Report=ValidationReport()
    # duplicate_VLAN_ID_check(VLAN_YAML_Contents,Report)
    # duplicate_VLAN_NAME_check(VLAN_YAML_Contents,Report)
    # pprint(All_devices_VLAN_details)
    # pprint(VLAN_INTERFACE_YAML_Contents)
    # Access_and_allowed_vlan_exisitence_check(VLAN_YAML_Contents,VLAN_INTERFACE_YAML_Contents,All_devices_VLAN_details,Report)
    # Native_VLAN_check(VLAN_INTERFACE_YAML_Contents,Report)
    VLAN_creation_check(VLAN_YAML_Contents, All_devices_VLAN_details, Report)
    pprint(Report)
    # pprint(VLAN_INTERFACE_YAML_Contents)

if __name__ == "__main__":
    main()
    