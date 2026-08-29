expected_output = {
 "total_sessions": 1,
 "sessions": {
  "2": {
   "type": "IPv4",
   "uid": 2,
   "state": "authen",
   "identity": "rouble-pppoe",
   "ipv4_address": "10.0.0.2",
   "session_up_time": "00:01:37",
   "last_changed": "00:00:02",
   "switch_id": 4102,
   "policy_information": {
    "authentication_status": "authen",
    "active_services": [
     "keepAliveSvc",
     "transparent-service"
    ],
    "rules_actions_conditions_executed": [
     {
      "type": "subscriber condition-map",
      "mode": "match-all",
      "name": "CONDA",
      "matches": [
       {
        "identifier": "source-ip-address",
        "ip": "10.0.0.2",
        "mask": "255.255.255.255",
        "result": "TRUE"
       }
      ]
     },
     {
      "type": "subscriber rule-map",
      "name": "START_RULE",
      "condition": {
       "name": "CONDA",
       "event": "session-start",
       "actions": [
        {
         "sequence": 1,
         "command": "authorize aaa list author_list identifier source-ip-address"
        }
       ]
      }
     },
     {
      "type": "subscriber rule-map",
      "name": "default-internal-rule",
      "condition": {
       "name": "always",
       "event": "service-start",
       "actions": [
        {
         "sequence": 1,
         "command": "service-policy type service identifier service-name"
        }
       ]
      }
     },
     {
      "type": "subscriber rule-map",
      "name": "default-internal-rule",
      "condition": {
       "name": "always",
       "event": "service-start",
       "actions": [
        {
         "sequence": 1,
         "command": "service-policy type service identifier service-name"
        }
       ]
      }
     }
    ]
   },
   "classifiers": {
    0: {
     "class_id": 0,
     "direction": "In",
     "packets": 9,
     "bytes": 1026,
     "priority": 0,
     "definition": "Match Any"
    },
    1: {
     "class_id": 1,
     "direction": "Out",
     "packets": 17,
     "bytes": 1938,
     "priority": 0,
     "definition": "Match Any"
    },
    2: {
     "class_id": 2,
     "direction": "In",
     "packets": 8,
     "bytes": 800,
     "priority": 0,
     "definition": "Match ACL 102"
    }
   },
   "template_id": 9,
   "static_routes": {
    0: {
     "class_id": 0,
     "configuration_status": "This feature is enabled",
     "source": "Peruser"
    }
   },
   "prepaid_time_monitor": {
    2: {
     "class_id": 2,
     "direction": "In",
     "threshold": 380,
     "quota": 400,
     "session_time": 73,
     "source": "transparent-service"
    }
   },
   "prepaid_volume_monitor": {
    2: {
     "class_id": 2,
     "direction": "In",
     "packets": 0,
     "bytes": 0,
     "source": "transparent-service"
    },
    "usage": {
     "since_last_update": 0,
     "total": 0
    },
    "thresholds": {
     "threshold": 300,
     "quota": 500
    },
    "post_tariff_thresholds": {
     "threshold": 800,
     "quota": 1000
    },
    "current_states": "Start Tariff-switched"
   },
   "keepalive": {
    0: {
     "class_id": 0,
     "idle_period": 60,
     "attempts": 5,
     "interval": 1,
     "protocol": "ICMP",
     "source": "keepAliveSvc"
    }
   },
   "configuration_sources": [
    {
     "type": "SVC",
     "active_time": "00:01:13",
     "aaa_service_id": "-",
     "name": "transparent-service"
    },
    {
     "type": "USR",
     "active_time": "00:01:37",
     "aaa_service_id": "-",
     "name": "Peruser"
    },
    {
     "type": "SVC",
     "active_time": "00:00:02",
     "aaa_service_id": "-",
     "name": "keepAliveSvc"
    },
    {
     "type": "INT",
     "active_time": "00:01:37",
     "aaa_service_id": "-",
     "name": "FastEthernet0/3/0"
    }
   ]
  }
 }
}
