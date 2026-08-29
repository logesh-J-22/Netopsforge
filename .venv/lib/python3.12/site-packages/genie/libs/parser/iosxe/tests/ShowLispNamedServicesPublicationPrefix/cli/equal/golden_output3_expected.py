expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4: {
                    'eid_prefixes': {
                        'firewall': {
                            'exported_to': ['local-eid, map-cache'],
                            'first_published': '00:23:39',
                            'last_published': '00:23:39',
                            'merged_locators': {
                                '100.11.11.11*': {
                                    'encap_iid': '-',
                                    'priority': 10,
                                    'publishers': {
                                        '100.44.44.44': {
                                            'encap_iid': '-',
                                            'priority': 10,
                                            'rdp_len': 0,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'rdp_len': 0,
                                    'src_add': '100.44.44.44',
                                    'state': 'up',
                                    'weight': 50
                                }
                            },
                            'publishers': {
                                '100.44.44.44:4342': {
                                    'domain_id': '1',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:23:39',
                                    'locators': {
                                        '100.11.11.11': {
                                            'encap_iid': '-',
                                            'priority': 10,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'multihoming_id': 'unspecified',
                                    'port': 4342,
                                    'publisher_epoch': 0,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0x448314C7-0xDE55C581-0xB1535180-0x5ABD34BD'
                                },
                                '100.55.55.55:4342': {
                                    'domain_id': '1',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:23:39',
                                    'locators': {
                                        '100.11.11.11': {
                                            'encap_iid': '-',
                                            'priority': 10,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'multihoming_id': 'unspecified',
                                    'port': 4342,
                                    'publisher_epoch': 0,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0x448314C7-0xDE55C581-0xB1535180-0x5ABD34BD'
                                }
                            },
                            'state': 'complete'
                        }
                    }
                }
            }
        }
    }
}
