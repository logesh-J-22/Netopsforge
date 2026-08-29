expected_output = {
 "services": {
  "l4rdt": {
   "profile_name": "l4rdt",
   "references": 2,
   "attributes": [
    {"name": "password", "priority": 0, "value": "<hidden>"},
    {"name": "username", "priority": 0, "value": "l4rdt"},
    {"name": "traffic-class", "priority": 0, "value": "input access-group name isg_acl4"},
    {"name": "traffic-class", "priority": 0, "value": "output access-group name isg_acl4"},
    {"name": "l4redirect", "priority": 0, "value": "redirect to ip 10.1.1.1 port 1000 duration 100 frequency 100"},
    {"name": "accounting-list", "priority": 0, "value": "AAA_LIST"}
   ],
   "class_id_in": "00000050",
   "class_id_out": "00000051"
  },
  "l4rdt(l4addr=11.1.1.1,l4dur=500)": {
   "profile_name": "l4rdt(l4addr=11.1.1.1,l4dur=500)",
   "references": 3,
   "attributes": [
    {"name": "password", "priority": 0, "value": "<hidden>"},
    {"name": "username", "priority": 0, "value": "l4rdt"},
    {"name": "traffic-class", "priority": 0, "value": "input access-group name isg_acl4"},
    {"name": "traffic-class", "priority": 0, "value": "output access-group name isg_acl4"},
    {"name": "accounting-list", "priority": 0, "value": "AAA_LIST"},
    {"name": "l4redirect", "priority": 0, "value": "redirect to ip 11.1.1.1 port 1000 duration 500 frequency 100"}
   ],
   "class_id_in": "00000052",
   "class_id_out": "00000053"
  },
  "isg_acct1": {
   "profile_name": None,
   "references": None,
   "attributes": [],
   "class_id_in": None,
   "class_id_out": None
  },
  "l4rdt(l4addr=33.1.1.1,l4dur=300)": {
   "profile_name": None,
   "references": None,
   "attributes": [],
   "class_id_in": None,
   "class_id_out": None
  },
  "isg_acct1(tc_in=isg_acl2,tc_in=isg_acl3)": {
   "profile_name": None,
   "references": None,
   "attributes": [],
   "class_id_in": None,
   "class_id_out": None
  }
 },
 "current_subscriber_info": {
  "service": "l4rdt(l4addr=11.1.1.1,l4dur=500)",
  "total_sessions": 1,
  "sessions": [
   {
    "uniq_id": 22,
    "interface": "Vi1.1",
    "state": "authen",
    "service_code": "Lterm",
    "up_time": "00:00:15",
    "tc_ct": 1,
    "identifier": "qinq_customer"
   }
  ]
 }
}