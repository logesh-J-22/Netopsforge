"""
Device State Parser
Normalizes raw live device state collected by Ansible (or other discovery tools)
into standardized dictionaries keyed by device name: {'SW1': ..., 'SW2': ...}.
Replaces static mock files with live device state from Ansible JSON artifacts.
"""
from typing import Any
import sys
import json
from pathlib import Path

# Ensure local imports work
sys.path.insert(0, str(Path(__file__).resolve().parent))

BASE_DIR = Path(__file__).resolve().parent
STATE_FILE = BASE_DIR / "live_device_state.json"
STATES_DIR = BASE_DIR / "device_states"


def to_device_map(data: list[dict[str, Any]] | dict[str, Any] | None) -> dict[str, Any]:
    """
    Normalize a list of single-device dicts [{'SW1': ...}, {'SW2': ...}]
    or an already consolidated dict {'SW1': ..., 'SW2': ...}
    into a guaranteed dictionary keyed by device name: {'SW1': ..., 'SW2': ...}.
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


def load_raw_device_state() -> dict[str, Any]:
    """
    Load raw device state gathered by Ansible.
    Checks:
    1. Individual device state files: Validation/device_states/<hostname>.json
    2. Aggregated file: Validation/live_device_state.json
    """
    devices_data: dict[str, Any] = {}

    # 1. Load from device_states directory if files exist
    if STATES_DIR.exists():
        for json_file in sorted(STATES_DIR.glob("*.json")):
            hostname = json_file.stem
            try:
                content = json.loads(json_file.read_text())
                devices_data[hostname] = content
            except Exception as e:
                print(f"[WARNING] Failed to parse device state from {json_file}: {e}")

    # 2. If aggregated file exists, merge or use it
    if STATE_FILE.exists():
        try:
            content = json.loads(STATE_FILE.read_text())
            if isinstance(content, dict):
                if "VLAN_details" in content:
                    return content
                for host, data in content.items():
                    if host not in devices_data:
                        devices_data[host] = data
        except Exception as e:
            print(f"[WARNING] Failed to parse {STATE_FILE}: {e}")

    return devices_data


def parse_device_states(raw_data: dict[str, Any]) -> tuple[dict[str, dict], dict[str, list[str]], dict[str, dict]]:
    """
    Parse raw Ansible switch state into normalized data structures:
    - All_devices_VLAN_details: { 'SW1': { '1': {'default': ['Et0/1']}, ... } }
    - All_devices_Interface_Summary: { 'SW1': ['Ethernet0/0', 'Ethernet0/1', ...] }
    - All_device_trunking_Interfaces: { 'SW1': { 'interface': { 'Ethernet0/2': {...} } } }
    """
    # If already pre-structured format:
    if "VLAN_details" in raw_data:
        vlan_map = to_device_map(raw_data.get("VLAN_details"))
        iface_map = to_device_map(raw_data.get("Interface_Summary"))
        trunk_map = to_device_map(raw_data.get("Trunking_Interfaces"))
        return vlan_map, iface_map, trunk_map

    vlan_map: dict[str, dict] = {}
    iface_map: dict[str, list[str]] = {}
    trunk_map: dict[str, dict] = {}

    for host, host_info in raw_data.items():
        if not isinstance(host_info, dict):
            continue

        # 1. Parse VLANs (show vlan brief)
        host_vlans = {}
        for v in host_info.get("vlans", []):
            if not isinstance(v, dict):
                continue
            vid = str(v.get("vlan_id", "")).strip()
            if not vid:
                continue
            vname = str(v.get("vlan_name", "")).strip()
            ifaces = v.get("interfaces", [])
            if isinstance(ifaces, str):
                ifaces = [i.strip() for i in ifaces.split(",") if i.strip()]
            host_vlans[vid] = {vname: ifaces}
        vlan_map[host] = host_vlans

        # 2. Parse Interfaces (show ip interface brief)
        host_ifaces = []
        for iface in host_info.get("interfaces", []):
            if isinstance(iface, dict):
                iname = iface.get("interface", "")
            else:
                iname = str(iface)
            if iname:
                host_ifaces.append(iname)
        iface_map[host] = host_ifaces

        # 3. Parse Trunk Interfaces (show interfaces switchport / show interfaces trunk)
        host_trunks = {}
        # From switchport details (ntc_templates show interfaces switchport)
        for sp in host_info.get("switchports", []):
            if not isinstance(sp, dict):
                continue
            mode = str(sp.get("mode", "")).lower()
            admin_mode = str(sp.get("admin_mode", "")).lower()
            if "trunk" in mode or "trunk" in admin_mode:
                iname = sp.get("interface", "")
                tvlans = sp.get("trunking_vlans", [])
                if isinstance(tvlans, list):
                    tvlans_str = ",".join(str(x) for x in tvlans)
                else:
                    tvlans_str = str(tvlans)
                host_trunks[iname] = {
                    "name": iname,
                    "native_vlan": str(sp.get("native_vlan", "1")),
                    "status": "trunking",
                    "vlans_allowed_on_trunk": tvlans_str,
                    "vlans_allowed_active_in_mgmt_domain": tvlans_str,
                    "vlans_in_stp_forwarding_not_pruned": tvlans_str,
                    "mode": "on",
                    "encapsulation": "802.1q",
                }

        # From raw trunk output (if present)
        for tr in host_info.get("trunks", []):
            if isinstance(tr, dict):
                iname = tr.get("port", tr.get("interface", ""))
                if iname and iname not in host_trunks:
                    host_trunks[iname] = {
                        "name": iname,
                        "native_vlan": str(tr.get("native_vlan", "1")),
                        "status": "trunking",
                        "vlans_allowed_on_trunk": str(tr.get("vlan_allowed", "")),
                        "mode": "on",
                        "encapsulation": "802.1q",
                    }

        trunk_map[host] = {"interface": host_trunks}

    return vlan_map, iface_map, trunk_map


def load_live_device_state():
    """Load and parse current live device states."""
    raw = load_raw_device_state()
    return parse_device_states(raw)


# Module-level exports initialized dynamically:
All_devices_VLAN_details, All_devices_Interface_Summary, All_device_trunking_Interfaces = load_live_device_state()


def refresh_device_state():
    """Reload live device states from disk after Ansible updates them."""
    global All_devices_VLAN_details, All_devices_Interface_Summary, All_device_trunking_Interfaces
    All_devices_VLAN_details, All_devices_Interface_Summary, All_device_trunking_Interfaces = load_live_device_state()
    return All_devices_VLAN_details, All_devices_Interface_Summary, All_device_trunking_Interfaces
