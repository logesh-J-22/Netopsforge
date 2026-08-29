expected_output = {
    'instance': {
        'default': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv4 unicast': {
                            'prefixes': {
                                '10.84.1.1/32': {
                                    'table_version': '10',
                                    'available_path': '2',
                                    'best_path': '2',
                                    'paths': '2 available, best #2, table default',
                                    'index': {
                                        1: {
                                            'next_hop': '2001:3:5:1::5',
                                            'next_hop_link_local': 'FE80:3:5:1::5',
                                            'gateway': '2001:3:5:1::5',
                                            'originator': '5.5.5.5',
                                            'localpref': 100,
                                            'origin_codes': '?',
                                            'status_codes': '* ',
                                            'refresh_epoch': 1,
                                            'route_info': '64512.64201 64512.64201 64512',
                                            'update_group': 1,
                                            'recipient_pathid': '0',
                                            'transfer_pathid': '0',
                                        },
                                        2: {
                                            'next_hop': '2001:2:3:1::2',
                                            'next_hop_link_local': 'FE80:2:3:1::2',
                                            'gateway': '2001:2:3:1::2',
                                            'originator': '2.2.2.2',
                                            'metric': 0,
                                            'localpref': 100,
                                            'origin_codes': '?',
                                            'status_codes': '*>',
                                            'refresh_epoch': 2,
                                            'route_info': '64512',
                                            'update_group': 1,
                                            'recipient_pathid': '0',
                                            'transfer_pathid': '0x0',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
