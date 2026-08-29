"""show_crypto.py

IOSXE parsers for the following show commands:
   * show crypto pki certificates <WORD>"""

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, ListOf

# Genie Libs
from genie.libs.parser.utils.common import Common

# =================================================
#  Schema for 'show crypto pki certificates <WORD>'
# =================================================
class ShowCryptoPkiCertificatesSchema(MetaParser):
    """Schema for show crypto pki certificates <WORD>"""
    schema = {
        'trustpoints':
            {Any():
                {'associated_trustpoints':
                    {Any():ListOf(
                        {'status': str,
                        'serial_number_in_hex': str,
                        'usage': str,
                        Optional('storage'): str,
                        'issuer':
                            {
                            Optional('cn'): str,
                            Optional('o'): str},
                        'subject':
                            {Optional('name'): str,
                            Optional('serial_number'): str,
                            Optional('pid'): str,
                            Optional('cn'): str,
                            Optional('o'): str,
                            },
                        Optional('crl_distribution_points'): str,
                        'validity_date':
                            {'start_date':str,
                            'end_date': str,
                            },
                        }),
                    },
                },
            },
        }

# =================================================
#  Parser for 'show crypto pki certificates <WORD>'
# =================================================
class ShowCryptoPkiCertificates(ShowCryptoPkiCertificatesSchema):
    """Parser for show crypto pki certificates <WORD>"""

    cli_command = ['show crypto pki certificates {trustpoint_name}','show crypto pki certificates']

    def cli(self, trustpoint_name='',output=None):
        if output is None:
            if trustpoint_name:
                cmd = self.cli_command[0].format(trustpoint_name=trustpoint_name)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        cer_dict = {}
        sub_dict = None
        trustpoints = None
        cer_type = None

        # initial regexp pattern
        # Certificate
        # CA Certificate
        p1 = re.compile(r'^((?P<cer>Certificate)|(?P<cer_name>(CA|Router Self-Signed) +Certificate))$')

        # Status: Available
        p2 = re.compile(r'^Status: +(?P<status>\w+)$')

        # Certificate Serial Number (hex): 793B572700000003750B
        # Certificate Serial Number: 0x15
        p3 = re.compile(r'^Certificate +Serial +Number( +\(hex\))?: +(?P<serial_number_in_hex>\w+)$')

        # Certificate Usage: General Purpose
        p4 = re.compile(r'^Certificate Usage: +(?P<usage>[\w\s]+)$')

        # Issuer:
        # Subject:
        # Validity Date:
        p5 = re.compile(r'^((?P<issuer>Issuer)|(?P<subject>Subject)|(?P<validity_date>Validity +Date)):$')

        # cn=Cisco Manufacturing CA SHA2
        # CN = tpca-root
        p6 = re.compile(r'(?i)^cn *= *(?P<cn>[\S\s]+)$')

        # o=Cisco
        # O = Company
        p7 = re.compile(r'(?i)^o *= *(?P<o>[\w\s]+)$')

        # Name: WS-C3850-24P-0057D21BC800
        p8 = re.compile(r'^Name: +(?P<name>.*)$')

        # Serial Number: PID:WS-C3850-24P SN:FCW1947C0GF
        p9 = re.compile(r'^Serial +Number: *'
                          r'PID: *(?P<pid>[\w\-]+) +'
                          r'SN: *(?P<serial_number>[\w\-]+)$')

        # CRL Distribution Points: 
        #     http://www.cisco.com/security/pki/crl/cmca2.crl
        p10 = re.compile(r'(?P<crl_distribution_points>^http:[\w\/\:\.]+)$')

        # start date: 00:34:52 UTC Nov 20 2015
        # end   date: 00:44:52 UTC Nov 20 2025
        p11 = re.compile(r'^((?P<start_date>start +date)|(?P<end_date>end +date)): +(?P<value>.*)$')

        # Associated Trustpoints: CISCO_IDEVID_SUDI
        # Associated Trustpoints: CISCO_IDEVID_SUDI Trustpool
        p12 = re.compile(r'^Associated +Trustpoints: +(?P<trustpoints>[\w\-]+)( +Trustpool)?$')

        # Storage: nvram:IOS-Self-Sig#1.cer
        p13 = re.compile(r'^Storage: +(?P<storage>(\S+))$')

        for line in out.splitlines():
            line = line.strip()
            
            # Certificate
            # CA Certificate
            m = p1.match(line)
            if m:
                if cer_dict and trustpoints:
                    trust = ret_dict.setdefault('trustpoints', {}).setdefault(trustpoints, {'associated_trustpoints': {}})
                    certs = trust['associated_trustpoints'].setdefault(cer_type, [])
                    certs.append(cer_dict)
                # New certificate starts
                cer_type = 'certificate' if m.groupdict()['cer'] else m.groupdict()['cer_name'].lower().replace(" ", "_").replace("-", "_")
                cer_dict = {}
                sub_dict = None
                trustpoints = None
                continue

            # Status: Available
            m = p2.match(line)
            if m:
                cer_dict['status'] = m.groupdict()['status']
                continue

            # Certificate Serial Number (hex): 793B572700000003750B
            # Certificate Serial Number: 0x15
            m = p3.match(line)
            if m:
                cer_dict['serial_number_in_hex'] = m.groupdict()['serial_number_in_hex']
                continue

            # Certificate Usage: General Purpose
            m = p4.match(line)
            if m:
                cer_dict['usage'] = m.groupdict()['usage']
                continue

            # Issuer:
            # Subject:
            # Validity Date:
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if group.get('issuer', {}):
                    sub_dict = cer_dict.setdefault('issuer', {})
                if group.get('subject', {}):
                    sub_dict = cer_dict.setdefault('subject', {})
                if group.get('validity_date', {}):
                    sub_dict = cer_dict.setdefault('validity_date', {})
                continue

            # cn=Cisco Manufacturing CA SHA2
            # CN = tpca-root
            m = p6.match(line)
            if m:
                sub_dict['cn'] = m.groupdict()['cn']
                continue
            
            # o=Cisco
            # O = Company
            m = p7.match(line)
            if m:
                sub_dict['o'] = m.groupdict()['o']
                continue

            # Name: WS-C3850-24P-0057D21BC800
            m = p8.match(line)
            if m:
                sub_dict['name'] = m.groupdict()['name']
                continue

            # Serial Number: PID:WS-C3850-24P SN:FCW1947C0GF
            m = p9.match(line)
            if m:
                sub_dict.update({k:v for k,v in m.groupdict().items()})
                continue
            
            # CRL Distribution Points: 
            #     http://www.cisco.com/security/pki/crl/cmca2.crl
            m = p10.match(line)
            if m:
                cer_dict['crl_distribution_points'] = m.groupdict()['crl_distribution_points']
                continue

            # start date: 00:34:52 UTC Nov 20 2015
            # end   date: 00:44:52 UTC Nov 20 2025
            m = p11.match(line)
            if m:
                group = m.groupdict()
                sub_dict.setdefault('start_date', group['value']) if \
                    group.get('start_date', {}) else None
                sub_dict.setdefault('end_date', group['value']) if \
                    group.get('end_date', {}) else None
                continue

            # Storage: nvram:IOS-Self-Sig#1.cer
            m = p13.match(line)
            if m:
                cer_dict['storage'] = m.groupdict()['storage']
                continue

            # Associated Trustpoints: CISCO_IDEVID_SUDI
            # Associated Trustpoints: CISCO_IDEVID_SUDI Trustpool
            m = p12.match(line)
            if m:
                trustpoints = m.groupdict()['trustpoints'] 
                continue
        if cer_dict and trustpoints:
            trust = ret_dict.setdefault('trustpoints', {}).setdefault(trustpoints, {'associated_trustpoints': {}})
            certs = trust['associated_trustpoints'].setdefault(cer_type, [])
            certs.append(cer_dict)

        return ret_dict


