expected_output = {
    'flow_record_name': {
        'mpls-bt': {
            'description': 'User defined',
            'no_of_users': 1,
            'total_field_space': 85,
            'fields': {
                'match_list': [
                    'ipv4 ttl',
                    'ipv4 source address',
                    'ipv4 destination address',
                    'ipv6 flow-label',
                    'ipv6 protocol',
                    'ipv6 source address',
                    'ipv6 destination address',
                    'transport source-port',
                    'transport destination-port',
                    'interface input',
                    'mpls label 1 ttl',
                    'mpls label 1 exp',
                    'mpls label 1 type',
                    'mpls label 1 details',
                    'routing pw destination address',
                ],
                'collect_list': [
                    'ipv6 version',
                    'ipv6 traffic-class',
                    'interface output',
                    'counter bytes',
                    'counter packets',
                    'timestamp sys-uptime first',
                    'timestamp sys-uptime last',
                ],
            },
        },
    },
}
