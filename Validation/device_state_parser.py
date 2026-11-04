"""
Device State Parser
Normalizes raw device state (from mock files or live Netmiko collectors)
into standardized dictionaries keyed by device name: {'R1': ..., 'R2': ...}.
"""
from typing import Any
import sys
from pathlib import Path

# Ensure local imports work
sys.path.insert(0, str(Path(__file__).resolve().parent))

from temp_file import (
    All_devices_VLAN_details as _raw_vlan_details,
    All_devices_Interface_Summary as _raw_iface_summary,
    All_device_trunking_Interfaces as _raw_trunk_interfaces,
)


def to_device_map(data: list[dict[str, Any]] | dict[str, Any] | None) -> dict[str, Any]:
    """
    Normalize a list of single-device dicts [{'R1': ...}, {'R2': ...}]
    or an already consolidated dict {'R1': ..., 'R2': ...}
    into a guaranteed dictionary keyed by device name: {'R1': ..., 'R2': ...}.
    """
    if not data:
        return {}
    if isinstance(data, dict):
        return dict(data)
    if isinstance(data, list):
        merged: dict[str, Any] = {}
        for entry in data:
            if isinstance(entry, dict):
                merged.update(entry)
        return merged
    return {}


# Normalized, clean dictionaries ready for direct O(1) device lookups:
# All_devices_VLAN_details: {'R1': {'1': {'default': [...]}, ...}, 'R2': {...}}
All_devices_VLAN_details: dict[str, dict] = to_device_map(_raw_vlan_details)

# All_devices_Interface_Summary: {'R1': ['Vlan1', 'GigabitEthernet1/0/1', ...], 'R2': [...]}
All_devices_Interface_Summary: dict[str, list[str]] = to_device_map(_raw_iface_summary)

# All_device_trunking_Interfaces: {'R1': {'interface': {...}}, 'R2': {'interface': {...}}}
All_device_trunking_Interfaces: dict[str, dict] = to_device_map(_raw_trunk_interfaces)

