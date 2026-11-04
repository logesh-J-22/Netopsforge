from pathlib import Path
from device_state_parser import (
    to_device_map,
    All_devices_VLAN_details,
    All_devices_Interface_Summary,
    All_device_trunking_Interfaces,
)
from validator import INVENTORY_VLAN, INVENTORY_VLAN_AND_INTERFACE
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


def find_duplicates(items: list) -> dict:
    """Return a dictionary of {item: count} for items appearing more than once."""
    return {item: count for item, count in Counter(items).items() if count > 1}


def duplicate_VLAN_ID_check(VLAN_YAML_Contents, Report) -> ValidationReport:
    """
    Check for duplicate VLAN IDs declared under the same device in the inventory YAML.

    Here's the thought process behind this validation:
    1. Every VLAN configured on a switch must have a unique numeric ID (1-4094).
       If an inventory file defines the same VLAN ID multiple times under the same device
       (for example, VLAN 10 assigned to 'HR' and also VLAN 10 assigned to 'Marketing'),
       this represents a syntax conflict and logical error.
    2. We collect all VLAN IDs defined for each device and check whether their count matches
       the number of unique IDs.
    3. If any duplicate IDs exist, we identify how many times they appear and record a
       Severity.ERROR showing which conflicting names were assigned to that same ID.
    """
    for device in VLAN_YAML_Contents["VLANS"]:
        device_Inventory = VLAN_YAML_Contents["VLANS"][device]

        # Step 1: Collect all VLAN IDs declared for this device and identify repeating IDs
        IDs = [items["id"] for items in device_Inventory if isinstance(items, dict) and "id" in items]
        Repeating_VLAN_IDS = find_duplicates(IDs)

        # Step 2: For each duplicate ID, gather the conflicting names and record an ERROR
        for VLAN_ID in Repeating_VLAN_IDS:
            VLAN_NAME = [items["name"] for items in device_Inventory if items.get("id") == VLAN_ID]
            VLAN_details = " | ".join(f"VLAN {VLAN_ID} -> {name}" for name in VLAN_NAME)
            Report.add(ValidationIssue(
                severity=Severity.ERROR,
                message=f"Duplicate VLAN ID {VLAN_ID} found in device {device}",
                device=device,
                resource="VLAN",
                expected="Unique VLAN ID",
                actual=f"Duplicate VLAN ID: {VLAN_details} "
            ))
def duplicate_VLAN_NAME_check(VLAN_YAML_Contents, Report) -> ValidationReport:
    """
    Check for duplicate VLAN names assigned to different VLAN IDs on the same device.

    Here's the thought process behind this validation:
    1. On Cisco IOS switches, VLAN names should be unique per switch to avoid operational
       confusion, automation ambiguity, and configuration overwrite issues.
    2. Defining two different VLAN IDs with the exact same name (e.g. VLAN 10 = 'Engineering'
       and VLAN 20 = 'Engineering') in the device's inventory indicates a naming collision
       or accidental copy-paste error.
    3. We normalize all VLAN names to lowercase and compare total names against unique names.
    4. If any duplicate names exist, we log a Severity.ERROR listing all the VLAN IDs that are
       competing for the same name.
    """
    for device in VLAN_YAML_Contents["VLANS"]:
        device_Inventory = VLAN_YAML_Contents["VLANS"][device]

        # Step 1: Collect normalized (lowercase) names for all VLANs and identify repeating names
        Names = [items["name"].lower() for items in device_Inventory if isinstance(items, dict) and items.get("name")]
        Repeating_VLAN_NAMES = find_duplicates(Names)

        # Step 2: For each duplicate name, find all associated VLAN IDs and record an ERROR
        for VLAN_NAME in Repeating_VLAN_NAMES:
            VLAN_ID = [items["id"] for items in device_Inventory if items.get("name", "").lower() == VLAN_NAME]
            VLAN_details = " | ".join(f"VLAN {id} -> {VLAN_NAME}" for id in VLAN_ID)
            Report.add(ValidationIssue(
                severity=Severity.ERROR,
                message=f"Duplicate VLAN Name found in device {device} with name -> {VLAN_NAME}",
                device=device,
                resource="VLAN",
                expected="Unique VLAN Names",
                actual=f"Duplicate VLAN Name: {VLAN_details} "
            ))

    
