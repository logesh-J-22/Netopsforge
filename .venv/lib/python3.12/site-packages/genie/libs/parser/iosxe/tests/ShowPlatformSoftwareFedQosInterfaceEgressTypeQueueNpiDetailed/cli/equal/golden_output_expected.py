expected_output = {
    'classmap': {
        'class-default': {
            'cgid': '0x383810',
            'child_classes': 0,
            'class_seq_number': '0xFFFFFFFF',
            'clid': '0x639',
            'filter': {
                'filter_match_any': {
                    'value': '0x0',
                },
            },
            'null_bind_count': 3,
            'tccg_ref_count': 3,
        },
        'tc6': {
            'cgid': '0x383810',
            'child_classes': 0,
            'class_seq_number': '0x4003FE',
            'clid': '0x7A661',
            'filter': {
                'filter_match_traffic_class': {
                    'value': '0x6',
                },
            },
            'null_bind_count': 3,
            'tccg_ref_count': 3,
        },
        'tc7': {
            'cgid': '0x383810',
            'child_classes': 0,
            'class_seq_number': '0x1FFFFF',
            'clid': '0x7A671',
            'filter': {
                'filter_match_traffic_class': {
                    'value': '0x7',
                },
            },
            'null_bind_count': 3,
            'tccg_ref_count': 3,
        },
    },
    'interface': {
        'GigabitEthernet2/0/2': {
            'cgid': '0x383810',
            'filter_state': 'UP TO DATE',
            'no_of_classes': 3,
            'tcg_ref_count': 3,
            'vmr_state': 'DIRTY',
        },
    },
    'tcg': {
        'npi_tcg': {
            'child_tcg': 0,
            'config_state': 'VALID',
            'mark_action': 0,
            'no_of_tccg': 3,
            'operational_state': 'IN HARDWARE',
            'parent_info': ['0x0', '0x0', '0'],
            'police_action': 0,
            'queue_action': 3,
        },
        'tccg': {
            '0': {
                'action': {
                    '0': {
                        'action_type': 'Queueing',
                        'attributes': '0x7 (QPARAMS, SHAPE, PRIORITY)',
                        'priority_parameters': {
                            'level': 1,
                        },
                        'queue_id': 7,
                        'queue_parameters': {
                            'queue_limit': '32256 Bytes',
                        },
                        'shape_parameters': {
                            'cir': 100000000,
                        },
                    },
                },
                'child_cgid': '0x0',
                'class_map_name': 'tc7',
                'clid': '0x7A671',
                'null_bind': True,
            },
            '1': {
                'action': {
                    '0': {
                        'action_type': 'Queueing',
                        'attributes': '0x1 (QPARAMS)',
                        'queue_id': 6,
                        'queue_parameters': {
                            'bandwidth_remaining_ratio': 16,
                            'queue_limit': '96000 Bytes',
                        },
                    },
                },
                'child_cgid': '0x0',
                'class_map_name': 'tc6',
                'clid': '0x7A661',
                'null_bind': True,
            },
            '2': {
                'action': {
                    '0': {
                        'action_type': 'Queueing',
                        'attributes': '0x9 (QPARAMS, WRED)',
                        'default_queue': True,
                        'queue_id': 0,
                        'queue_parameters': {
                            'bandwidth_remaining_ratio': 16,
                            'queue_limit': '96000 Bytes',
                        },
                        'wred_parameters': {
                            'configured_discard_classes': 2,
                            'discard_classes': {
                                0: {
                                    'mark_prob_denom': 1,
                                    'max_thresh': 100,
                                    'min_thresh': 90,
                                },
                                1: {
                                    'mark_prob_denom': 1,
                                    'max_thresh': 100,
                                    'min_thresh': 80,
                                },
                            },
                            'exponential_weighting_constant': 1,
                            'mode': 'Discard Class',
                            'threshold_unit': 'Percent',
                        },
                    },
                },
                'child_cgid': '0x0',
                'class_map_name': 'class-default',
                'clid': '0x639',
                'null_bind': True,
            },
        },
    },
}