class ShowCryptoIkev2StatsExchangeSchema(MetaParser):
    """Schema for show crypto ikev2 stats exchange"""
    schema = {
        "exchanges": {
            Any(): {
                "tx_req": int,
                "tx_res": int,
                "rx_req": int,
                "rx_res": int,
                Optional("rtx_req"): int,
                Optional("rtx_res"): int,
                Optional("rrx_req"): int,
                Optional("rrx_res"): int,
            }
        },
        Optional("error_notify"): {
            Any(): {
                "tx_req": int,
                "tx_res": int,
                "rx_req": int,
                "rx_res": int,
                Optional("rtx_req"): int,
                Optional("rtx_res"): int,
                Optional("rrx_req"): int,
                Optional("rrx_res"): int,
            }
        },
        Optional("other_notify"): {
            Any(): {
                "tx_req": int,
                "tx_res": int,
                "rx_req": int,
                "rx_res": int,
                Optional("rtx_req"): int,
                Optional("rtx_res"): int,
                Optional("rrx_req"): int,
                Optional("rrx_res"): int,
            }
        },
        Optional("config_payload_type"): {
            Any(): {
                "tx": int,
                "rx": int,
                Optional("rtx"): int,
                Optional("rrx"): int,
            }
        },
        Optional("other_counters"): {
            Any(): {
                "tx": int,
                Optional("rtx"): int,
            }
        },
    }


