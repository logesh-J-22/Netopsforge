expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6": {
                    "instance": {
                        100: {
                            "router_id": "2.2.2.2",
                            "network": {
                                "2001:DB8:112::/64": {
                                    "type": 2,
                                    "metric": 20,
                                    "tag": 0,
                                    "origin": "connected (vrf VRF1) (connected)",
                                    "source_vrf": "VRF1",
                                    "via_network": "None",
                                    "interface": "Ethernet0/1",
                                },
                                "2001:DB8:400::1/128": {
                                    "type": 2,
                                    "metric": 20,
                                    "tag": 0,
                                    "origin": "connected (vrf VRF1) (connected)",
                                    "source_vrf": "VRF1",
                                    "via_network": "None",
                                    "interface": "Loopback40",
                                },
                                "2001:DB8:600::/64": {
                                    "type": 2,
                                    "metric": 20,
                                    "tag": 0,
                                    "origin": "static (vrf VRF1)",
                                    "source_vrf": "VRF1",
                                    "via_network": "None",
                                    "interface": "Null0",
                                },
                                "2001:DB8:1100::1/128": {
                                    "type": 2,
                                    "metric": 1,
                                    "tag": 65001,
                                    "origin": "bgp 65002 (vrf VRF1)",
                                    "source_vrf": "VRF1",
                                    "via_network": "FE80::A8BB:CCFF:FE00:9B10",
                                    "interface": "Ethernet0/1",
                                },
                                "2001:DB8:1200::1/128": {
                                    "type": 2,
                                    "metric": 20,
                                    "tag": 0,
                                    "origin": "eigrp 10 (vrf VRF1)",
                                    "source_vrf": "VRF1",
                                    "via_network": "FE80::A8BB:CCFF:FE00:9B10",
                                    "interface": "Ethernet0/1",
                                },
                            },
                        }
                    }
                }
            }
        },
        "VRF1": {
            "address_family": {
                "ipv6": {
                    "instance": {
                        100: {
                            "router_id": "2.2.2.2",
                            "network": {
                                "2001:DB8:12::/64": {
                                    "type": 2,
                                    "metric": 20,
                                    "tag": 0,
                                    "origin": "connected (connected)",
                                    "via_network": "None",
                                    "interface": "Ethernet0/0",
                                },
                                "2001:DB8:23::/64": {
                                    "type": 2,
                                    "metric": 20,
                                    "tag": 0,
                                    "origin": "connected (connected)",
                                    "via_network": "None",
                                    "interface": "Ethernet0/2",
                                },
                                "2001:DB8:100::1/128": {
                                    "type": 2,
                                    "metric": 1,
                                    "tag": 65001,
                                    "origin": "bgp 65002",
                                    "via_network": "FE80::A8BB:CCFF:FE00:9B00",
                                    "interface": "Ethernet0/0",
                                },
                                "2001:DB8:200::1/128": {
                                    "type": 2,
                                    "metric": 20,
                                    "tag": 0,
                                    "origin": "eigrp 10",
                                    "via_network": "FE80::A8BB:CCFF:FE00:9B00",
                                    "interface": "Ethernet0/0",
                                },
                                "2001:DB8:300::1/128": {
                                    "type": 2,
                                    "metric": 20,
                                    "tag": 0,
                                    "origin": "connected (connected)",
                                    "via_network": "None",
                                    "interface": "Loopback30",
                                },
                                "2001:DB8:500::/64": {
                                    "type": 2,
                                    "metric": 20,
                                    "tag": 0,
                                    "origin": "static",
                                    "via_network": "None",
                                    "interface": "Null0",
                                },
                            },
                        }
                    }
                }
            }
        },
    }
}
