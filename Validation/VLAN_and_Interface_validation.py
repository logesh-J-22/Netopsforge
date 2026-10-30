from pathlib import Path
from temp_file import All_devices_VLAN_details, All_devices_Interface_Summary, All_device_trunking_Interfaces
from validator import INVENTORY_VLAN,INVENTORY_VLAN_AND_INTERFACE
from pprint import pprint
from orchestrator import load_yaml
from dataclasses import dataclass,field
from enum import Enum
from collections import Counter

VLAN_YAML_Contents=load_yaml(INVENTORY_VLAN)
VLAN_INTERFACE_YAML_Contents=load_yaml(INVENTORY_VLAN_AND_INTERFACE)


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
    for device in VLAN_YAML_Contents["VLANS"]:
        device_Inventory=VLAN_YAML_Contents["VLANS"][device]
        IDs= [items["id"] for items in device_Inventory]
        duplicate_removed_IDs=list(set(IDs))
        if len(IDs) != len(duplicate_removed_IDs):
            Repeating_VLAN_IDS= {num: count for num, count in Counter(IDs).items() if count>1}
            for VLAN_ID, count in Repeating_VLAN_IDS.items():
                VLAN_NAME=[items["name"] for items in device_Inventory if items["id"]==VLAN_ID]
                VLAN_details=" | ".join(f"VLAN {VLAN_ID} -> {name}" for name in VLAN_NAME)
                Report.add(ValidationIssue(
                    severity=Severity.ERROR,
                    message=f"Duplicate VLAN ID {VLAN_ID} found in device {device}",
                    device=device,
                    resource="VLAN",
                    expected="Unique VLAN ID",
                    actual=f"Duplicate VLAN ID: {VLAN_details} "
                ))
def duplicate_VLAN_NAME_check(VLAN_YAML_Contents,Report) -> ValidationReport:
    for device in VLAN_YAML_Contents["VLANS"]:
            device_Inventory=VLAN_YAML_Contents["VLANS"][device]
            Names= [items["name"].lower() for items in device_Inventory]
            duplicate_removed_Names=list(set(Names))
            if len(Names) != len(duplicate_removed_Names):
                Repeating_VLAN_NAMES= {num: count for num, count in Counter(Names).items() if count>1}
                for VLAN_NAME, count in Repeating_VLAN_NAMES.items():
                    VLAN_ID=[items["id"] for items in device_Inventory if items["name"].lower()==VLAN_NAME]
                    VLAN_details=" | ".join(f"VLAN {id} -> {VLAN_NAME}" for id in VLAN_ID)
                    Report.add(ValidationIssue(
                        severity=Severity.ERROR,
                        message=f"Duplicate VLAN Name found in device {device} with name -> {VLAN_NAME}",
                        device=device,
                        resource="VLAN",
                        expected="Unique VLAN Names",
                        actual=f"Duplicate VLAN Name: {VLAN_details} "
                    ))

    
def Access_and_allowed_vlan_exisitence_check(VLAN_YAML_Contents,VLAN_INTERFACE_YAML_Contents,All_devices_VLAN_details,Report):
        for device in VLAN_YAML_Contents["VLANS"]:
            access_vlan_list=[]
            allowed_vlan_list=[]
            device_vlan=[]
            device_Inventory=VLAN_YAML_Contents["VLANS"][device]
            device_VLAN_Inventory_list=[item['id'] for item in device_Inventory]
            for device_vlan_details in All_devices_VLAN_details:
                if device in device_vlan_details:
                    device_vlan=[int(vlan) for vlan in device_vlan_details[device].keys()]
            for device_name,device_interface_details in VLAN_INTERFACE_YAML_Contents["interfaces"].items():
                if device == device_name:
                    for item in device_interface_details:
                        if 'access_vlan' in item:
                            access_vlan_list.append(item["access_vlan"])
                        else:
                            allowed_vlan_list.append(item["allowed_vlans"])
            Normalized_allowed_vlan_list=[item for sublist in allowed_vlan_list for item in sublist]
            Duplicate_removed_Normalized_allowed_vlan_list=list(set(Normalized_allowed_vlan_list))
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