class ShowCryptoIkev2StatsExchange(ShowCryptoIkev2StatsExchangeSchema):
    """Parser for show crypto ikev2 stats exchange"""

    cli_command = "show crypto ikev2 stats exchange"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        current_section = None

        # EXCHANGES
        p1 = re.compile(r'^EXCHANGES$')

        # ERROR NOTIFY
        p2 = re.compile(r'^ERROR NOTIFY$')

        # OTHER NOTIFY
        p3 = re.compile(r'^OTHER NOTIFY$')

        # IKE_SA_INIT          8     11     11      8   [  0    0    0    0 ]
        # New (8 cols) and old (4 cols) both supported.
        p4 = re.compile(
            r'^(?P<name>[A-Z0-9_]+)\s+'
            r'(?P<tx_req>\d+)\s+(?P<tx_res>\d+)\s+'
            r'(?P<rx_req>\d+)\s+(?P<rx_res>\d+)'
            r'(?:\s+(?P<rtx_req>\d+)\s+(?P<rtx_res>\d+)'
            r'\s+(?P<rrx_req>\d+)\s+(?P<rrx_res>\d+))?$'
        )

        # CONFIG PAYLOAD TYPE     TX     RX  [ RTX    RRX ]
        p5 = re.compile(
            r'^CONFIG PAYLOAD TYPE(?:\s+TX\s+RX(?:\s+RTX\s+RRX)?)?$'
        )

        # CFG_REQUEST   8   11  [ 0   0 ]    -> new (4 ints) or old (2 ints)
        p6 = re.compile(
            r'^(?P<name>[A-Z0-9_]+)\s+(?P<tx>\d+)\s+(?P<rx>\d+)'
            r'(?:\s+(?P<rtx>\d+)\s+(?P<rrx>\d+))?$'
        )

        # OTHER COUNTERS  [ TX  [ RTX ] ]
        p7 = re.compile(r'^OTHER COUNTERS(?:\s+TX(?:\s+RTX)?)?$')

        # NO_NAT    19   [ 0 ]    -> new (2 ints) or old (1 int)
        p8 = re.compile(
            r'^(?P<name>[A-Z0-9_]+)\s+(?P<tx>\d+)(?:\s+(?P<rtx>\d+))?$'
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # EXCHANGES
            if p1.match(line):
                current_section = "exchanges"
                ret_dict.setdefault("exchanges", {})
                continue

            # ERROR NOTIFY
            if p2.match(line):
                current_section = "error_notify"
                ret_dict.setdefault("error_notify", {})
                continue

            # OTHER NOTIFY
            if p3.match(line):
                current_section = "other_notify"
                ret_dict.setdefault("other_notify", {})
                continue

            # CONFIG PAYLOAD TYPE header (with or without RTX/RRX columns)
            if p5.match(line):
                current_section = "config_payload_type"
                ret_dict.setdefault("config_payload_type", {})
                continue

            # OTHER COUNTERS header (with or without TX/RTX columns)
            if p7.match(line):
                current_section = "other_counters"
                ret_dict.setdefault("other_counters", {})
                continue

            # Exchange / notify rows
            if current_section in ("exchanges", "error_notify", "other_notify"):
                m = p4.match(line)
                if m:
                    group = m.groupdict()
                    name = group.pop("name")
                    target = ret_dict.setdefault(current_section, {}).setdefault(name, {})
                    target["tx_req"] = int(group["tx_req"])
                    target["tx_res"] = int(group["tx_res"])
                    target["rx_req"] = int(group["rx_req"])
                    target["rx_res"] = int(group["rx_res"])
                    if group.get("rtx_req") is not None:
                        target["rtx_req"] = int(group["rtx_req"])
                        target["rtx_res"] = int(group["rtx_res"])
                        target["rrx_req"] = int(group["rrx_req"])
                        target["rrx_res"] = int(group["rrx_res"])
                    continue

            # CONFIG PAYLOAD TYPE rows
            if current_section == "config_payload_type":
                m = p6.match(line)
                if m:
                    group = m.groupdict()
                    name = group.pop("name")
                    entry = ret_dict.setdefault("config_payload_type", {}).setdefault(name, {})
                    entry["tx"] = int(group["tx"])
                    entry["rx"] = int(group["rx"])
                    if group.get("rtx") is not None:
                        entry["rtx"] = int(group["rtx"])
                        entry["rrx"] = int(group["rrx"])
                    continue

            # OTHER COUNTERS rows
            if current_section == "other_counters":
                m = p8.match(line)
                if m:
                    group = m.groupdict()
                    name = group.pop("name")
                    entry = ret_dict.setdefault("other_counters", {}).setdefault(name, {})
                    entry["tx"] = int(group["tx"])
                    if group.get("rtx") is not None:
                        entry["rtx"] = int(group["rtx"])
                    continue

        return ret_dict
