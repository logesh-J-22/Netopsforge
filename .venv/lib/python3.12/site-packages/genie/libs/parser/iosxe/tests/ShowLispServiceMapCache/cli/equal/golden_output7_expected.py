expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_instance_id": 0,
            "service": {
                "named-services": {
                    "service": "named-services",
                    "itr": {
                        "map_cache": {
                            "4": {
                                "vni": "4",
                                "entries": 1,
                                "mappings": {
                                    "firewall": {
                                        "id": "firewall",
                                        "creation_time": "00:00:16",
                                        "time_to_live": "23:59:43",
                                        "via": "transient-publication, complete",
                                        "eid": {
                                            "address_type": "dn-afi",
                                            "vrf": "N/A",
                                            "dn": {"dn": "firewall"},
                                        },
                                        "positive_mapping": {
                                            "rlocs": {
                                                1: {
                                                    "id": "1",
                                                    "uptime": "00:00:16",
                                                    "state": "up",
                                                    "priority": 10,
                                                    "weight": 50,
                                                    "encap_iid": "-",
                                                    "locator_address": {
                                                        "address_type": "ipv4-afi",
                                                        "virtual_network_id": "4",
                                                        "ipv4": {"ipv4": "100.11.11.11"},
                                                    },
                                                }
                                            }
                                        },
                                    }
                                },
                            }
                        }
                    },
                }
            },
        }
    }
}
