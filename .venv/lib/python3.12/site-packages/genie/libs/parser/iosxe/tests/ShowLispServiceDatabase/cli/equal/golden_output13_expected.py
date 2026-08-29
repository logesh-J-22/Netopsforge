expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4: {
                    'eid_table': 'N/A',
                    'lsb': '0x1',
                    'entries': {
                        'total': 3,
                        'no_route': 0,
                        'inactive': 0,
                        'do_not_register': 0,
                        'eids': {
                            'dual-stack': {
                                'eid': 'dual-stack',
                                'locator_set': 'RLOC',
                                'uptime': '00:41:19',
                                'last_change': '00:41:19',
                                'domain_id': 'local',
                                'service_insertion': 'N/A',
                                'locators': {
                                    '100.11.11.11': {
                                        'priority': 10,
                                        'weight': 50,
                                        'source': 'cfg-intf',
                                        'location': 'site-self',
                                        'state': 'reachable'
                                    }
                                }
                            },
                            'firewall': {
                                'eid': 'firewall',
                                'locator_set': 'RLOC',
                                'uptime': '00:41:25',
                                'last_change': '00:41:25',
                                'domain_id': 'local',
                                'service_insertion': 'N/A',
                                'locators': {
                                    '100.11.11.11': {
                                        'priority': 10,
                                        'weight': 50,
                                        'source': 'cfg-intf',
                                        'location': 'site-self',
                                        'state': 'reachable'
                                    }
                                }
                            },
                            'internet': {
                                'eid': 'internet',
                                'locator_set': 'RLOC',
                                'uptime': '00:00:09',
                                'last_change': '00:00:09',
                                'domain_id': 'local',
                                'service_insertion': 'N/A',
                                'locators': {
                                    '100.11.11.11': {
                                        'priority': 10,
                                        'weight': 50,
                                        'source': 'cfg-intf',
                                        'location': 'site-self',
                                        'state': 'reachable'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}