"""show_lisp_l2_multihoming.py

IOSXE parsers for the following show commands:
    * show lisp multihoming site-id *
    * show lisp multihoming site-id * detail
    * show lisp multihoming site-id {site_id}
    * show lisp multihoming site-id {site_id} detail
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.metaparser.util.schemaengine import ListOf, Optional, Or


class ShowLispMultihomingSiteIdSchema(MetaParser):
    """Schema for:
        * show lisp multihoming site-id *
        * show lisp multihoming site-id * detail
        * show lisp multihoming site-id {site_id}
        * show lisp multihoming site-id {site_id} detail
    """

    schema = {
        'lisp_id': {
            int: {
                'multihoming_site_id': {
                    int: {
                        Optional('type'): str,
                        Optional('mode'): str,
                        Optional('peer_sync'): str,
                        Optional('stp_tracking'): str,
                        Optional('interfaces'): ListOf(str),
                        Optional('interface_status'): str,
                        Optional('l2_host_count'): int,
                        Optional('multihoming_peers'): {
                            str: {
                                'priority': int,
                                'weight': int,
                                'source': str,
                                'state': str,
                            }
                        },
                        Optional('df_status'): {
                            Optional('active'): Or(int, str),
                            Optional('standby'): Or(int, str),
                        },
                    }
                }
            }
        }
    }


class ShowLispMultihomingSiteId(ShowLispMultihomingSiteIdSchema):
    """Parser for:
        * show lisp multihoming site-id *
        * show lisp multihoming site-id {site_id}
    """

    cli_command = [
        'show lisp multihoming site-id {site_id}',
        'show lisp multihoming site-id *',
    ]

    def cli(self, site_id=None, msi=None, output=None):
        site_id = site_id or msi
        if output is None:
            if site_id:
                output = self.device.execute(self.cli_command[0].format(site_id=site_id))
            else:
                output = self.device.execute(self.cli_command[1])

        if not output.strip():
            raise SchemaEmptyParserError("Parser Output is empty")

        ret_dict = {}
        lisp_id_dict = {}
        site_dict = {}

        # LISP L2 Multihoming Information for LISP top ID 0
        p1 = re.compile(
            r'^LISP\s+L2\s+Multihoming\s+Information\s+for\s+LISP\s+top\s+ID\s+'
            r'(?P<lisp_id>\d+)$'
        )

        # Multihoming Site ID: 123
        p2 = re.compile(r'^Multihoming\s+Site\s+ID:\s+(?P<msi>\d+)$')

        # Type:                Single-Active
        # Mode:                Single-Active
        # Peer Sync:           Enabled
        # STP Tracking:        Enabled
        # Interface(s):        Ethernet Gi1/0/1
        # Interface Status:    Down
        # L2 Host Count:       10
        # Active: 4100
        # Standby: 4101
        p3 = re.compile(
            r'^(?P<key>Type|Mode|Peer\s+Sync|STP\s+Tracking|Interface\(s\)|'
            r'Interface\s+Status|L2\s+Host\s+Count|Active|Standby):\s+'
            r'(?P<value>.+)$'
        )

        # 100.11.11.11   10/50   cfg-intf   site-self, reachable
        p4 = re.compile(
            r'^(?P<locator>(\d{1,3}\.){3}\d{1,3}|[a-fA-F\d\:]+)\s+'
            r'(?P<priority>\d+)\/(?P<weight>\d+)\s+'
            r'(?P<source>\S+)\s+'
            r'(?P<state>site-self,\s+reachable|site-other,\s+report-reachable)$'
        )

        key_map = {
            'Type': 'type',
            'Mode': 'mode',
            'Peer Sync': 'peer_sync',
            'STP Tracking': 'stp_tracking',
            'Interface Status': 'interface_status',
            'L2 Host Count': 'l2_host_count',
        }

        def convert_df_value(value):
            return int(value) if value.isdigit() else value

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # LISP L2 Multihoming Information for LISP top ID 0
            m = p1.match(line)
            if m:
                lisp_id = int(m.groupdict()['lisp_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                continue

            # Multihoming Site ID: 123
            m = p2.match(line)
            if m:
                msi = int(m.groupdict()['msi'])
                site_dict = lisp_id_dict.setdefault('multihoming_site_id', {}).setdefault(msi, {})
                continue

            # 100.11.11.11   10/50   cfg-intf   site-self, reachable
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                locator = groups['locator']
                peer_dict = site_dict.setdefault('multihoming_peers', {}).setdefault(locator, {})
                peer_dict.update({
                    'priority': int(groups['priority']),
                    'weight': int(groups['weight']),
                    'source': groups['source'],
                    'state': groups['state'],
                })
                continue

            # Type:                Single-Active
            # Mode:                Single-Active
            # Peer Sync:           Enabled
            # STP Tracking:        Enabled
            # Interface(s):        Ethernet Gi1/0/1
            # Interface Status:    Down
            # L2 Host Count:       10
            # Active: 4100
            # Standby: 4101
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key']
                value = groups['value']

                if key == 'Interface(s)':
                    interfaces = [interface.strip() for interface in value.split(',') if interface.strip()]
                    site_dict.update({'interfaces': interfaces})
                elif key in ('Active', 'Standby'):
                    df_dict = site_dict.setdefault('df_status', {})
                    df_dict.update({key.lower(): convert_df_value(value)})
                elif key == 'L2 Host Count':
                    site_dict.update({key_map[key]: int(value)})
                elif key in key_map:
                    site_dict.update({key_map[key]: value})

        return ret_dict


class ShowLispMultihomingSiteIdDetail(ShowLispMultihomingSiteId):
    """Parser for:
        * show lisp multihoming site-id * detail
        * show lisp multihoming site-id {site_id} detail
    """

    cli_command = [
        'show lisp multihoming site-id {site_id} detail',
        'show lisp multihoming site-id * detail',
    ]
