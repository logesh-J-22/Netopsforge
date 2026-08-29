expected_output = {
    'interchassis_redundancy_group': {
        '4294967295': {
            'backbone_uplink_status': 'Connected',
            'iccp_version': 0,
            'local_configuration': {
                'node_id': 1,
            },
            'p_mlacp_interfaces': {
                '1': {
                    'local_vlan_state': {
                        'primary': 'DN',
                        'secondary': 'DN',
                    },
                    'peer_vlan_state': {
                        'primary': 'ACT',
                        'secondary': 'ACT',
                    },
                    'port_state_local': 'DN',
                },
            },
            'peer_information': {
                'iccp_version': 0,
                'node_id': 2,
                'state': 'Up',
            },
            'rg_state': 'Synchronized',
            'states_legend': {
                'Active': 'ACT',
                'AdminDown': 'ADN',
                'Down': 'DN',
                'Reverting': 'REV',
                'Standby': 'SBY',
                'Unknown': 'UN',
            },
        },
    },
}