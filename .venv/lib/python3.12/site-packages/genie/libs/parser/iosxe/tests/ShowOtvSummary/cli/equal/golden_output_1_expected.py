expected_output = {
 "otv": {
  "site_bridge_domain": 4,
  "total_overlays": 2,
  "overlays": {
   "1": {
    "overlay_id": 1,
    "vpn_name": "Northeast",
    "control_group": "225.22.22.22",
    "data_groups": ["232.5.0.0/8"],
    "join_interface": "Gi0/0/0",
    "state": "up"
   },
   "2": {
    "overlay_id": 2,
    "vpn_name": "Southwest",
    "control_group": "225.11.11.11",
    "data_groups": ["232.6.0.0/8"],
    "join_interface": "Gi0/0/1",
    "state": "down"
   }
  }
 }
}