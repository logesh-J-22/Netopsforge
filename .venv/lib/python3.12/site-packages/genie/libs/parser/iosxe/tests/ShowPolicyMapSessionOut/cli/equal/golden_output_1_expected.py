expected_output = {
 "sessions": {
  "16": {
   "service_policy": {
    "direction": "output",
    "name": "ShaperDT",
    "class_map": {
     "class-default": {
      "match_type": "match-any",
      "match": "any",
      "queueing": True,
      "counters": {
       "packets": 0,
       "bytes": 0,
       "interval_seconds": 30,
       "offered_rate_bps": 0,
       "drop_rate_bps": 0,
       "pkts_output": 0,
       "bytes_output": 0
      },
      "queue": {
       "limit_packets": 64,
       "queue_depth": 0,
       "total_drops": 0,
       "no_buffer_drops": 0
      },
      "shape": {
       "type": "average",
       "cir": 10000,
       "bc": 40,
       "be": 40,
       "target_shape_rate_bps": 10000
      }
     }
    }
   }
  }
 }
}