def VLAN_creation_check(VLAN_YAML_Contents, All_devices_VLAN_details, Report) -> ValidationReport:
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

        # Identify duplicate names and duplicate IDs within this device's inventory
        names_list = [
            item["name"].strip().lower()
            for item in device_Inventory
            if isinstance(item, dict) and item.get("name")
        ]
        duplicate_names = {name for name, count in Counter(names_list).items() if count > 1}

        ids_list = [
            item["id"]
            for item in device_Inventory
            if isinstance(item, dict) and item.get("id") is not None
        ]
        duplicate_ids = {vid for vid, count in Counter(ids_list).items() if count > 1}

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

            clean_name = vlan_name.strip().lower() if vlan_name else ""

            # Check 1: If the VLAN name is duplicated on this device, it is already flagged as an ERROR
            if clean_name and clean_name in duplicate_names:
                continue

            # Check 2: If the VLAN ID is duplicated on this device, it is already flagged as an ERROR
            if vlan_id in duplicate_ids:
                continue

            # Check 3: Check if Report already has an ERROR or CONFLICT logged for this VLAN on this device
            has_blocking_error = any(
                issue.device == device
                and issue.severity in {Severity.ERROR, Severity.CONFLICT}
                and (
                    f"vlan {vlan_id}" in (issue.message + " " + (issue.actual or "")).lower()
                    or f"vlan id {vlan_id}" in (issue.message + " " + (issue.actual or "")).lower()
                    or (clean_name and (
                        f"name -> {clean_name}" in (issue.message + " " + (issue.actual or "")).lower()
                        or f"'{clean_name}'" in (issue.message + " " + (issue.actual or "")).lower()
                        or f"-> {clean_name}" in (issue.message + " " + (issue.actual or "")).lower()
                    ))
                )
                for issue in Report.issues
            )
            if has_blocking_error:
                continue

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


def VLAN_exist_check(VLAN_YAML_Contents, All_devices_VLAN_details, Report, report_name_mismatch: bool = False) -> ValidationReport:
    for device in VLAN_YAML_Contents.get("VLANS", {}):
        device_Inventory = VLAN_YAML_Contents["VLANS"][device]
        device_vlan_map = {}

        if isinstance(All_devices_VLAN_details, dict):
            if device in All_devices_VLAN_details:
                for vlan, details in All_devices_VLAN_details[device].items():
                    if str(vlan).isdigit():
                        vlan_name = next(iter(details.keys())) if isinstance(details, dict) else str(details)
                        device_vlan_map[int(vlan)] = vlan_name
        elif isinstance(All_devices_VLAN_details, list):
            for device_vlan_details in All_devices_VLAN_details:
                if device in device_vlan_details:
                    for vlan, details in device_vlan_details[device].items():
                        if str(vlan).isdigit():
                            vlan_name = next(iter(details.keys())) if isinstance(details, dict) else str(details)
                            device_vlan_map[int(vlan)] = vlan_name
        seen_vlans = set()
        for item in device_Inventory:
            if isinstance(item, dict):
                vlan_id = item.get("id")
                inv_vlan_name = item.get("name")
            else:
                vlan_id = int(item)
                inv_vlan_name = None

            if vlan_id is None or vlan_id in seen_vlans:
                continue
            seen_vlans.add(vlan_id)

            if vlan_id in device_vlan_map:
                dev_vlan_name = device_vlan_map[vlan_id]
                name_matches = False
                if inv_vlan_name and dev_vlan_name:
                    name_matches = (inv_vlan_name.strip().lower() == dev_vlan_name.strip().lower())
                elif not inv_vlan_name and not dev_vlan_name:
                    name_matches = True

                if name_matches:
                    name_str = f" ({inv_vlan_name})" if inv_vlan_name else ""
                    Report.add(ValidationIssue(
                        severity=Severity.OK,
                        message=f"VLAN {vlan_id}{name_str} is already present on device {device} and name matches. No need to create.",
                        device=device,
                        resource="VLAN",
                        expected=f"VLAN {vlan_id}{name_str} exists on device {device}",
                        actual=f"VLAN {vlan_id}{name_str} is present on device {device}"
                    ))
                elif report_name_mismatch:
                    Report.add(ValidationIssue(
                        severity=Severity.CHANGE,
                        message=f"VLAN {vlan_id} exists on device {device} but name differs (Inventory: '{inv_vlan_name}', Device: '{dev_vlan_name}')",
                        device=device,
                        resource="VLAN",
                        expected=f"VLAN {vlan_id} with name '{inv_vlan_name}'",
                        actual=f"VLAN {vlan_id} exists with name '{dev_vlan_name}' on device {device}"
                    ))

    return Report


