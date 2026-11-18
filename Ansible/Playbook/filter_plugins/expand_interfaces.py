import re

INTERFACE_PREFIX_MAP = {
    "et": "Ethernet",
    "ethernet": "Ethernet",
    "fa": "FastEthernet",
    "fastethernet": "FastEthernet",
    "gi": "GigabitEthernet",
    "gigabitethernet": "GigabitEthernet",
    "te": "TenGigabitEthernet",
    "tengigabitethernet": "TenGigabitEthernet",
    "fo": "FortyGigabitEthernet",
    "fortygigabitethernet": "FortyGigabitEthernet",
    "hu": "HundredGigE",
    "hundredgige": "HundredGigE",
    "tw": "TwoGigabitEthernet",
    "twogigabitethernet": "TwoGigabitEthernet",
    "fi": "FiveGigabitEthernet",
    "fivegigabitethernet": "FiveGigabitEthernet",
    "twentyfivegige": "TwentyFiveGigE",
    "twe": "TwentyFiveGigE",
    "lo": "Loopback",
    "loopback": "Loopback",
    "po": "Port-channel",
    "port-channel": "Port-channel",
    "vl": "Vlan",
    "vlan": "Vlan",
}


def canonical_interface_name(name: str) -> str:
    """Normalize abbreviated interface names (e.g. 'Et0/0') to canonical Cisco names ('Ethernet0/0')."""
    if not name or not isinstance(name, str):
        return name
    m = re.match(r"^([a-zA-Z\-]+)\s*([\d\/\.]+)$", name.strip())
    if not m:
        return name.strip()
    prefix, num = m.groups()
    canonical_prefix = INTERFACE_PREFIX_MAP.get(prefix.lower(), prefix)
    return f"{canonical_prefix}{num}"


def expand_interfaces(interface_list):
    """
    Expands comma-separated interface names in a list of interface dictionaries
    into individual interface entries with canonical Cisco IOS interface names
    for true resource idempotency.

    Example:
      Input:  [{'name': 'Et0/1, Et0/2', 'mode': 'access', 'access_vlan': 10}]
      Output: [{'name': 'Ethernet0/1', 'mode': 'access', 'access_vlan': 10},
               {'name': 'Ethernet0/2', 'mode': 'access', 'access_vlan': 10}]
    """
    if not interface_list or not isinstance(interface_list, list):
        return []

    result = []
    for item in interface_list:
        if not isinstance(item, dict):
            result.append(item)
            continue

        raw_name = item.get("name")
        if not raw_name:
            result.append(item)
            continue

        # Split comma-separated interface names
        names = [n.strip() for n in str(raw_name).split(",") if n.strip()]
        if not names:
            result.append(item)
            continue

        for name in names:
            new_item = dict(item)
            new_item["name"] = canonical_interface_name(name)
            result.append(new_item)

    return result


class FilterModule(object):
    def filters(self):
        return {
            "expand_interfaces": expand_interfaces
        }
