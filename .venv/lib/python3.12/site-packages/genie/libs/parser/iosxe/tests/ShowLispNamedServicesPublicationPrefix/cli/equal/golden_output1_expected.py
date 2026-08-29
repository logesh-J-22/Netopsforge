expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4: {
                    'eid_prefixes': {
                        'firewall': {
                            'first_published': '00:02:20',
                            'last_published': '00:02:20',
                            'state': 'complete',
                            'exported_to': ['map-cache'],
                            'publishers': {
                                '100.44.44.44:4342': {
                                    'port': 4342,
                                    'last_published': '00:02:20',
                                    'ttl': 'never',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x50B8AF6A-0x8EBE65AE-0x11AE0789-0xEC78F6DB',
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
                                },
                                '100.55.55.55:4342': {
                                    'port': 4342,
                                    'last_published': '00:02:20',
                                    'ttl': 'never',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x50B8AF6A-0x8EBE65AE-0x11AE0789-0xEC78F6DB',
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