def Access_and_allowed_vlan_exisitence_check(VLAN_YAML_Contents, VLAN_INTERFACE_YAML_Contents, All_devices_VLAN_details, Report):
    """
    Ensure every access VLAN and trunk allowed VLAN assigned to an interface exists on the switch or in inventory.

    Here's the thought process behind this validation:
    1. When an interface is configured as an access port (`switchport access vlan X`) or trunk port
       (`switchport trunk allowed vlan ...`), the specified VLANs must actually exist.
    2. If an engineer binds an interface to a VLAN that does not exist on the switch and is not
       scheduled to be created in `VLANs.yaml`, packets for that VLAN cannot be forwarded and traffic
       will be blackholed.
    3. We collect all access VLANs and trunk allowed VLANs assigned across all interfaces on each device.
    4. For every referenced VLAN, we verify it is either already active on the device hardware or
       present in the VLAN inventory for creation.
    5. If a VLAN is neither on the switch nor in the inventory, we raise a blocking Severity.ERROR.
    """
    vlan_details_map = to_device_map(All_devices_VLAN_details)

    for device in VLAN_YAML_Contents["VLANS"]:
        # Step 1: Collect existing device VLANs and planned inventory VLANs
        device_Inventory = VLAN_YAML_Contents["VLANS"][device]
        device_VLAN_Inventory_list = [item['id'] for item in device_Inventory]
        dev_vlan_info = vlan_details_map.get(device, {})
        device_vlan = [int(vlan) for vlan in dev_vlan_info.keys() if str(vlan).isdigit()]

        # Step 2: Extract access VLANs and trunk allowed VLANs configured on this device's interfaces
        access_vlan_list = []
        allowed_vlan_list = []
        device_interface_details = VLAN_INTERFACE_YAML_Contents.get("interfaces", {}).get(device, [])
        for item in device_interface_details:
            if 'access_vlan' in item:
                access_vlan_list.append(item["access_vlan"])
            elif 'allowed_vlans' in item:
                allowed_vlan_list.append(item["allowed_vlans"])

        Normalized_allowed_vlan_list = [item for sublist in allowed_vlan_list for item in sublist]
        Duplicate_removed_Normalized_allowed_vlan_list = list(set(Normalized_allowed_vlan_list))

        # Step 3: Validate that all trunk allowed VLANs exist on switch or in inventory
        for vlan in Duplicate_removed_Normalized_allowed_vlan_list:
            if (vlan not in device_VLAN_Inventory_list) and (vlan not in device_vlan):
                Report.add(ValidationIssue(
                    severity=Severity.ERROR,
                    message="Interface VLAN must exist in the VLAN inventory/device",
                    device=device,
                    resource="Interface VLAN",
                    expected=f"allowed VLAN {vlan} exist in the device or its present in the inventory ",
                    actual=f"allowed VLAN {vlan} neither exist in the device nor added in the inventory to create it"
                ))

        # Step 4: Validate that all access VLANs exist on switch or in inventory
        for vlan in access_vlan_list:
            if (vlan not in device_VLAN_Inventory_list) and (vlan not in device_vlan):
                Report.add(ValidationIssue(
                    severity=Severity.ERROR,
                    message="Interface VLAN must exist in the VLAN inventory/device",
                    device=device,
                    resource="Interface VLAN",
                    expected=f"access VLAN {vlan} exist in the device or its present in the inventory ",
                    actual=f"access VLAN {vlan} neither exist in the device nor added in the inventory to create it"
                ))


