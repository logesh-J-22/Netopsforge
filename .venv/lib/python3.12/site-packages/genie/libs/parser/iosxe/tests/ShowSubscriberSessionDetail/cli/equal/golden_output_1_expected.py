expected_output = {
 "sessions": {
  1: {
   "type": "PPPoE",
   "uid": 1,
   "state": "authen",
   "identity": "qinq_customer",
   "ipv4_address": "135.1.1.1",
   "session_uptime": "00:00:03",
   "last_changed": "00:00:00",
   "interface": "Virtual-Access1.1",
   "switch_id": 4098,
   "policy_information": {
    "context": "7F29E1B05A38",
    "handle": "D0000001",
    "aaa_id": "0000000D",
    "flow_handle": 0,
    "authentication_status": "authen",
    "downloaded_user_profile": {
     "excluding_services": [
      {"attribute": "service-type", "sequence": 0, "value": "2 [Framed]"},
      {"attribute": "qos-policy-out", "sequence": 0, "value": "add-class(sub,(class-default,voip),shape(64000),queue-limit(30))"},
      {"attribute": "qos-policy-in", "sequence": 0, "value": "add-class(sub,(class-default,mission-critical),police(200000,9216,1000,transmit,drop,drop))"},
      {"attribute": "qos-policy-out", "sequence": 0, "value": "add-class(sub,(class-default,mission-critical),bw-abs(64),set-ip-prec(5))"},
      {"attribute": "qos-policy-in", "sequence": 0, "value": "add-class(sub,(class-default,voip),set-ip-dscp(46))"},
      {"attribute": "sub-qos-policy-in", "sequence": 0, "value": "ISG-3"},
      {"attribute": "sub-qos-policy-out", "sequence": 0, "value": "ISG-7"}
     ],
     "including_services": [
      {"attribute": "service-type", "sequence": 0, "value": "2 [Framed]"},
      {"attribute": "username", "sequence": 0, "value": "isg_acct1"},
      {"attribute": "traffic-class", "sequence": 0, "value": "input access-group name isg_acl1"},
      {"attribute": "traffic-class", "sequence": 0, "value": "output access-group name isg_acl1"},
      {"attribute": "accounting-list", "sequence": 0, "value": "AAA_LIST"},
      {"attribute": "qos-policy-out", "sequence": 0, "value": "add-class(sub,(class-default,voip),shape(64000),queue-limit(30))"},
      {"attribute": "qos-policy-in", "sequence": 0, "value": "add-class(sub,(class-default,mission-critical),police(200000,9216,1000,transmit,drop,drop))"},
      {"attribute": "qos-policy-out", "sequence": 0, "value": "add-class(sub,(class-default,mission-critical),bw-abs(64),set-ip-prec(5))"},
      {"attribute": "qos-policy-in", "sequence": 0, "value": "add-class(sub,(class-default,voip),set-ip-dscp(46))"},
      {"attribute": "sub-qos-policy-in", "sequence": 0, "value": "ISG-3"},
      {"attribute": "sub-qos-policy-out", "sequence": 0, "value": "ISG-7"}
     ]
    }
   },
   "config_history": [
    {
     "access_type": "PPP",
     "client": "Push Command-Handler",
     "policy_event": "Process Config",
     "profile": {
      "name": "qinq_customer",
      "references": 2,
      "attributes": [
       {"attribute": "qos-policy-out", "sequence": 0, "value": "add-class(sub,(class-default,voip),shape(64000),queue-limit(30))"},
       {"attribute": "qos-policy-in", "sequence": 0, "value": "add-class(sub,(class-default,mission-critical),police(200000,9216,1000,transmit,drop,drop))"},
       {"attribute": "qos-policy-out", "sequence": 0, "value": "add-class(sub,(class-default,mission-critical),bw-abs(64),set-ip-prec(5))"},
       {"attribute": "qos-policy-in", "sequence": 0, "value": "add-class(sub,(class-default,voip),set-ip-dscp(46))"},
       {"attribute": "sub-qos-policy-in", "sequence": 0, "value": "ISG-3"},
       {"attribute": "sub-qos-policy-out", "sequence": 0, "value": "ISG-7"}
      ]
     }
    },
    {
     "access_type": "Web-service-logon",
     "client": "SM",
     "policy_event": "Apply Config Success (Service)",
     "profile": {
      "name": "isg_acct1",
      "references": 3,
      "attributes": [
       {"attribute": "password", "sequence": 0, "value": "<hidden>"},
       {"attribute": "username", "sequence": 0, "value": "isg_acct1"},
       {"attribute": "traffic-class", "sequence": 0, "value": "input access-group name isg_acl1"},
       {"attribute": "traffic-class", "sequence": 0, "value": "output access-group name isg_acl1"},
       {"attribute": "accounting-list", "sequence": 0, "value": "AAA_LIST"}
      ]
     }
    },
    {
     "access_type": "PPP",
     "client": "SM",
     "policy_event": "Process Config Connecting",
     "profile": {
      "name": "apply-config-only",
      "references": 2,
      "attributes": [
       {"attribute": "service-type", "sequence": 0, "value": "2 [Framed]"}
      ]
     }
    }
   ],
   "active_services": [
    {"name": "isg_acct1"}
   ],
   "rules_actions_conditions": [
    {
     "type": "subscriber rule-map",
     "name": "default-internal-rule",
     "conditions": [
      {
       "condition": "always",
       "event": "service-start",
       "actions": [
        "service-policy type service identifier service-name"
       ]
      }
     ]
    }
   ],
   "classifiers": {
    0: {"direction": "In", "packets": 0, "bytes": 0, "priority": 0, "definition": "Match Any"},
    1: {"direction": "Out", "packets": 0, "bytes": 0, "priority": 0, "definition": "Match Any"},
    2: {"direction": "In", "packets": 0, "bytes": 0, "priority": 0, "definition": "Match ACL isg_acl1"},
    3: {"direction": "Out", "packets": 0, "bytes": 0, "priority": 0, "definition": "Match ACL isg_acl1"}
   },
   "features": {},
   "qos_policy_map": {
    0: {"direction": "In", "policy_name": "ISG-3", "source": "Peruser"},
    1: {"direction": "Out", "policy_name": "ISG-7", "source": "Peruser"}
   },
   "accounting": {
    2: {"direction": "In", "packets": 0, "bytes": 0, "source": "isg_acct1"},
    3: {"direction": "Out", "packets": 0, "bytes": 0, "source": "isg_acct1"}
   },
   "configuration_sources": [
    {"type": "SVC", "active_time": "00:00:00", "aaa_service_id": "1090519041", "name": "isg_acct1"},
    {"type": "USR", "active_time": "00:00:03", "aaa_service_id": "-", "name": "Peruser"},
    {"type": "INT", "active_time": "00:00:03", "aaa_service_id": "-", "name": "Virtual-Template1"}
   ]
  }
 }
}