expected_output = {
 "port_channel": {
  "Port-Channel 1": {
   "local_configuration": {
    "p_mlacp_enabled": "Yes",
    "redundancy_group": 4294967295,
    "revertive_mode": "Revertive",
    "primary_vlans": 20,
    "secondary_vlans": 40
   },
   "local_interface_state": {
    "interface_id": 1,
    "port_state": "Admin Down",
    "fail_flags": "0x2",
    "primary_vlan_state": "Admin Down",
    "secondary_vlan_state": "Admin Down"
   },
   "peer_interface_state": {
    "interface_id": 1,
    "primary_vlan_state": "Active",
    "secondary_vlan_state": "Active"
   }
  }
 }
}