def VLAN_name_conflict_check(VLAN_YAML_Contents, All_devices_VLAN_details, Report) -> ValidationReport:
    for device in VLAN_YAML_Contents.get("VLANS", {}):
        device_Inventory = VLAN_YAML_Contents["VLANS"][device]
        device_vlan_map = {}

        if isinstance(All_devices_VLAN_details, dict):
            if device in All_devices_VLAN_details:
                for vlan, details in All_devices_VLAN_details[device].items():
                    if str(vlan).isdigit():
                        vlan_name = next(iter(details.keys())) if isinstance(details, dict) else str(details)
                        device_vlan_map[int(vlan)] = vlan_name
        elif isinstance(All_devices_VLAN_details, list):
            for device_vlan_details in All_devices_VLAN_details:
                if device in device_vlan_details:
                    for vlan, details in device_vlan_details[device].items():
                        if str(vlan).isdigit():
                            vlan_name = next(iter(details.keys())) if isinstance(details, dict) else str(details)
                            device_vlan_map[int(vlan)] = vlan_name

        device_name_to_vlans = {}
        for dev_vlan_id, dev_vlan_name in device_vlan_map.items():
            if dev_vlan_name:
                device_name_to_vlans.setdefault(dev_vlan_name.strip().lower(), []).append(dev_vlan_id)

        seen_vlans = set()
        for item in device_Inventory:
            if isinstance(item, dict):
                vlan_id = item.get("id")
                inv_vlan_name = item.get("name")
            else:
                vlan_id = int(item)
                inv_vlan_name = None

            if vlan_id is None or not inv_vlan_name or vlan_id in seen_vlans:
                continue
            seen_vlans.add(vlan_id)

            clean_name = inv_vlan_name.strip().lower()
            if clean_name in device_name_to_vlans:
                conflicting_ids = [dev_id for dev_id in device_name_to_vlans[clean_name] if dev_id != vlan_id]
                if conflicting_ids:
                    conflicting_str = ", ".join(f"VLAN {dev_id}" for dev_id in conflicting_ids)
                    Report.add(ValidationIssue(
                        severity=Severity.CONFLICT,
                        message=f"VLAN name '{inv_vlan_name}' for VLAN {vlan_id} already exists under {conflicting_str} on device {device}",
                        device=device,
                        resource="VLAN",
                        expected=f"VLAN name '{inv_vlan_name}' not in use by another VLAN on device {device}",
                        actual=f"VLAN name '{inv_vlan_name}' is already used by {conflicting_str} on device {device}"
                    ))

    return Report


def normalize_name(name: str) -> str:
    """Normalize Cisco interface names (e.g. GigabitEthernet1/0/1 -> gi1/0/1)."""
    s = str(name).strip().lower()
    prefixes = [
        ("gigabitethernet", "gi"),
        ("tengigabitethernet", "te"),
        ("fastethernet", "fa"),
        ("ethernet", "et"),
        ("port-channel", "po"),
    ]
    for full, short in prefixes:
        if s.startswith(full):
            return short + s[len(full):]
    return s


def parse_vlan_range(vlan_input) -> set[int]:
    """
    Parses Cisco VLAN string representations, ranges, or lists into a set of integers.
    Examples:
        '20' -> {20}
        '20-25' -> {20, 21, 22, 23, 24, 25}
        '20,23,30' -> {20, 23, 30}
        '1-3,5' -> {1, 2, 3, 5}
        'none' -> set()
        [10, 20] -> {10, 20}
    """
    if not vlan_input:
        return set()
    if isinstance(vlan_input, (list, set, tuple)):
        result = set()
        for item in vlan_input:
            result.update(parse_vlan_range(item))
        return result
    s = str(vlan_input).strip()
    if not s or s.lower() in ("none", "null"):
        return set()
    if s.lower() == "all":
        return set(range(1, 4095))
    vlans = set()
    for part in s.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            bounds = part.split("-")
            if len(bounds) == 2 and bounds[0].strip().isdigit() and bounds[1].strip().isdigit():
                start, end = int(bounds[0].strip()), int(bounds[1].strip())
                vlans.update(range(start, end + 1))
        elif part.isdigit():
            vlans.add(int(part))
    return vlans


