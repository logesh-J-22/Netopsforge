expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4: {
                    'locator_table': 'default',
                    'eid_table': 'N/A',
                    'itr': {
                        'enabled': True,
                        'proxy_itr_router': False,
                        'local_rloc_last_resort': '100.22.22.22',
                        'solicit_map_request': 'accept and process',
                        'max_smr_per_map_cache': '8 more specifics',
                        'multiple_smr_supression_time': 2
                        },
                    'etr': {
                        'enabled': True,
                        'proxy_etr_router': False,
                        'accept_mapping_data': 'disabled, verify disabled',
                        'map_cache_ttl': '1d00h'
                        },
                    'nat_traversal_router': False,
                    'mobility_first_hop_router': 'disabled',
                    'map_server': {
                        'enabled': False
                        },
                    'map_resolver': {
                        'enabled': False
                        },
                    'mr_use_petr': {
                        'role': 'disabled'
                        },
                    'first_packet_petr': {
                        'role': 'disabled'
                        },
                    'multiple_ip_per_mac': False,
                    'delegated_database_tree': 'disabled',
                    'mcast_flood_access_tunnel': False,
                    'pub_sub': {
                        'role': True
                        },
                    'pub_sub_eid': True,
                    'site_registration_limit': 0,
                    'map_resolvers': {
                        '100.44.44.44': {
                            'mr_address': '100.44.44.44',
                            'prefix_list': '100.55.55.55'
                            }
                        },
                    'xtr_id': '0xBE7E13DC-0xF6206EDD-0x9BE5B662-0x19E0A35B',
                    'site_id': 'unspecified',
                    'locator_status_algorithms': {
                        'rloc_probe_algorithm': 'disabled',
                        'rloc_probe_on_route_change': False,
                        'rloc_probe_member_change': 'disabled',
                        'lsb_reports': 'process',
                        'ipv4_rloc_min_mask_len': 0,
                        'ipv6_rloc_min_mask_len': 0
                        },
                    'map_cache': {
                        'static_mappings': 0,
                        'size': 1,
                        'limit': 4294967295,
                        'imported_route': {
                            'count': 0,
                            'limit': 5000
                            },
                        'activity_check_period': 60,
                        'signal_supress': False,
                        'conservative_allocation': False,
                        'fib_updates': 'pre-init',
                        'persistent': 'disabled',
                        'activity_tracking': True
                        },
                    'database': {
                        'dummy_database': {
                            'limit': 4294967295,
                            'size': 0
                            },
                        'dynamic_database': {
                            'limit': 4294967295,
                            'size': 0
                            },
                        'import_publication': {
                            'limit': 4294967295,
                            'size': 0
                            },
                        'import_site_reg': {
                            'limit': 4294967295,
                            'size': 0
                            },
                        'inactive': {
                            'size': 0
                            },
                        'proxy_database': {
                            'size': 0
                            },
                        'route_import': {
                            'limit': 5000,
                            'size': 0
                            },
                        'static_database': {
                            'limit': 4294967295,
                            'size': 2
                            },
                        'total_database_mapping': 2
                        },
                    'publication_entries_exported': {
                        'map_cache': 0,
                        'rib': 0,
                        'database': 0,
                        'prefix_list': 0
                        },
                    'site_reg_entries_exported': {
                        'map_cache': 0,
                        'rib': 0
                        },
                    'encapsulation_type': 'vxlan'
                    }
                }
            }
        }
    }