expected_output = {
    "interfaces": {
        "Fif1/0/19": {
            "vlan": 100,
            "mac": "0011.2233.4456",
            "type": "SecureConfigured",
            "mac_addresses": {
                "00aa.bbcc.ddee": {
                    "vlan": 100,
                    "type": "SecureDynamic",
                    "remaining_age": "5 (I)",
                },
                "0011.2233.4455": {
                    "vlan": 100,
                    "type": "SecureConfigured",
                },
                "0011.2233.4456": {
                    "vlan": 100,
                    "type": "SecureConfigured",
                },
            },
        },
        "Hu1/0/36": {
            "vlan": 100,
            "mac": "00ff.eedd.ccbb",
            "type": "SecureConfigured",
        },
        "HundredGigE1/0/36": {
            "vlan": 100,
            "mac": "00ff.eedd.cccc",
            "type": "SecureConfigured",
        },
    },
    "total_addr_in_system": 1,
    "max_addr_limit_in_system": 4096,
}
