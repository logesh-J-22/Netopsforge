expected_output = {
 "vrf": {
  "global": {
   "global_table_statistics": {
    "total_session": {
     "count_estab_plus_half_open": 502,
     "exceed": 0
    },
    "total_session_aggressive_aging": {
     "period": "Off",
     "event_count": 0
    },
    "half_open": {
     "protocols": {
      "all": {
       "session_count": 500,
       "exceed": 232667
      },
      "udp": {
       "session_count": 0,
       "exceed": 0
      },
      "icmp": {
       "session_count": 500,
       "exceed": 0
      },
      "tcp": {
       "session_count": 0,
       "exceed": 0
      }
     },
     "tcp_syn_flood": {
      "half_open_count": 0,
      "exceed": 0
     },
     "aggressive_aging": {
      "period": "On",
      "event_count": 1
     }
    }
   }
  }
 }
}