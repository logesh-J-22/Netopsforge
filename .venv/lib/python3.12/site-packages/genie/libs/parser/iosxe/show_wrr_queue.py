""" show_wrr_queue.py
IOSXE parsers for the following show commands:
    *  'show wrr-queue bandwidth'
    *  'show wrr-queue cos-map'
"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowWrrQueueBandwidthSchema(MetaParser):
    """
    Schema for show wrr-queue bandwidth

    Example outputs:
    Example1:
        wrr-queue bandwidth for Etherswitch NGWIC is:
        WRR Queue  :   1   2   3   4   5   6   7   8
        Bandwidth  :   1   2   3   6  12  17  25  33
    Example2:
        wrr-queue bandwidth is disabled
    """
    schema = {
        'enabled': bool,
        Optional('interface_type'): str,
        Optional('queues'): {
            Any(): {
                'bandwidth': int
            }
        }
    }


class ShowWrrQueueBandwidth(ShowWrrQueueBandwidthSchema):
    """Parser for show wrr-queue bandwidth"""

    cli_command = 'show wrr-queue bandwidth'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # wrr-queue bandwidth for Etherswitch NGWIC is:
        # wrr-queue bandwidth is disabled
        p1 = re.compile(
            r'^wrr-queue +bandwidth'
            r'(?: +for +(?P<interface_type>.+?) +is\s*:|'
            r' +(?P<disabled>is +disabled))'
        )

        # WRR Queue  :   1   2   3   4   5   6   7   8
        p2 = re.compile(r'^WRR +Queue\s*:\s*(?P<queues>[\d\s]+)$')

        # Bandwidth  :   1   2   3   6  12  17  25  33
        p3 = re.compile(r'^Bandwidth\s*:\s*(?P<bandwidths>[\d\s]+)$')

        queue_numbers = []

        for line in out.splitlines():
            line = line.strip()

            # wrr-queue bandwidth for Etherswitch NGWIC is:
            # wrr-queue bandwidth is disabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group.get('disabled'):
                    ret_dict['enabled'] = False
                else:
                    ret_dict['enabled'] = True
                    if group.get('interface_type'):
                        ret_dict['interface_type'] = group['interface_type']
                continue

            # WRR Queue  :   1   2   3   4   5   6   7   8
            m = p2.match(line)
            if m:
                queue_numbers = [int(q) for q in m.group('queues').split()]
                continue

            # Bandwidth  :   1   2   3   6  12  17  25  33
            m = p3.match(line)
            if m and queue_numbers:
                bandwidths = [int(b) for b in m.group('bandwidths').split()]
                queues_dict = ret_dict.setdefault('queues', {})
                for q, bw in zip(queue_numbers, bandwidths):
                    queues_dict[q] = {'bandwidth': bw}
                continue

        return ret_dict


class ShowWrrQueueCosMapSchema(MetaParser):
    """
    Schema for show wrr-queue cos-map

    Example output:
        wrr-queue cos map for Etherswitch NGWIC is
        CoS Value      :  0  1  2  3  4  5  6  7
        Priority Queue :  1  5  3  4  5  6  7  8
    """

    schema = {
        Optional('interface_type'): str,
        'cos_map': {
            Any(): {
                'priority_queue': int
            }
        }
    }


class ShowWrrQueueCosMap(ShowWrrQueueCosMapSchema):
    """Parser for show wrr-queue cos-map"""

    cli_command = 'show wrr-queue cos-map'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # wrr-queue cos map for Etherswitch NGWIC is
        p1 = re.compile(
            r'^wrr-queue +cos +map +for +(?P<interface_type>.+?) +is$'
        )

        # CoS Value      :  0  1  2  3  4  5  6  7
        p2 = re.compile(r'^CoS +Value\s*:\s*(?P<cos_values>[\d\s]+)$')

        # Priority Queue :  1  5  3  4  5  6  7  8
        p3 = re.compile(
            r'^Priority +Queue\s*:\s*(?P<priority_queues>[\d\s]+)$')

        cos_values = []

        for line in out.splitlines():
            line = line.strip()

            # wrr-queue cos map for Etherswitch NGWIC is
            m = p1.match(line)
            if m:
                ret_dict['interface_type'] = m.groupdict()['interface_type']
                continue

            # CoS Value      :  0  1  2  3  4  5  6  7
            m = p2.match(line)
            if m:
                cos_values = [int(c) for c in m.group('cos_values').split()]
                continue

            # Priority Queue :  1  5  3  4  5  6  7  8
            m = p3.match(line)
            if m and cos_values:
                priority_queues = [
                    int(p) for p in m.group('priority_queues').split()]
                cos_map = ret_dict.setdefault('cos_map', {})
                for cos, queue in zip(cos_values, priority_queues):
                    cos_map[cos] = {'priority_queue': queue}

        return ret_dict
