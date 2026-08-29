''' show_smartpower.py

IOSXE revision 1 parsers for the following show commands:
   
    * show smartpower children
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.libs.parser.utils.common import Common
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

# ==========================================
# Schema for:
#   * 'show smartpower children'
# ==========================================
class ShowSmartPowerChildrenSchema(MetaParser):
    ''' Schema for show smartpower children '''

    schema = {
        Optional('interfaces'): {
            Any(): {
                Optional('interface'): str,
                Optional('role'): str,
                Optional('name'): str,
                Optional('usage'): str,
                Optional('category'): str,
                Optional('level'): str,
                Optional('imp'): str,
                Optional('type'): str,
            },
        },
        Optional('device_models'): {
            Any(): {
                Optional('usage'): str,
                Optional('role'): str,
                Optional('name'): str,
                Optional('category'): str,
                Optional('level'): str,
                Optional('imp'): str,
                Optional('type'): str,
            },
            Optional('consumer'): float,
            Optional('meter'): float,
            Optional('producer'): float,
            Optional('total'): float,
            Optional('count'): int,
        },
    }
    

# ==========================================
# Parser for:
#   * 'show smartpower children'
# ==========================================
class ShowSmartPowerChildren(ShowSmartPowerChildrenSchema):
    ''' Parser for show smartpower children '''

    cli_command = ['show smartpower children']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        ret_dict = {}

        # Gi1/0/3     IP Phone 9971     SEP08CC68E9DB8A       8.0   (W)  consumer  10    1    PoE
        # Gi1/0/11    interface         Gi1.0.11              10.7  (W)  consumer  10    1    PoE
        # Te3/0/2     AIR-AP1261N-A-K9  ap                    6.3   (W)  consumer  10    1    PoE
        # Gi2/0/3     interface         Gi2.0.3               NA    (W)  consumer  10    1    PoE
        p1 = re.compile(
            r'^(?P<interface>\S+\/\S+)\s+'
            r'(?P<role>(?:IP\s+Phone.*\d+|interface|AIR-[\w-]+))\s{2,}(?P<name>\S+)\s+'
            r'(?P<usage>[\d.]+|NA)\s+\(W\)\s+(?P<category>\w+)\s+(?P<level>\d+)\s+(?P<imp>\d+)\s+(?P<type>\w+)$'
        )

        # Subtotals: (Consumer: 371.5 (W), Meter: 0.0 (W), Producer: 0.0 (W))
        # Subtotals: (Consumer: 371.5 (W), Meter: 0.0 (W),
        p2 = re.compile(
            r'^Subtotals: \(Consumer: (?P<consumer>[\d.]+)\s+\(W\),\s+Meter: (?P<meter>[\d.]+)'
            r'(?:\s+\(W\),\s+Producer: (?P<producer>[\d.]+))?'
        )

        # Total: 371.5 (W), Count: 15
        p3 = re.compile(r'^Total: (?P<total>[\d.]+)\s+\(W\),\s+Count:\s*(?P<count>\d+)')

        # C9300-24P         Sust-PoE-3M-1         76.0  (W)  consumer  10    1    parent
        p4 = re.compile(
            r'^(?P<role>[\w][\w\-]*)\s+(?P<name>\S+)\s+'
            r'(?P<usage>[\d.]+)\s+\(W\)\s+(?P<category>\w+)\s+(?P<level>\d+)\s+(?P<imp>\d+)\s+(?P<type>\w+)$'
        )

        for line in output.splitlines():
            line = line.strip()

            if not line:
                continue

            # Gi1/0/3     IP Phone 9971     SEP08CC68E9DB8A       8.0   (W)  consumer  10    1    PoE
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group['interface'])
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})
                intf_dict.update({
                    'interface': intf,
                    'role': group['role'].strip(),
                    'name': group['name'],
                    'usage': group['usage'],
                    'category': group['category'],
                    'level': group['level'],
                    'imp': group['imp'],
                    'type': group['type'],
                })
                continue

            # Subtotals: (Consumer: 371.5 (W), Meter: 0.0 (W), Producer: 0.0 (W))
            m = p2.match(line)
            if m:
                group = m.groupdict()
                device_models_dict = ret_dict.setdefault('device_models', {})
                device_models_dict['consumer'] = float(group['consumer'])
                device_models_dict['meter'] = float(group['meter'])
                if group.get('producer'):
                    device_models_dict['producer'] = float(group['producer'])
                continue

            # Total: 371.5 (W), Count: 15
            m = p3.match(line)
            if m:
                group = m.groupdict()
                device_models_dict = ret_dict.setdefault('device_models', {})
                device_models_dict['total'] = float(group['total'])
                device_models_dict['count'] = int(group['count'])
                continue

            # C9300-24P         Sust-PoE-3M-1         76.0  (W)  consumer  10    1    parent
            m = p4.match(line)
            if m:
                group = m.groupdict()
                usage_key = group['usage']
                model_dict = ret_dict.setdefault('device_models', {}).setdefault(usage_key, {})
                model_dict.update({
                    'usage': group['usage'],
                    'name': group['name'],
                    'role': group['role'],
                    'category': group['category'],
                    'level': group['level'],
                    'imp': group['imp'],
                    'type': group['type'],
                })
                continue

        return ret_dict
