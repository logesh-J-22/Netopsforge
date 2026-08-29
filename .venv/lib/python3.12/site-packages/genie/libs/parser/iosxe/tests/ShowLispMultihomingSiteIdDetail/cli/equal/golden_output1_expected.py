expected_output = {
    'lisp_id': {
        0: {
            'multihoming_site_id': {
                123: {
                    'mode': 'Single-Active',
                    'peer_sync': 'Enabled',
                    'stp_tracking': 'Enabled',
                    'interfaces': ['Ethernet Gi1/0/1'],
                    'interface_status': 'Down',
                    'l2_host_count': 10,
                    'multihoming_peers': {
                        '100.11.11.11': {
                            'priority': 10,
                            'weight': 50,
                            'source': 'cfg-intf',
                            'state': 'site-self, reachable',
                        }
                    },
                    'df_status': {
                        'active': 4100,
                        'standby': 4101,
                    },
                },
                456: {
                    'mode': 'Single-Active',
                    'peer_sync': 'Enabled',
                    'stp_tracking': 'Enabled',
                    'interface_status': 'Up',
                    'l2_host_count': 10,
                    'multihoming_peers': {
                        '100.11.11.11': {
                            'priority': 10,
                            'weight': 50,
                            'source': 'cfg-intf',
                            'state': 'site-self, reachable',
                        }
                    },
                    'df_status': {
                        'active': 'All',
                        'standby': 'None',
                    },
                },
            }
        }
    }
}
