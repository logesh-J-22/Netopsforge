"""  show_mpls.py
   supported commands:
   *  show mpls tp summary
        *  show mpls l2transport summary
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional

from genie.libs.parser.utils.common import Common


class ShowMplsL2TransportSummarySchema(MetaParser):
    '''Schema for show mpls l2transport summary'''
    schema = {
        'destination_address': {
            Any(): {
                'total_number_of_vc': int,
                'vc_status': {
                    'unknown': int,
                    'up': int,
                    'down': int,
                    'admin_down': int,
                    'recovering': int,
                    'standby': int,
                    'hotstandby': int,
                },
                'active_vc': {
                    Any(): {
                        'count': int,
                    }
                }
            }
        }
    }


class ShowMplsL2TransportSummary(ShowMplsL2TransportSummarySchema):
    '''Parser for show mpls l2transport summary'''
    cli_command = 'show mpls l2transport summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed = {}
        current_dest = None

        #Destination address: 101.1.1.1, total number of vc: 10
        p1 = re.compile(r'^Destination address: +(?P<destination_address>[\d\.]+), +total number of vc: +(?P<total_number_of_vc>\d+)$')

        #0 unknown, 10 up, 0 down, 0 admin down, 0 recovering, 0 standby, 0 hotstandby
        p2 = re.compile(r'^(?P<unknown>\d+) unknown, +(?P<up>\d+) up, +(?P<down>\d+) down, +(?P<admin_down>\d+) admin down, +(?P<recovering>\d+) recovering, +(?P<standby>\d+) standby, +(?P<hotstandby>\d+) hotstandby$')

        #5 active vc on MPLS interface Tp1
        p3 = re.compile(r'^(?P<count>\d+) active vc on MPLS interface +(?P<interface>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            #Destination address: 101.1.1.1, total number of vc: 10
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_dest = group['destination_address']
                dest_dict = parsed.setdefault('destination_address', {}).setdefault(current_dest, {})
                dest_dict['total_number_of_vc'] = int(group['total_number_of_vc'])
                continue

            if current_dest is None:
                continue

            dest_dict = parsed['destination_address'][current_dest]

            #0 unknown, 10 up, 0 down, 0 admin down, 0 recovering, 0 standby, 0 hotstandby
            m = p2.match(line)
            if m:
                group = m.groupdict()
                dest_dict['vc_status'] = {k: int(v) for k, v in group.items()}
                continue

            #5 active vc on MPLS interface Tp1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                dest_dict.setdefault('active_vc', {})[interface] = {'count': int(group['count'])}

        return parsed