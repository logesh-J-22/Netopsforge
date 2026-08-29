expected_output = {
    "interface": {
        "GigabitEthernet0/0/0": {
            "interface_state": "up",
            "protocol_state": "up",
            "link_local_address": "",
            "ipv6_addresses": [],
        },
        "GigabitEthernet0/0/1": {
            "interface_state": "up",
            "protocol_state": "up",
            "link_local_address": "",
            "ipv6_addresses": [],
        },
        "GigabitEthernet0/0/2": {
            "interface_state": "administratively down",
            "protocol_state": "down",
            "link_local_address": "",
            "ipv6_addresses": [],
        },
        "GigabitEthernet0/0/3": {
            "interface_state": "administratively down",
            "protocol_state": "down",
            "link_local_address": "",
            "ipv6_addresses": [],
        },
        "Te0/0/4": {
            "interface_state": "up",
            "protocol_state": "up",
            "link_local_address": "FE80::9633:D8FF:FE01:6884",
            "ipv6_addresses": ["2015:A1::1"],
        },
        "Te0/0/5": {
            "interface_state": "up",
            "protocol_state": "up",
            "link_local_address": "FE80::9633:D8FF:FE01:6885",
            "ipv6_addresses": ["2060:A1::1"],
        },
        "Te0/1/0": {
            "interface_state": "administratively down",
            "protocol_state": "down",
            "link_local_address": "",
            "ipv6_addresses": [],
        },
        "Te1/0/0": {
            "interface_state": "administratively down",
            "protocol_state": "down",
            "link_local_address": "",
            "ipv6_addresses": [],
        },
        "Sdwan-system-intf": {
            "interface_state": "up",
            "protocol_state": "up",
            "link_local_address": "",
            "ipv6_addresses": [],
        },
        "vmanage_system": {
            "interface_state": "up",
            "protocol_state": "up",
            "link_local_address": "",
            "ipv6_addresses": [],
        },
        "Loopback65528": {
            "interface_state": "up",
            "protocol_state": "up",
            "link_local_address": "",
            "ipv6_addresses": [],
        },
        "Loopback65529": {
            "interface_state": "up",
            "protocol_state": "up",
            "link_local_address": "",
            "ipv6_addresses": [],
        },
        "Tunnel2": {
            "interface_state": "up",
            "protocol_state": "up",
            "link_local_address": "",
            "ipv6_addresses": [],
        },
        "Tunnel101": {
            "interface_state": "up",
            "protocol_state": "up",
            "link_local_address": "FE80::9633:D8FF:FE01:6880",
            "ipv6_addresses": ["2015:A1::1"],
            "unnumbered": {"interface_ref": "TenGigabitEthernet0/0/4"},
        },
    }
}