def format_vlan_list(vlans) -> str:
    """Formats a collection of VLAN IDs into a concise Cisco range string (e.g. '10-12,20')."""
    if not vlans:
        return ""
    sorted_vlans = sorted(set(vlans))
    ranges = []
    start = sorted_vlans[0]
    end = start
    for v in sorted_vlans[1:]:
        if v == end + 1:
            end = v
        else:
            ranges.append(f"{start}-{end}" if start != end else f"{start}")
            start = end = v
    ranges.append(f"{start}-{end}" if start != end else f"{start}")
    return ",".join(ranges)


def interface_has_errors(report: ValidationReport, device: str, interface_name: str) -> bool:
    """Check if there are any Severity.ERROR issues for this interface on this device."""
    norm = normalize_name(interface_name)
    for issue in report.issues:
        if issue.severity == Severity.ERROR and issue.device == device:
            text = f"{issue.message} {issue.actual or ''} {issue.resource or ''}"
            if interface_name.lower() in text.lower():
                return True
            for w in text.split():
                cleaned = w.strip("(),:;'\"").lower()
                if normalize_name(cleaned) == norm:
                    return True
    return False


def Trunk_interface_check(
    VLAN_INTERFACE_YAML_Contents,
    arg2,
    arg3=None,
    arg4=None,
    arg5=None,
    report_ok: bool = False
) -> ValidationReport:
    """
    Validate trunk interfaces against current device state and generate configuration commands.

    Here's the thought process behind this trunk validation:
    1. First, we check if there are any blocking ERRORs already recorded for this interface in the Report.
       For instance, if the interface doesn't physically exist on the switch hardware or has an invalid
       native VLAN, we skip generating trunk changes — because pushing trunk commands to a non-existent
       or broken port will only cause deployment failures.
    2. Once we know the interface is in good standing:
       - We consult `All_device_trunking_Interfaces` to see if the port is already actively trunking.
       - If it's already trunking: we check which VLANs are currently allowed (e.g. '20-30') and compute
         the exact missing delta. If VLANs need to be added, we generate `switchport trunk allowed vlan add <vlans>`
         so we don't accidentally overwrite or drop existing allowed VLANs.
       - We also verify whether the native VLAN matches the expected inventory setting (updating it with
         `switchport trunk native vlan <native_vlan>` if needed).
       - If the port is not yet trunking: we generate the full setup commands (`switchport mode trunk`,
         `switchport trunk allowed vlan <vlans>`, and native VLAN) to safely convert it.
    3. Each planned change is recorded as a CHANGE issue, complete with human-readable VLAN details (ID and name)
       and the exact list of Cisco CLI commands ready for execution.
    """
    # Flexibility: resolve arguments based on what was passed
    if arg3 is None and arg4 is None:
        Report = arg2
        All_devices_Interface_Summary_data = globals().get("All_devices_Interface_Summary", [])
        All_device_trunking_Interfaces_data = globals().get("All_device_trunking_Interfaces", [])
        All_devices_VLAN_details_data = globals().get("All_devices_VLAN_details", [])
        VLAN_YAML_Contents_data = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)
    elif arg4 is None:
        if hasattr(arg3, "add") and hasattr(arg3, "issues"):
            All_devices_Interface_Summary_data = arg2
            Report = arg3
            All_device_trunking_Interfaces_data = globals().get("All_device_trunking_Interfaces", [])
            All_devices_VLAN_details_data = globals().get("All_devices_VLAN_details", [])
            VLAN_YAML_Contents_data = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)
        else:
            All_devices_Interface_Summary_data = arg2
            All_device_trunking_Interfaces_data = arg3
            Report = ValidationReport()
            All_devices_VLAN_details_data = globals().get("All_devices_VLAN_details", [])
            VLAN_YAML_Contents_data = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)
    elif arg5 is None:
        if hasattr(arg4, "add") and hasattr(arg4, "issues"):
            All_devices_Interface_Summary_data = arg2
            All_device_trunking_Interfaces_data = arg3
            Report = arg4
            All_devices_VLAN_details_data = globals().get("All_devices_VLAN_details", [])
            VLAN_YAML_Contents_data = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)
        else:
            All_devices_Interface_Summary_data = arg2
            All_device_trunking_Interfaces_data = arg3
            All_devices_VLAN_details_data = arg4
            Report = ValidationReport()
            VLAN_YAML_Contents_data = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)
    else:
        All_devices_Interface_Summary_data = arg2
        All_device_trunking_Interfaces_data = arg3
        All_devices_VLAN_details_data = arg4
        Report = arg5
        VLAN_YAML_Contents_data = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)

    if isinstance(VLAN_INTERFACE_YAML_Contents, (str, Path)):
        VLAN_INTERFACE_YAML_Contents = load_yaml(VLAN_INTERFACE_YAML_Contents)
    if isinstance(VLAN_YAML_Contents_data, (str, Path)):
        VLAN_YAML_Contents_data = load_yaml(VLAN_YAML_Contents_data)

    for device, device_interfaces_details in VLAN_INTERFACE_YAML_Contents.get("interfaces", {}).items():
        # Step 1: Collect device interface list to verify hardware presence
        device_interfaces = []
        if isinstance(All_devices_Interface_Summary_data, dict):
            if device in All_devices_Interface_Summary_data:
                device_interfaces = All_devices_Interface_Summary_data[device]
        elif isinstance(All_devices_Interface_Summary_data, list):
            for dev_summary in All_devices_Interface_Summary_data:
                if device in dev_summary:
                    device_interfaces = dev_summary[device]
                    break
        device_interfaces_normalized = {normalize_name(i) for i in device_interfaces}

        # Step 2: Build VLAN ID -> VLAN Name lookup
        vlan_name_lookup = {}
        dev_vlan_info = {}
        if isinstance(All_devices_VLAN_details_data, dict):
            if device in All_devices_VLAN_details_data:
                dev_vlan_info = All_devices_VLAN_details_data[device]
        elif isinstance(All_devices_VLAN_details_data, list):
            for dev_dict in All_devices_VLAN_details_data:
                if device in dev_dict:
                    dev_vlan_info = dev_dict[device]
                    break

        for vlan_str, vlan_data in dev_vlan_info.items():
            if str(vlan_str).isdigit():
                vlan_id = int(vlan_str)
                if isinstance(vlan_data, dict):
                    for vname in vlan_data.keys():
                        vlan_name_lookup[vlan_id] = vname

        # Supplement VLAN names with inventory YAML (for VLANs yet to be created on switch)
        if VLAN_YAML_Contents_data and "VLANS" in VLAN_YAML_Contents_data:
            for inv_vlan in VLAN_YAML_Contents_data["VLANS"].get(device, []):
                if isinstance(inv_vlan, dict):
                    vid = inv_vlan.get("id")
                    vname = inv_vlan.get("name")
                    if vid is not None and vname:
                        vlan_name_lookup[int(vid)] = vname

        # Step 3: Extract active trunk details for this device from All_device_trunking_Interfaces
        device_trunks = {}
        raw_trunk_obj = None
        if isinstance(All_device_trunking_Interfaces_data, dict):
            raw_trunk_obj = All_device_trunking_Interfaces_data.get(device)
        elif isinstance(All_device_trunking_Interfaces_data, list):
            for dev_entry in All_device_trunking_Interfaces_data:
                if isinstance(dev_entry, dict) and device in dev_entry:
                    raw_trunk_obj = dev_entry[device]
                    break

        if isinstance(raw_trunk_obj, dict):
            ifaces = raw_trunk_obj.get("interface", {})
            if isinstance(ifaces, dict):
                for if_name, if_info in ifaces.items():
                    if isinstance(if_info, dict):
                        device_trunks[normalize_name(if_name)] = if_info

        # Step 4: Validate each trunk interface in inventory
        seen_interfaces = set()
        for item in device_interfaces_details:
            if not isinstance(item, dict):
                continue
            raw_name = item.get("name")
            mode = item.get("mode")
            allowed_vlans_raw = item.get("allowed_vlans")
            native_vlan = item.get("native_vlan")

            if not raw_name or (mode != "trunk" and not allowed_vlans_raw):
                continue

            names = [n.strip() for n in str(raw_name).split(",") if n.strip()]
            for interface_name in names:
                if interface_name in seen_interfaces:
                    continue
                seen_interfaces.add(interface_name)

                norm_name = normalize_name(interface_name)

                # Check A: Does this interface exist on the switch hardware?
                if norm_name not in device_interfaces_normalized:
                    # Interface missing error: ensure it's logged in Report if not already recorded
                    if not interface_has_errors(Report, device, interface_name):
                        Report.add(ValidationIssue(
                            severity=Severity.ERROR,
                            message=f"Interface {interface_name} doesn't exist in the device {device}",
                            device=device,
                            resource="Interface",
                            expected=f"Interface {interface_name} exists on device {device}",
                            actual=f"Interface {interface_name} doesn't exist in the device {device}"
                        ))
                    continue

                # Check B: Are there ANY errors regarding this specific interface in the Report?
                if interface_has_errors(Report, device, interface_name):
                    # Skip trunk change because of blocking errors on this port
                    continue

                # Parse expected allowed VLANs
                expected_vlans = parse_vlan_range(allowed_vlans_raw)
                expected_native = int(native_vlan) if native_vlan is not None else None

                # Check C: Check device trunking status
                trunk_info = device_trunks.get(norm_name)
                is_currently_trunking = trunk_info is not None and trunk_info.get("status") == "trunking"

                if is_currently_trunking:
                    current_allowed_str = trunk_info.get("vlans_allowed_on_trunk", "")
                    current_allowed_vlans = parse_vlan_range(current_allowed_str)
                    current_native_vlan = int(trunk_info.get("native_vlan", 1))

                    missing_vlans = sorted(expected_vlans - current_allowed_vlans)

                    # Build human-readable VLAN summary (ID and Name)
                    vlan_details_list = []
                    for vid in missing_vlans:
                        vname = vlan_name_lookup.get(vid)
                        vname_str = f" ({vname})" if vname else ""
                        vlan_details_list.append(f"VLAN {vid}{vname_str}")
                    vlans_display = ", ".join(vlan_details_list)

                    if missing_vlans:
                        Report.add(ValidationIssue(
                            severity=Severity.CHANGE,
                            message=f"VLANs {vlans_display} will be added in the trunk interface {interface_name} on device {device}",
                            device=device,
                            resource="Trunk Interface",
                            expected=f"Trunk interface {interface_name} allowing VLANs {format_vlan_list(expected_vlans)}",
                            actual=f"Trunk interface {interface_name} currently allows VLANs {format_vlan_list(current_allowed_vlans)}; missing: {vlans_display}"
                        ))
                    elif expected_native is not None and expected_native != current_native_vlan:
                        Report.add(ValidationIssue(
                            severity=Severity.CHANGE,
                            message=f"Native VLAN {expected_native} will be configured on trunk interface {interface_name} on device {device}",
                            device=device,
                            resource="Trunk Native VLAN",
                            expected=f"Native VLAN {expected_native}",
                            actual=f"Native VLAN is currently {current_native_vlan}"
                        ))
                    elif report_ok:
                        Report.add(ValidationIssue(
                            severity=Severity.OK,
                            message=f"Trunk interface {interface_name} is already properly configured on device {device}",
                            device=device,
                            resource="Trunk Interface",
                            expected=f"Trunk interface {interface_name} allowing VLANs {format_vlan_list(expected_vlans)}",
                            actual=f"Trunk interface {interface_name} already allows VLANs {format_vlan_list(current_allowed_vlans)}"
                        ))
                else:
                    # Interface exists on device, but is not currently operating as a trunk
                    vlan_details_list = []
                    for vid in sorted(expected_vlans):
                        vname = vlan_name_lookup.get(vid)
                        vname_str = f" ({vname})" if vname else ""
                        vlan_details_list.append(f"VLAN {vid}{vname_str}")
                    vlans_display = ", ".join(vlan_details_list)

                    Report.add(ValidationIssue(
                        severity=Severity.CHANGE,
                        message=f"VLANs {vlans_display} will be added in the trunk interface {interface_name} on device {device}",
                        device=device,
                        resource="Trunk Interface",
                        expected=f"Trunk interface {interface_name} allowing {vlans_display}",
                        actual=f"Interface {interface_name} is not currently operating as a trunk; will be converted to trunk with VLANs {vlans_display}"
                    ))

    return Report


