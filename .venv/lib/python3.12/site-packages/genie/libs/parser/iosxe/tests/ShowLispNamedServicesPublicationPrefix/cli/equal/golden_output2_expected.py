expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4: {
                    'eid_prefixes': {
                        'firewall': {
                            'first_published': '00:15:11',
                            'last_published': '00:15:11',
                            'state': 'complete',
                            'exported_to': ['map-cache'],
                            'publishers': {
                                '100.44.44.44:4342': {
                                    'port': 4342,
                                    'last_published': '00:15:11',
                                    'ttl': 'never',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x54D0BE4C-0xD0BA3F79-0x6BF0D90D-0xD9DB8927',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': 'unspecified',
                                    'locators': {
                                        '100.11.11.11': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[-]'
                                        }
                                    }
                                }
                            },
                            'merged_locators': {
                                '100.11.11.11*': {
                                    'priority': 10,
                                    'weight': 50,
                                    'state': 'up',
                                    'encap_iid': '-',
                                    'rdp_len': 0,
                                    'src_add': '100.44.44.44',
                                    'publishers': {
                                        '100.44.44.44': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp_len': 0
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
}
