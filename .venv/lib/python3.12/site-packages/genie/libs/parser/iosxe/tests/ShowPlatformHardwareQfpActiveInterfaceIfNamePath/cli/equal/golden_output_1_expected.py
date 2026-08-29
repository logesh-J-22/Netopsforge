expected_output = {
 "interface": {
  "GigabitEthernet0/0/0": {
   "interface_index": 12,
   "qfp_interface": "0x45",
   "state": "UP",
   "ingress_path": {
    "rx_path": "QFP_RX",
    "feature_path": "IPv4 CEF",
    "adjacency_type": "Connected",
    "rewrite_type": "Ethernet"
   },
   "egress_path": {
    "tx_path": "QFP_TX",
    "output_feature": "QoS",
    "encapsulation": "ARPA",
    "mtu": 1500
   },
   "statistics": {
    "packets_in_path": 12457892,
    "packets_out_path": 12399871,
    "packets_dropped": 15
   }
  }
 }
}