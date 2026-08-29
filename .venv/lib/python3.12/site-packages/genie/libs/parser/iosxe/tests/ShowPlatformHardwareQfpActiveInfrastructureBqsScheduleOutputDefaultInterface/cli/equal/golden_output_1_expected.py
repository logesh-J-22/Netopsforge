expected_output = {
 "interface": {
  "GigabitEthernet0/0/0": {
   "egress_scheduler": {
    "name": "Default",
    "scheduler_id": "0x1A",
    "scheduler_type": "Default",
    "parent_node": "Root",
    "state": "Active",
    "bandwidth_kbps": 1000000,
    "shaper_rate": None,
    "priority": None
   },
   "queue_statistics": {
    "total_packets_enqueued": 154321,
    "total_packets_dequeued": 154300,
    "total_packets_dropped": 21,
    "total_bytes_enqueued": 123456789,
    "total_bytes_dequeued": 123450000
   },
   "per_flow_class_queues": {
    0: {"weight": 1, "packets": 50234, "bytes": 42342342, "drops": 0},
    1: {"weight": 2, "packets": 40321, "bytes": 32342342, "drops": 5},
    2: {"weight": 4, "packets": 30210, "bytes": 22342342, "drops": 10},
    3: {"weight": 8, "packets": 20000, "bytes": 12342342, "drops": 6},
    4: {"weight": 1, "packets": 10000, "bytes": 8234234, "drops": 0},
    5: {"weight": 1, "packets": 5000, "bytes": 4234234, "drops": 0},
    6: {"weight": 1, "packets": 3000, "bytes": 2234234, "drops": 0},
    7: {"weight": 1, "packets": 556, "bytes": 123423, "drops": 0}
   },
   "child_queue_details": {
    0: {"weight": 1, "credits": 2048, "drops": 0, "state": "Active"},
    1: {"weight": 2, "credits": 2048, "drops": 5, "state": "Active"},
    2: {"weight": 4, "credits": 2048, "drops": 10, "state": "Active"},
    3: {"weight": 8, "credits": 2048, "drops": 6, "state": "Active"}
   }
  }
 }
}