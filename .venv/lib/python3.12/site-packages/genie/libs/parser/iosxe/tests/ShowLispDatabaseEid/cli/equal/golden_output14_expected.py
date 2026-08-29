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
                    'eid_prefix': 'default-etr',
                    'eid_info': 'import from publication, inherited from default locator-set RLOC, auto-discover-rlocs, proxy',
                    'domain_id': '1',
                    'locators': {
                        '100.88.88.88': {
                            'priority': 10,
                            'weight': 50,
                            'source': 'cfg-intf',
                            'state': 'site-self, reachable',
                            'config_missing': False
                        }
                    }
                }
            }
        }
    }
}
