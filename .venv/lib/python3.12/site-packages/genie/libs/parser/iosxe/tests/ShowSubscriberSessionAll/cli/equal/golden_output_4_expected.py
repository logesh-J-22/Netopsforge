expected_output = {
    "total_sessions": 1,
    "sessions": {
        "915": {
            "type": "IPv4/IPv6",
            "uid": 915,
            "state": "authen",
            "identity": "aaaa.bbbb.cccc",
            "ipv4_address": "11.11.11.2",
            "ipv6_address": "8001::",
            "policy_information": {
                "rules_actions_conditions_executed": [
                    {
                        "type": "subscriber rule-map",
                        "name": "TAL",
                        "condition": {
                            "name": "always",
                            "event": "session-start",
                            "actions": [
                                {
                                    "sequence": 10,
                                    "command": "authorize identifier mac-address"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
}