def Native_VLAN_check(VLAN_INTERFACE_YAML_Contents, Report) -> ValidationReport:
    """
    Validate that trunk interfaces use the enterprise standard native VLAN 999.

    Here's the thought process behind this validation:
    1. By default, Cisco 802.1Q trunks use VLAN 1 as the native (untagged) VLAN.
       Leaving the native VLAN as 1 is a known security vulnerability (enabling VLAN hopping
       attacks and mixing untagged control traffic with user data).
    2. Enterprise security standards mandate that all trunk ports explicitly configure
       an isolated, non-default native VLAN (VLAN 999).
    3. We scan every interface in `VLAN_interfaces.yaml` that defines a `native_vlan`.
    4. If the configured `native_vlan` is anything other than 999, we record a blocking
       Severity.ERROR indicating the violation and the offending interface.
    """
    for device_name, device_interface_details in VLAN_INTERFACE_YAML_Contents["interfaces"].items():
        # Step 1: Iterate over each interface defined for the device
        for interface in device_interface_details:
            # Step 2: Check if this interface specifies a native VLAN
            if 'native_vlan' in interface:
                # Step 3: Enforce security standard that native VLAN must be 999
                if interface["native_vlan"] != 999:
                    Report.add(ValidationIssue(
                        severity=Severity.ERROR,
                        message=f"Native VLAN must be 999 for the Trunk allowed VLAN {interface.get('allowed_vlans')}",
                        device=device_name,
                        resource="Native VLAN",
                        expected="Native VLAN 999",
                        actual=f"Native VLAN {interface['native_vlan']} on interface {interface.get('name')} is not 999"
                    ))
    return Report




def VLAN_creation_check(VLAN_YAML_Contents, All_devices_VLAN_details, Report) -> ValidationReport:
    """
    Identify which VLANs from the inventory need to be newly provisioned on each device.

    Here's the thought process behind this validation:
    1. We want to determine which VLANs in `VLANs.yaml` do not currently exist on the physical switch
       hardware and therefore need to be created (`vlan <id>`, `name <name>`).
    2. However, we must NOT schedule creation for invalid or conflicting VLANs:
       - If a VLAN has duplicate IDs or duplicate names within the inventory itself, it has already
         been flagged as a blocking ERROR; attempting to create it would fail or overwrite configs.
       - If a VLAN name conflicts with a different VLAN ID already on the switch (Severity.CONFLICT),
         or has any other blocking error logged in Report, we safely suppress the creation CHANGE.
    3. For all valid, error-free VLANs that are missing from the switch (`vlan_id not in device_vlan`),
       we record a Severity.CHANGE to schedule their provisioning.
    """
    vlan_details_map = to_device_map(All_devices_VLAN_details)

    for device in VLAN_YAML_Contents.get("VLANS", {}):
        # Step 1: Collect existing VLAN IDs on this device
        device_Inventory = VLAN_YAML_Contents["VLANS"][device]
        dev_vlan_info = vlan_details_map.get(device, {})
        device_vlan = [int(vlan) for vlan in dev_vlan_info.keys() if str(vlan).isdigit()]

        # Step 2: Identify local duplicate names and duplicate IDs within this device's inventory
        duplicate_names = set(find_duplicates([
            item["name"].strip().lower()
            for item in device_Inventory
            if isinstance(item, dict) and item.get("name")
        ]))
        duplicate_ids = set(find_duplicates([
            item["id"]
            for item in device_Inventory
            if isinstance(item, dict) and item.get("id") is not None
        ]))

        # Step 3: Check each inventory VLAN and filter out any with duplicate or blocking errors
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

            # Filter A: Skip if VLAN name is duplicated on this device (already flagged as ERROR)
            if clean_name and clean_name in duplicate_names:
                continue

            # Filter B: Skip if VLAN ID is duplicated on this device (already flagged as ERROR)
            if vlan_id in duplicate_ids:
                continue

            # Filter C: Skip if Report already has an ERROR or CONFLICT logged for this VLAN
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

            # Step 4: If VLAN does not exist on switch, record a CHANGE to create it
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


def get_device_vlan_map(device_vlan_details: dict) -> dict[int, str]:
    """Extract a clean dictionary of {vlan_id: vlan_name} from device VLAN state."""
    vlan_map = {}
    for vlan, details in device_vlan_details.items():
        if str(vlan).isdigit():
            name = next(iter(details.keys())) if isinstance(details, dict) else str(details)
            vlan_map[int(vlan)] = name
    return vlan_map


