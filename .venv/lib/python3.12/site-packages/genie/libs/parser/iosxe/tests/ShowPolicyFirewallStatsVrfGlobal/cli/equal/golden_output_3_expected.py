expected_output = {
 "vrf": {
  "global": {
   "global_table_statistics": {
    "total_session": {
     "count_estab_plus_half_open": 102,
     "exceed": 1000
    },
    "total_session_aggressive_aging": {
     "period": "On",
     "event_count": 1000
    },
    "half_open": {
     "protocols": {
      "all": {
       "session_count": 200,
       "exceed": 564280
      },
      "udp": {
       "session_count": 100,
       "exceed": 100
      },
      "icmp": {
       "session_count": 100,
       "exceed": 100
      },
      "tcp": {
       "session_count": 300,
       "exceed": 153
      }
     },
     "tcp_syn_flood": {
      "half_open_count": 301,
      "exceed": 1000
     },
     "aggressive_aging": {
      "period": "Off",
      "event_count": 1000
     }
    }
   }
  }
 }
}