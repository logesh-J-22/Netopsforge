expected_output={
  'device': {
    1: {
      'dev_code': 'AUT',
      'link_layer_address': 'dead.beef.0033',
      'interface': 'Gi1/0/1',
      'vlan_id': 20,
      'pref_level': 'TRUSTED',
      'state': 'MAC-REACHABLE',
      'policy': 'LISP-DT-GUARD-VLAN',
      'time_left': '232 s',
      'input_index': 9,
      'attached': {
        1: {
          'ip': '20.0.0.21'
        }
      }
    },
    2: {
      'dev_code': 'L',
      'link_layer_address': 'ba25.cdf4.ad38',
      'interface': 'Vl20',
      'vlan_id': 20,
      'pref_level': 'TRUSTED',
      'state': 'MAC-REACHABLE',
      'policy': 'LISP-DT-GUARD-VLAN',
      'time_left': 'N/A',
      'input_index': 77,
      'attached': {
        1: {
          'ip': '20.0.0.254'
        },
        2: {
          'ip': 'FE80::B825:CDFF:FEF4:AD38'
        },
        3: {
          'ip': '2001::100'
        }
      }
    },
    3: {
      'dev_code': 'L',
      'link_layer_address': 'b0c5.3cc1.a556',
      'interface': 'Vl20',
      'vlan_id': 20,
      'pref_level': 'TRUSTED',
      'state': 'MAC-REACHABLE',
      'policy': 'LISP-DT-GUARD-VLAN',
      'time_left': 'N/A',
      'input_index': 77,
      'attached': {
      }
    }
  }
}