def VLAN_exist_check(VLAN_YAML_Contents, All_devices_VLAN_details, Report, report_name_mismatch: bool = False) -> ValidationReport:
    """
    Check if inventory VLANs already exist on the device and verify if their names match.

    Here's the thought process behind this validation:
    1. For every VLAN specified in `VLANs.yaml`, we check whether it already exists on the live switch.
    2. If the VLAN ID is already configured on the switch:
       - If both the ID and name match exactly between inventory and device, no changes are needed!
         We log a Severity.OK issue to confirm that this VLAN is in its desired state.
       - If the VLAN ID exists but has a different name on the switch (e.g. switch has 'SALES' while
         inventory specifies 'Sales_Dept'), this is an informational/name drift. When
         `report_name_mismatch` is enabled, we record a Severity.CHANGE to prompt a name update.
    3. If the VLAN ID does not exist on the switch at all, we do nothing here (that creation check
       is handled separately by `VLAN_creation_check`).
    """
    vlan_details_map = to_device_map(All_devices_VLAN_details)

    for device in VLAN_YAML_Contents.get("VLANS", {}):
        device_Inventory = VLAN_YAML_Contents["VLANS"][device]

        # Step 1: Build a map of existing VLAN IDs to names on this device
        device_vlan_map = get_device_vlan_map(vlan_details_map.get(device, {}))

        # Step 2: Check each inventory VLAN against the device's existing VLANs
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

            # Step 3: If VLAN exists on switch, compare names
            if vlan_id in device_vlan_map:
                dev_vlan_name = device_vlan_map[vlan_id]
                name_matches = False
                if inv_vlan_name and dev_vlan_name:
                    name_matches = (inv_vlan_name.strip().lower() == dev_vlan_name.strip().lower())
                elif not inv_vlan_name and not dev_vlan_name:
                    name_matches = True

                # Case A: VLAN ID and name already match; no action needed
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
                # Case B: VLAN ID exists but has a different name on switch
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
    """
    Check if a proposed VLAN name in the inventory already belongs to a different VLAN on the switch.

    Here's the thought process behind this validation:
    1. On Cisco IOS switches, assigning a name that is already used by an existing VLAN
       causes naming ambiguity, monitoring confusion, or command failures.
    2. For instance, if the switch already has VLAN 20 named 'VOICE', and the inventory proposes
       creating VLAN 30 with the name 'VOICE', this is a naming conflict between two different VLAN IDs.
    3. We invert the device's current VLAN map to build a lookup from lowercase names to their VLAN IDs.
    4. For every VLAN in `VLANs.yaml`, we check whether its desired name is already owned by any
       *different* VLAN ID on that device.
    5. If a collision is found, we log a Severity.CONFLICT alerting the engineer to rename one of the VLANs.
    """
    vlan_details_map = to_device_map(All_devices_VLAN_details)

    for device in VLAN_YAML_Contents.get("VLANS", {}):
        device_Inventory = VLAN_YAML_Contents["VLANS"][device]

        # Step 1: Collect existing VLAN ID -> Name mappings on the device
        device_vlan_map = get_device_vlan_map(vlan_details_map.get(device, {}))

        # Step 2: Build an inverted lookup: lowercase VLAN name -> list of existing VLAN IDs
        device_name_to_vlans = {}
        for dev_vlan_id, dev_vlan_name in device_vlan_map.items():
            if dev_vlan_name:
                device_name_to_vlans.setdefault(dev_vlan_name.strip().lower(), []).append(dev_vlan_id)

        # Step 3: Check each inventory VLAN to see if its name conflicts with a different VLAN ID
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
                # Step 4: If another VLAN ID already owns this name, record a CONFLICT
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


def format_vlan_names(vlans, lookup: dict[int, str]) -> str:
    """Format VLAN IDs with human-readable names: e.g. 'VLAN 10 (Devops), VLAN 20 (Security)'."""
    return ", ".join(f"VLAN {v}" + (f" ({lookup[v]})" if lookup.get(v) else "") for v in sorted(vlans))