def Interface_existence_check(
    VLAN_INTERFACE_YAML_Contents,
    All_devices_Interface_Summary,
    arg3,
    arg4=None,
    arg5=None,
    arg6=None,
    report_ok: bool = False
) -> ValidationReport:
    """
    Check interface existence, access VLAN assignments, and trunk configurations on the device.

    Here's the thought process behind this validation:
    1. First, we check if the interface from the inventory actually exists on the device hardware.
       If it's missing, we immediately log an ERROR because you can't push configs to an interface
       that isn't physically or logically there.
    2. For access interfaces:
       - If it's already sitting on a different VLAN, we raise a WARNING to give the team
         a heads-up that this interface is currently part of another VLAN and will be moved.
         We also include the CLI command to reassign the VLAN.
       - If it's unassigned (not in any VLAN yet), we log a CHANGE since it's ready to be
         provisioned into its target access VLAN, along with the full access port commands.
    3. For trunk interfaces:
       - We first make sure there are no existing blocking ERRORS on this interface (like an invalid
         native VLAN, or the interface not existing).
       - If everything looks clean and error-free, we inspect `All_device_trunking_Interfaces` to determine
         which VLANs need to be added, and record a CHANGE noting the VLAN IDs and names, along with the
         exact Cisco CLI commands to apply.
    """
    # Flexibility: support calling with 3, 4, 5, or 6 arguments seamlessly
    if arg4 is None and arg5 is None and arg6 is None:
        Report = arg3
        All_device_trunking_Interfaces_data = globals().get("All_device_trunking_Interfaces", [])
        All_devices_VLAN_details_data = globals().get("All_devices_VLAN_details", [])
        VLAN_YAML_Contents_data = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)
    elif arg5 is None and arg6 is None:
        if hasattr(arg3, "add") and hasattr(arg3, "issues"):
            Report = arg3
            All_devices_VLAN_details_data = arg4
            All_device_trunking_Interfaces_data = globals().get("All_device_trunking_Interfaces", [])
            VLAN_YAML_Contents_data = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)
        else:
            All_devices_VLAN_details_data = arg3
            Report = arg4
            All_device_trunking_Interfaces_data = globals().get("All_device_trunking_Interfaces", [])
            VLAN_YAML_Contents_data = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)
    elif arg6 is None:
        if hasattr(arg4, "add") and hasattr(arg4, "issues"):
            All_device_trunking_Interfaces_data = arg3
            Report = arg4
            All_devices_VLAN_details_data = arg5 if arg5 is not None else globals().get("All_devices_VLAN_details", [])
            VLAN_YAML_Contents_data = globals().get("VLAN_YAML_Contents") or load_yaml(INVENTORY_VLAN)
        else:
            All_devices_VLAN_details_data = arg3
            VLAN_YAML_Contents_data = arg4
            Report = arg5
            All_device_trunking_Interfaces_data = globals().get("All_device_trunking_Interfaces", [])
    else:
        All_device_trunking_Interfaces_data = arg3
        All_devices_VLAN_details_data = arg4
        VLAN_YAML_Contents_data = arg5
        Report = arg6

    if isinstance(VLAN_INTERFACE_YAML_Contents, (str, Path)):
        VLAN_INTERFACE_YAML_Contents = load_yaml(VLAN_INTERFACE_YAML_Contents)
    if isinstance(VLAN_YAML_Contents_data, (str, Path)):
        VLAN_YAML_Contents_data = load_yaml(VLAN_YAML_Contents_data)

    for device, device_interfaces_details in VLAN_INTERFACE_YAML_Contents.get("interfaces", {}).items():
        # Step 1: Collect all interface names present on this device
        device_interfaces = []
        if isinstance(All_devices_Interface_Summary, dict):
            if device in All_devices_Interface_Summary:
                device_interfaces = All_devices_Interface_Summary[device]
        elif isinstance(All_devices_Interface_Summary, list):
            for dev_summary in All_devices_Interface_Summary:
                if device in dev_summary:
                    device_interfaces = dev_summary[device]
                    break

        device_interfaces_normalized = {normalize_name(i) for i in device_interfaces}

        # Step 2: Build lookup tables for interface VLANs and VLAN names on this device
        device_interface_vlan_map = {}
        vlan_name_lookup = {}
        dev_vlan_info = {}
        if isinstance(All_devices_VLAN_details_data, dict):
            if device in All_devices_VLAN_details_data:
                dev_vlan_info = All_devices_VLAN_details_data[device]
        elif isinstance(All_devices_VLAN_details_data, list):
            for dev_dict in All_devices_VLAN_details_data:
                if device in dev_dict:
                    dev_vlan_info = dev_dict[device]
                    break

        for vlan_str, vlan_data in dev_vlan_info.items():
            if str(vlan_str).isdigit():
                vlan_id = int(vlan_str)
                if isinstance(vlan_data, dict):
                    for vlan_name, ifaces in vlan_data.items():
                        vlan_name_lookup[vlan_id] = vlan_name
                        if isinstance(ifaces, list):
                            for iface in ifaces:
                                device_interface_vlan_map[normalize_name(iface)] = vlan_id

        # Supplement VLAN names with inventory YAML (in case VLAN isn't on the box yet)
        if VLAN_YAML_Contents_data and "VLANS" in VLAN_YAML_Contents_data:
            for inv_vlan in VLAN_YAML_Contents_data["VLANS"].get(device, []):
                if isinstance(inv_vlan, dict):
                    vid = inv_vlan.get("id")
                    vname = inv_vlan.get("name")
                    if vid is not None and vname:
                        vlan_name_lookup[int(vid)] = vname

        seen_interfaces = set()
        for interface in device_interfaces_details:
            if isinstance(interface, dict):
                raw_name = interface.get("name")
                expected_access_vlan = interface.get("access_vlan")
                mode = interface.get("mode")
                allowed_vlans = interface.get("allowed_vlans")
            else:
                raw_name = str(interface)
                expected_access_vlan = None
                mode = None
                allowed_vlans = None

            if not raw_name:
                continue

            # Handle possible comma-separated lists of interface names
            names = [n.strip() for n in str(raw_name).split(",") if n.strip()]
            for interface_name in names:
                if interface_name in seen_interfaces:
                    continue
                seen_interfaces.add(interface_name)

                norm_name = normalize_name(interface_name)

                # Check 1: Does the interface exist on the device hardware at all?
                if norm_name not in device_interfaces_normalized:
                    Report.add(ValidationIssue(
                        severity=Severity.ERROR,
                        message=f"Interface {interface_name} doesn't exist in the device {device}",
                        device=device,
                        resource="Interface",
                        expected=f"Interface {interface_name} exists on device {device}",
                        actual=f"Interface {interface_name} doesn't exist in the device {device}"
                    ))
                    continue

                # Check 2: For access interfaces, verify their access VLAN status
                if expected_access_vlan is not None:
                    current_vlan = device_interface_vlan_map.get(norm_name)

                    if current_vlan is None:
                        # Case: Interface is present on the device, but not assigned to any VLAN yet
                        Report.add(ValidationIssue(
                            severity=Severity.CHANGE,
                            message=f"Interface {interface_name} is not part of any VLAN on device {device}. The interface will be added in VLAN {expected_access_vlan}",
                            device=device,
                            resource="Interface VLAN",
                            expected=f"Interface {interface_name} in VLAN {expected_access_vlan}",
                            actual=f"Interface {interface_name} is not part of any VLAN"
                        ))
                    elif current_vlan != expected_access_vlan:
                        # Case: Interface is currently assigned to a different VLAN on the device
                        Report.add(ValidationIssue(
                            severity=Severity.WARNING,
                            message=f"Interface {interface_name} is part of a different VLAN (VLAN {current_vlan}) rather than access VLAN {expected_access_vlan} on device {device}",
                            device=device,
                            resource="Interface VLAN",
                            expected=f"Interface {interface_name} in access VLAN {expected_access_vlan}",
                            actual=f"Interface {interface_name} is in VLAN {current_vlan}"
                        ))
                    elif report_ok:
                        # Case: Interface already matches the expected access VLAN
                        Report.add(ValidationIssue(
                            severity=Severity.OK,
                            message=f"Interface {interface_name} is already in access VLAN {expected_access_vlan} on device {device}",
                            device=device,
                            resource="Interface VLAN",
                            expected=f"Interface {interface_name} in access VLAN {expected_access_vlan}",
                            actual=f"Interface {interface_name} is in access VLAN {expected_access_vlan}"
                        ))

    # Step 3: Run Trunk interface validation with All_device_trunking_Interfaces and generate commands
    Trunk_interface_check(
        VLAN_INTERFACE_YAML_Contents=VLAN_INTERFACE_YAML_Contents,
        arg2=All_devices_Interface_Summary,
        arg3=All_device_trunking_Interfaces_data,
        arg4=Report,
        report_ok=report_ok
    )

    return Report


def main():
    Report = ValidationReport()
    Interface_existence_check(VLAN_INTERFACE_YAML_Contents, All_devices_Interface_Summary, Report)
    pprint(Report)

if __name__ == "__main__":
    main()

    