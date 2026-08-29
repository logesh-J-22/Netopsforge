expected_output={
  'device': {
    1: {
      'dev_code': 'L',
      'link_layer_address': 'aabb.cc81.f6ff',
      'interface': 'BD12',
      'vlan_id': 12,
      'pref_level': 'TRUSTED',
      'state': 'MAC-REACHABLE',
      'policy': 'evpn-device-track',
      'time_left': 'N/A',
      'input_index': 22,
      'attached': {
      }
    },
    2: {
      'dev_code': 'L',
      'link_layer_address': 'aabb.cc81.f6ff',
      'interface': 'BD22',
      'vlan_id': 22,
      'pref_level': 'TRUSTED',
      'state': 'MAC-REACHABLE',
      'policy': 'evpn-device-track',
      'time_left': 'N/A',
      'input_index': 23,
      'attached': {
      }
    },
    3: {
      'dev_code': 'L3F',
      'link_layer_address': 'aabb.0000.0002',
      'interface': 'Et1/0',
      'vlan_id': 12,
      'pref_level': 'NO TRUST',
      'state': 'MAC-REACHABLE',
      'policy': 'evpn-device-track',
      'time_left': '188 s',
      'input_index': 12,
      'attached': {
        1: {
          'ip': '192.168.12.2'
        },
        2: {
          'ip': '2001:12::2'
        },
        3: {
          'ip': 'FE80::A8BB:FF:FE00:2'
        }
      }
    },
    4: {
      'dev_code': 'L3F',
      'link_layer_address': 'aabb.0000.0002',
      'interface': 'Et1/0',
      'vlan_id': 22,
      'pref_level': 'NO TRUST',
      'state': 'MAC-REACHABLE',
      'policy': 'evpn-device-track',
      'time_left': '184 s',
      'input_index': 22,
      'attached': {
        1: {
          'ip': '192.168.22.2'
        },
        2: {
          'ip': '2001:22::2'
        },
        3: {
          'ip': 'FE80::A8BB:FF:FE00:2'
        }
      }
    },
    5: {
      'dev_code': 'L',
      'link_layer_address': '0022.0022.0022',
      'interface': 'BD22',
      'vlan_id': 22,
      'pref_level': 'TRUSTED',
      'state': 'MAC-REACHABLE',
      'policy': 'evpn-device-track',
      'time_left': 'N/A',
      'input_index': 23,
      'attached': {
        1: {
          'ip': '192.168.22.254'
        },
        2: {
          'ip': 'FE80::222:FF:FE22:22'
        },
        3: {
          'ip': '2001:22::254'
        }
      }
    },
    6: {
      'dev_code': 'L',
      'link_layer_address': '0012.0012.0012',
      'interface': 'BD12',
      'vlan_id': 12,
      'pref_level': 'TRUSTED',
      'state': 'MAC-REACHABLE',
      'policy': 'evpn-device-track',
      'time_left': 'N/A',
      'input_index': 22,
      'attached': {
        1: {
          'ip': '192.168.12.254'
        },
        2: {
          'ip': 'FE80::212:FF:FE12:12'
        },
        3: {
          'ip': '2001:12::254'
        }
      }
    }
  }
}