def get_vlan_name_lookup(device: str, vlan_details_map: dict, vlan_yaml: dict | None = None) -> dict[int, str]:
    """Build a VLAN ID -> VLAN Name lookup table for a device from switch state and inventory YAML."""
    lookup = get_device_vlan_map(vlan_details_map.get(device, {}))
    if vlan_yaml and "VLANS" in vlan_yaml:
        for item in vlan_yaml["VLANS"].get(device, []):
            if isinstance(item, dict) and item.get("id") is not None and item.get("name"):
                lookup[int(item["id"])] = item["name"]
    return lookup


def _evaluate_trunk_port(
    device: str,
    interface_name: str,
    item: dict,
    trunk_info: dict | None,
    vlan_name_lookup: dict[int, str],
    Report: ValidationReport,
    report_ok: bool = False
):
    """
    Evaluate a single trunk interface against live device state and record CHANGE, ERROR, or OK issues.

    Here's the thought process behind this evaluation:
    1. If the port is already actively trunking (802.1Q mode):
       - Compare current allowed VLANs against desired allowed VLANs to compute missing VLANs.
       - If missing VLANs exist, record a Severity.CHANGE listing the VLAN IDs and human-readable names.
       - If the native VLAN differs from desired, record a Severity.CHANGE to update the native VLAN.
       - If already completely configured and in sync, record Severity.OK (when report_ok is True).
    2. If the port is not yet trunking (currently in access mode or default state):
       - Record a Severity.CHANGE noting that the interface will be converted to trunk mode and all
         desired VLANs will be added.
    """
    expected_vlans = parse_vlan_range(item.get("allowed_vlans"))
    expected_native = int(item["native_vlan"]) if item.get("native_vlan") is not None else None

    # Case 1: Interface is already operating as an 802.1Q trunk port
    if trunk_info and trunk_info.get("status") == "trunking":
        current_allowed = parse_vlan_range(trunk_info.get("vlans_allowed_on_trunk", ""))
        current_native = int(trunk_info.get("native_vlan", 1))
        missing_vlans = sorted(expected_vlans - current_allowed)
        vlans_display = format_vlan_names(missing_vlans, vlan_name_lookup)

        # Delta check: Are any expected VLANs missing from the trunk?
        if missing_vlans:
            Report.add(ValidationIssue(
                severity=Severity.CHANGE,
                device=device,
                resource="Trunk Interface",
                message=f"VLANs {vlans_display} will be added in the trunk interface {interface_name} on device {device}",
                expected=f"Trunk interface {interface_name} allowing VLANs {format_vlan_list(expected_vlans)}",
                actual=f"Trunk interface {interface_name} currently allows VLANs {format_vlan_list(current_allowed)}; missing: {vlans_display}"
            ))
        # Native VLAN check: Does native VLAN match desired standard?
        elif expected_native is not None and expected_native != current_native:
            Report.add(ValidationIssue(
                severity=Severity.CHANGE,
                device=device,
                resource="Trunk Native VLAN",
                message=f"Native VLAN {expected_native} will be configured on trunk interface {interface_name} on device {device}",
                expected=f"Native VLAN {expected_native}",
                actual=f"Native VLAN is currently {current_native}"
            ))
        # Already fully matching: Report OK if requested
        elif report_ok:
            Report.add(ValidationIssue(
                severity=Severity.OK,
                device=device,
                resource="Trunk Interface",
                message=f"Trunk interface {interface_name} is already properly configured on device {device}",
                expected=f"Trunk interface {interface_name} allowing VLANs {format_vlan_list(expected_vlans)}",
                actual=f"Trunk interface {interface_name} already allows VLANs {format_vlan_list(current_allowed)}"
            ))
    else:
        # Case 2: Interface is currently an access port; needs full trunk conversion
        vlans_display = format_vlan_names(expected_vlans, vlan_name_lookup)
        Report.add(ValidationIssue(
            severity=Severity.CHANGE,
            device=device,
            resource="Trunk Interface",
            message=f"VLANs {vlans_display} will be added in the trunk interface {interface_name} on device {device}",
            expected=f"Trunk interface {interface_name} allowing {vlans_display}",
            actual=f"Interface {interface_name} is not currently operating as a trunk; will be converted to trunk with VLANs {vlans_display}"
        ))


