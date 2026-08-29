"""show_nslookup.py
    IOSXE parsers for the following show commands:
        * nslookup {domain}
        * nslookup {domain} {server_ip}
        * nslookup {auth_type} {domain} {server_ip}
        * nslookup {auth_type} {domain}
"""
#python
import re
import logging
logger = logging.getLogger(__name__)

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema,Any,Optional,ListOf

# ====================================================
# Schema for 'nslookup'
# ====================================================
class NslookupDomainSchema(MetaParser):
    """Schema for nslookup {domain}"""

    schema = {
        'server': str,
        'address': str,
        Optional('fqdn'): ListOf({
            'domain': str,
            'cname': str,
        }),
        Optional('name'): {
            Any(): {
                'addresses': ListOf(str)
            }
        }
    }

# ====================================================
# Parser for 'nslookup {domain}'
# ====================================================
class NslookupDomain(NslookupDomainSchema):
    """ Parser for 
        nslookup {domain}
        nslookup {domain} {server_ip}
        nslookup {auth_type} {domain} {server_ip}
        nslookup {auth_type} {domain}
    """

    cli_command = ["nslookup {domain}",
                    "nslookup {domain} {server_ip}",
                    "nslookup {auth_type} {domain} {server_ip}",
                    "nslookup {auth_type} {domain}",
                   ]

    def cli(self, domain, server_ip=None, auth_type=None, output=None):
        if output is None:
            if auth_type and server_ip:
                cmd = self.cli_command[2].format(auth_type=auth_type, domain=domain, server_ip=server_ip)
            elif auth_type:
                cmd = self.cli_command[3].format(auth_type=auth_type, domain=domain)
            elif server_ip:
                cmd = self.cli_command[1].format(domain=domain, server_ip=server_ip)
            else:
                cmd = self.cli_command[0].format(domain=domain)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Server:         64.104.128.236
        p1 = re.compile(r'^Server:\s+(?P<server>\S+)$')
        
        # Address:        64.104.128.236#53
        p2 = re.compile(r'^Address:\s+(?P<address>\S+)#\d+$')
        
        # www.cisco.com   canonical name = origin-www.cisco.com.
        p3 = re.compile(r'^(?P<domain>\S+)\s+canonical\s+name\s+=\s+(?P<cname>\S+)$')
        
        # Name:   origin-www.xgslb-v3.cisco.com
        p4 = re.compile(r'^Name:\s+(?P<name>\S+)$')
        
        # Address: 173.37.145.84 or Address: 2001:420:1201:2::a
        p5 = re.compile(r'^Address:\s+(?P<ip>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Server:         64.104.128.236
            m = p1.match(line)
            if m:
                ret_dict['server'] = m.groupdict()['server']
                continue

            # Address:        64.104.128.236#53
            m = p2.match(line)
            if m:
                ret_dict['address'] = m.groupdict()['address']
                continue

            # www.cisco.com   canonical name = origin-www.cisco.com.
            m = p3.match(line)
            if m:
                fqdn_dict = ret_dict.setdefault('fqdn', [])
                fqdn_dict.append({
                    'domain': m.groupdict()['domain'],
                    'cname': m.groupdict()['cname']
                })
                continue

            # Name:   origin-www.xgslb-v3.cisco.com
            m = p4.match(line)
            if m:
                current_fqdn = ret_dict.setdefault('name', {}).setdefault(m.groupdict()['name'], {})
                continue

            # Address: 171.68.194.101 or Address: 2001:420:1201:2::a
            m = p5.match(line)
            if m and current_fqdn is not None:
                current_fqdn.setdefault('addresses', []).append(m.groupdict()['ip'])
                continue

        return ret_dict