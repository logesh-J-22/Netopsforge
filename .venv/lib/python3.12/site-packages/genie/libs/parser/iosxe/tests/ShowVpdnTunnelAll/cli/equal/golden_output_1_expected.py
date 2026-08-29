expected_output = {
 "l2tp": {
  "total_tunnels": 1,
  "total_sessions": 1,
  "tunnels": {
   "679": {
    "status": "up",
    "remote_id": 58433,
    "active_sessions": 1,
    "initiated": "remote",
    "state": "established",
    "time_since_change": "00:00:07",
    "transport": {
     "protocol": "UDP",
     "protocol_num": 17
    },
    "remote": {
     "tunnel_name": "lac",
     "ip": "80.1.1.1",
     "port": 1701
    },
    "local": {
     "tunnel_name": "lns",
     "ip": "80.1.1.2",
     "port": 1701
    },
    "l2tp_class": "vg_ip2",
    "counters": {
     "since_last_clear": {
      "packets": {
       "sent": 4,
       "received": 0
      },
      "bytes": {
       "sent": 50,
       "received": 0
      },
      "last_clearing": "never"
     },
     "ignore_last_clear": {
      "packets": {
       "sent": 4,
       "received": 0
      },
      "bytes": {
       "sent": 50,
       "received": 0
      }
     }
    },
    "control": {
     "ns": 2,
     "nr": 4,
     "local_rws": 1024,
     "local_rws_is_default": True,
     "remote_rws": 1024,
     "in_use_remote_rws": 10,
     "congestion_control_enabled": False,
     "message_authentication_enabled": False,
     "zlb_acks_sent": 3
    },
    "pmtu_checking_enabled": False,
    "retransmission_time": {
     "current": 1,
     "max": 1,
     "units": "seconds"
    },
    "unsent_queue": {
     "size": 0,
     "max": 0
    },
    "resend_queue": {
     "size": 0,
     "max": 1
    },
    "total_resends": 0,
    "out_of_order": {
     "dropped_pkts": 0,
     "reorder_pkts": 0
    },
    "peer_auth_failures": 0,
    "no_session_pak_queue_check": {
     "current": 0,
     "of": 5
    },
    "retransmit_time_distribution": [0, 0, 0, 0, 0, 0, 0, 0, 0],
    "vpdn_group": "vg_ip2"
   }
  }
 }
}