def Interface_existence_check(
    VLAN_INTERFACE_YAML_Contents,
    All_devices_Interface_Summary,
    Report: ValidationReport,
    All_device_trunking_Interfaces=None,
    All_devices_VLAN_details=None,
    VLAN_YAML_Contents=None,
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
       - If it's unassigned (not in any VLAN yet), we log a CHANGE since it's ready to be
         provisioned into its target access VLAN.
    3. For trunk interfaces:
       - We first make sure there are no existing blocking ERRORS on this interface (like an invalid
         native VLAN, or the interface not existing).
       - If clean, we inspect `All_device_trunking_Interfaces` to determine which VLANs need to be added,
         and record a CHANGE noting the VLAN IDs and names.
    """
    All_device_trunking_Interfaces = All_device_trunking_Interfaces or globals().get("All_device_trunking_Interfaces")
    VLAN_YAML_Contents = VLAN_YAML_Contents or globals().get("VLAN_YAML_Contents")
    All_devices_VLAN_details = All_devices_VLAN_details or globals().get("All_devices_VLAN_details")

    # Step 1: Normalize device summaries, VLAN details, and trunk state tables
    iface_summary_map = to_device_map(All_devices_Interface_Summary)
    vlan_details_map = to_device_map(All_devices_VLAN_details)
    trunk_interfaces_map = to_device_map(All_device_trunking_Interfaces)

    for device, device_interfaces_details in VLAN_INTERFACE_YAML_Contents.get("interfaces", {}).items():
        # Step 2: Build lookup tables for interface names, VLANs, and trunk states on this device
        device_interfaces_normalized = {normalize_name(i) for i in iface_summary_map.get(device, [])}
        vlan_name_lookup = get_vlan_name_lookup(device, vlan_details_map, VLAN_YAML_Contents)
        raw_trunks = trunk_interfaces_map.get(device, {}).get("interface", {})
        device_trunks = {normalize_name(k): v for k, v in raw_trunks.items() if isinstance(v, dict)}

        dev_vlan_info = vlan_details_map.get(device, {})
        device_interface_vlan_map = {
            normalize_name(iface): int(vlan_str)
            for vlan_str, vdata in dev_vlan_info.items() if str(vlan_str).isdigit() and isinstance(vdata, dict)
            for ifaces in vdata.values() if isinstance(ifaces, list)
            for iface in ifaces
        }

        # Step 3: Validate each interface in inventory
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

                # Check 3: For trunk interfaces, evaluate trunk status and missing allowed VLANs
                elif (mode == "trunk" or allowed_vlans) and not interface_has_errors(Report, device, interface_name):
                    _evaluate_trunk_port(
                        device, interface_name, interface,
                        device_trunks.get(norm_name),
                        vlan_name_lookup, Report, report_ok
                    )

    return Report


def Trunk_interface_check(
    VLAN_INTERFACE_YAML_Contents,
    All_devices_Interface_Summary,
    All_device_trunking_Interfaces,
    Report: ValidationReport,
    All_devices_VLAN_details=None,
    VLAN_YAML_Contents=None,
    report_ok: bool = False
) -> ValidationReport:
    """
    Validate trunk interfaces against current device state and determine required trunk updates.
    (Kept for backward compatibility; interface checks are unified in Interface_existence_check).
    """
    return Interface_existence_check(
        VLAN_INTERFACE_YAML_Contents=VLAN_INTERFACE_YAML_Contents,
        All_devices_Interface_Summary=All_devices_Interface_Summary,
        Report=Report,
        All_device_trunking_Interfaces=All_device_trunking_Interfaces,
        All_devices_VLAN_details=All_devices_VLAN_details,
        VLAN_YAML_Contents=VLAN_YAML_Contents,
        report_ok=report_ok,
    )


def main():
    Report = ValidationReport()
    Interface_existence_check(VLAN_INTERFACE_YAML_Contents, All_devices_Interface_Summary, Report)
    pprint(Report)

if __name__ == "__main__":
    main()

    