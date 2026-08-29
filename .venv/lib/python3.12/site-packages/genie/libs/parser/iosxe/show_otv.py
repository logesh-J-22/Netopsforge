"""show_otv.py

IOSXE parsers for the following show commands:

    * show otv summary
    * show otv isis neighbors
    * show otv route
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf, Optional


# =====================================================
# Schema for 'show otv summary'
# =====================================================
class ShowOtvSummarySchema(MetaParser):
    """Schema for: show otv summary"""

    schema = {
        'otv': {
            Optional('site_bridge_domain'): int,
            Optional('total_overlays'): int,
            Optional('overlays'): {
                Any(): {
                    'overlay_id': int,
                    'vpn_name': str,
                    'control_group': str,
                    'data_groups': ListOf(str),
                    'join_interface': str,
                    'state': str,
                }
            },
        }
    }


# =====================================================
# Parser for 'show otv summary'
# =====================================================
class ShowOtvSummary(ShowOtvSummarySchema):
    """Parser for: show otv summary"""

    cli_command = 'show otv summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # OTV Configuration Information, Site Bridge-Domain: 4
        p_site = re.compile(
            r'^OTV\s+Configuration\s+Information,\s+'
            r'Site\s+Bridge-Domain\s*:\s*(?P<bd>\d+)\s*$'
        )

        # 1       Northeast       225.22.22.22    232.5.0.0/8       Gi0/0/0        UP
        p_overlay = re.compile(
            r'^(?P<id>\d+)\s+'
            r'(?P<vpn>\S+)\s+'
            r'(?P<ctrl>\S+)\s+'
            r'(?P<data>\S+)\s+'
            r'(?P<intf>\S+)\s+'
            r'(?P<state>\S+)\s*$'
        )

        #                                         232.5.1.0/8
        p_data_cont = re.compile(r'^(?P<data>\d+\.\d+\.\d+\.\d+/\d+)\s*$')

        # Total Overlay(s): 2
        p_total = re.compile(r'^Total\s+Overlay\(s\)\s*:\s*(?P<n>\d+)\s*$')

        last_overlay = None

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # OTV Configuration Information, Site Bridge-Domain: 4
            m = p_site.match(line)
            if m:
                ret_dict.setdefault('otv', {})['site_bridge_domain'] = int(m.group('bd'))
                continue

            # Total Overlay(s): 2
            m = p_total.match(line)
            if m:
                ret_dict.setdefault('otv', {})['total_overlays'] = int(m.group('n'))
                last_overlay = None
                continue

            # 1       Northeast       225.22.22.22    232.5.0.0/8       Gi0/0/0        UP
            m = p_overlay.match(line)
            if m:
                otv_dict = ret_dict.setdefault('otv', {})
                overlays = otv_dict.setdefault('overlays', {})
                ovid = m.group('id')
                overlays[ovid] = {
                    'overlay_id': int(ovid),
                    'vpn_name': m.group('vpn'),
                    'control_group': m.group('ctrl'),
                    'data_groups': [m.group('data')],
                    'join_interface': m.group('intf'),
                    'state': m.group('state').lower(),
                }
                last_overlay = overlays[ovid]
                continue

            #                                         232.5.1.0/8
            m = p_data_cont.match(line)
            if m and last_overlay is not None:
                last_overlay['data_groups'].append(m.group('data'))
                continue

        return ret_dict


# =====================================================
# Schema for 'show otv isis neighbors'
# =====================================================
class ShowOtvIsisNeighborsSchema(MetaParser):
    """Schema for: show otv isis neighbors"""

    schema = {
        'tag': {
            Any(): {
                'neighbors': {
                    Any(): {
                        'type': str,
                        'interface': str,
                        'ip_address': str,
                        'state': str,
                        'holdtime': int,
                        'circuit_id': str,
                    }
                }
            }
        },
    }


# =====================================================
# Parser for 'show otv isis neighbors'
# =====================================================
class ShowOtvIsisNeighbors(ShowOtvIsisNeighborsSchema):
    """Parser for: show otv isis neighbors"""

    cli_command = 'show otv isis neighbors'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        tag_dict = None

        # Tag Overlay1:
        p_tag = re.compile(r'^Tag\s+(?P<tag>\S+)\s*:\s*$')

        # u1          L1   Ov1        209.165.201.22     UP      22         u3.01
        p_neighbor = re.compile(
            r'^(?P<sysid>\S+)\s+'
            r'(?P<type>\S+)\s+'
            r'(?P<intf>\S+)\s+'
            r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+'
            r'(?P<state>\S+)\s+'
            r'(?P<hold>\d+)\s+'
            r'(?P<circuit>\S+)\s*$'
        )

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # Tag Overlay1:
            m = p_tag.match(line)
            if m:
                tag_dict = ret_dict.setdefault('tag', {}).setdefault(
                    m.group('tag'), {}).setdefault('neighbors', {})
                continue

            # u1          L1   Ov1        209.165.201.22     UP      22         u3.01
            m = p_neighbor.match(line)
            if m and tag_dict is not None:
                tag_dict[m.group('sysid')] = {
                    'type': m.group('type'),
                    'interface': m.group('intf'),
                    'ip_address': m.group('ip'),
                    'state': m.group('state'),
                    'holdtime': int(m.group('hold')),
                    'circuit_id': m.group('circuit'),
                }
                continue

        return ret_dict


# =====================================================
# Schema for 'show otv route'
# =====================================================
class ShowOtvRouteSchema(MetaParser):
    """Schema for: show otv route"""

    schema = {
        Optional('overlay'): {
            Any(): {
                Optional('vlan'): {
                    Any(): {
                        'mac': {
                            Any(): {
                                'inst': int,
                                'bd': int,
                                'ad': int,
                                'owner': str,
                                'next_hop': str,
                            }
                        }
                    }
                },
                'unicast_routes_displayed': int,
            }
        },
        Optional('total_unicast_routes_displayed'): int,
    }


# =====================================================
# Parser for 'show otv route'
# =====================================================
class ShowOtvRoute(ShowOtvRouteSchema):
    """Parser for: show otv route"""

    cli_command = 'show otv route'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        overlay_dict = None

        # OTV Unicast MAC Routing Table for Overlay1
        p_section = re.compile(
            r'^OTV\s+Unicast\s+MAC\s+Routing\s+Table\s+for\s+(?P<overlay>\S+)\s*$'
        )

        # 0    67   67     0007.0007.0009 20    OTV    232.1.2.3
        # 0    67   67     0102.0304.0506 40    BD Eng Gi0/0/1:SI67
        p_route = re.compile(
            r'^(?P<inst>\d+)\s+'
            r'(?P<vlan>\d+)\s+'
            r'(?P<bd>\d+)\s+'
            r'(?P<mac>[0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4})\s+'
            r'(?P<ad>\d+)\s+'
            r'(?P<owner>BD\s+Eng|\S+)\s+'
            r'(?P<nh>.+?)\s*$'
        )

        # 8 unicast routes displayed in Overlay1
        p_overlay_count = re.compile(
            r'^(?P<n>\d+)\s+unicast\s+routes\s+displayed\s+in\s+(?P<overlay>\S+)\s*$'
        )

        # 14 Total Unicast Routes Displayed
        p_total = re.compile(
            r'^(?P<n>\d+)\s+Total\s+Unicast\s+Routes\s+Displayed\s*$'
        )

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # OTV Unicast MAC Routing Table for Overlay1
            m = p_section.match(line)
            if m:
                overlay_dict = ret_dict.setdefault(
                    'overlay', {}).setdefault(m.group('overlay'), {})
                continue

            # 14 Total Unicast Routes Displayed
            m = p_total.match(line)
            if m:
                ret_dict['total_unicast_routes_displayed'] = int(m.group('n'))
                overlay_dict = None
                continue

            # 8 unicast routes displayed in Overlay1
            m = p_overlay_count.match(line)
            if m:
                ov = ret_dict.setdefault(
                    'overlay', {}).setdefault(m.group('overlay'), {})
                ov['unicast_routes_displayed'] = int(m.group('n'))
                continue

            # 0    67   67     0007.0007.0009 20    OTV    232.1.2.3
            m = p_route.match(line)
            if m and overlay_dict is not None:
                vlan = int(m.group('vlan'))
                vlan_dict = overlay_dict.setdefault(
                    'vlan', {}).setdefault(vlan, {})
                mac_dict = vlan_dict.setdefault('mac', {})
                mac_dict[m.group('mac')] = {
                    'inst': int(m.group('inst')),
                    'bd': int(m.group('bd')),
                    'ad': int(m.group('ad')),
                    'owner': re.sub(r'\s+', ' ', m.group('owner')),
                    'next_hop': m.group('nh'),
                }
                continue

        return ret_dict
