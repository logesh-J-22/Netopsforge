''' show_license.py

IOSXE parsers for the following show commands:
   
    * show license usage
    

'''

#Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common


# ======================================
#  Schema for: 'show license usage'   
# ======================================

class ShowLicenseUsageSchema(MetaParser):
    schema = {
        'license_name': {
            Any(): {
                Optional('description'): str,
                Optional('count'): int,
                Optional('version'): str,
                Optional('status'): str,
                Optional('export_status'): str,
                Optional('feature_name'): str,
                Optional('feature_description'): str,
                Optional('enforcement_type'): str,
                Optional('license_type'): str,
            }
        },
        Optional('license_authorization'): {
            Optional('status'): str
        }
    }

# ======================================
#  Parser for: 'show license usage'   
# ======================================

class ShowLicenseUsage(ShowLicenseUsageSchema):
    """ Parser for show license usage """
    cli_command = 'show license usage'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}

        # Patterns
        # Example: dna-advantage (C9500X_DNA_A):
        p1 = re.compile(r'^.*\(.*:+(?P<license_name>.*)$')
        # Example: Status: IN USE
        p2 = re.compile(r'^Status: +(?P<status>.*)$')
        # Example: Description: DNA Advantage License for Catalyst 9500X Switches
        p3 = re.compile(r'^Description: +(?P<description>.*)$')
        # Example: Count: 2
        p4 = re.compile(r'^Count: +(?P<count>\d+)$')
        # Example: Version: 1.0
        p5 = re.compile(r'^Version: +(?P<version>.*)$')
        # Example: Export status: NOT RESTRICTED
        p6 = re.compile(r'^Export +status: +(?P<export_status>.*)$')
        # Example: Feature Name: dna-advantage
        p7 = re.compile(r'^Feature +Name: +(?P<feature_name>.*)$')
        # Example: Feature Description: DNA Advantage License for Catalyst 9500X Switches
        p8 = re.compile(r'^Feature +Description: +(?P<feature_description>.*)$')
        # Example: Enforcement type: NOT ENFORCED
        p9 = re.compile(r'^Enforcement +type: +(?P<enforcement_type>.*)$')
        # Example: License type: Subscription
        p10 = re.compile(r'^License +type: +(?P<license_type>.*)$')

        license_name_dict = None
        current_license = None

        for line in output.splitlines():
            line = line.strip()

            # (C9300-24 Network Advantage):
            m = p1.match(line)
            if m:
                current_license = m.group()
                license_name_dict = ret_dict.setdefault('license_name', {}).setdefault(current_license, {})
                continue

            # Status: Not Applicable
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if license_name_dict is not None:
                    license_name_dict.setdefault('status', group['status'])
                else:
                    ret_dict.setdefault('license_authorization', {}).setdefault('status', group['status'])
                continue

            # Description: ...
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if license_name_dict is not None:
                    license_name_dict.setdefault('description', group['description'])
                continue

            # Count: ...
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group['count'] = int(group['count'])
                if license_name_dict is not None:
                    license_name_dict.setdefault('count', group['count'])
                continue

            # Version: ...
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if license_name_dict is not None:
                    license_name_dict.setdefault('version', group['version'])
                continue

            # Export status: ...
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if license_name_dict is not None:
                    license_name_dict.setdefault('export_status', group['export_status'])
                continue

            # Feature Name: ...
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if license_name_dict is not None:
                    license_name_dict.setdefault('feature_name', group['feature_name'])
                continue

            # Feature Description: ...
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if license_name_dict is not None:
                    license_name_dict.setdefault('feature_description', group['feature_description'])
                continue

            # Enforcement type: ...
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if license_name_dict is not None:
                    license_name_dict.setdefault('enforcement_type', group['enforcement_type'])
                continue

            # License type: ...
            m = p10.match(line)
            if m:
                group = m.groupdict()
                if license_name_dict is not None:
                    license_name_dict.setdefault('license_type', group['license_type'])
                continue

        return ret_dict
