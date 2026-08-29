expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4: {
                    'address_family': 'DN',
                    'eid_table': 'N/A',
                    'lsb': '0x1',
                    'entries_total': 1,
                    'no_route_entries': 0,
                    'inactive_entries': 0,
                    'do_not_register_entries': 0,
                    'all_no_route': False,
                    'eid_prefix': 'internet',
                    'eid_info': 'inherited from default locator-set RLOC',
                    'domain_id': 'local',
                    'locators': {
                        '100.11.11.11': {
                            'priority': 10,
                            'weight': 50,
                            'source': 'cfg-intf',
                            'state': 'site-self, reachable',
                            'config_missing': False
                        }
                    },
                    'map_servers': {
                        '100.44.44.44': {
                            'uptime': '00:00:07',
                            'ack': 'Yes',
                            'domain_id': '0'
                        },
                        '100.55.55.55': {
                            'uptime': '00:00:07',
                            'ack': 'Yes',
                            'domain_id': '0'
                        }
                    }
                }
            }
        }
    }
}
