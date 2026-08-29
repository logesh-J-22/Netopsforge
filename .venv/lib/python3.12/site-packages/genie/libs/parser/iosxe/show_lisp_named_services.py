"""show_lisp_named_services.py

    * show lisp {lisp_id} instance-id {instance_id} named-services map-cache
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services map-cache
    * show lisp instance-id {instance_id} named-services map-cache
    * show lisp {lisp_id} instance-id {instance_id} named-services map-cache {eid_prefix}
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services map-cache {eid_prefix}
    * show lisp instance-id {instance_id} named-services map-cache {eid_prefix}
    * show lisp instance-id {instance_id} named-services server
    * show lisp {lisp_id} instance-id {instance_id} named-services server
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services server
    * show lisp instance-id {instance_id} named-services server detail
    * show lisp instance-id {instance_id} named-services server name {site_name}
    * show lisp instance-id {instance_id} named-services server {eid}
    * show lisp instance-id {instance_id} named-services server etr-address {etr_address}
    * show lisp {lisp_id} instance-id {instance_id} named-services server detail
    * show lisp {lisp_id} instance-id {instance_id} named-services server name {site_name}
    * show lisp {lisp_id} instance-id {instance_id} named-services server {eid}
    * show lisp {lisp_id} instance-id {instance_id} named-services server etr-address {etr_address}
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services server detail
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services server name {site_name}
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services server {eid}
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services server etr-address {etr_address}
    * show lisp instance-id {instance_id} named-services publication
    * show lisp {lisp_id} instance-id {instance_id} named-services publication
    * show lisp locator-table {vrf} instance-id {instance_id} named-services publication
    * show lisp instance-id {instance_id} named-services publication {eid_prefix}
    * show lisp {lisp_id} instance-id {instance_id} named-services publication {eid_prefix}
    * show lisp locator-table {vrf} instance-id {instance_id} named-services publication {eid_prefix}
    * show lisp locator-table vrf {vrf} instance-id {instance_id} named-services publication {eid_prefix}
    * show lisp {lisp_id} instance-id {instance_id} named-services subscription
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription
    * show lisp instance-id {instance_id} named-services subscription
    * show lisp instance-id {instance_id} named-services subscription {eid_prefix}
    * show lisp {lisp_id} instance-id {instance_id} named-services subscription {eid_prefix}
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription {eid_prefix}
    * show lisp instance-id {instance_id} named-services subscription detail
    * show lisp {lisp_id} instance-id {instance_id} named-services subscription detail
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription detail
    * show lisp {lisp_id} instance-id {instance_id} named-services server subscription
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription
    * show lisp instance-id {instance_id} named-services server subscription
    * show lisp instance-id {instance_id} named-services server subscription {eid_prefix}
    * show lisp {lisp_id} instance-id {instance_id} named-services server subscription {eid_prefix}
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription {eid_prefix}
    * show lisp instance-id {instance_id} named-services server subscription detail
    * show lisp {lisp_id} instance-id {instance_id} named-services server subscription detail
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription detail
    * show lisp {lisp_id} instance-id {instance_id} named-services subscriber
    * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscriber
    * show lisp instance-id {instance_id} named-services subscriber
    * show lisp {lisp_id} instance-id {instance_id} named-services publisher
    * show lisp locator-table {vrf} instance-id {instance_id} named-services publisher
    * show lisp instance-id {instance_id} named-services publisher
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional

from genie.libs.parser.iosxe.show_lisp_super import (
    ShowLispIpMapCachePrefixSuperParser,
    ShowLispIpv4PublicationSchema,
    ShowLispMapCacheSuperParser,
    ShowLispPublicationPrefixSuperParser,
    ShowLispPublisherSchema,
    ShowLispPublisherSuperParser,
    ShowLispServerSubscriptionPrefixSchema,
    ShowLispServerSubscriptionPrefixSuperParser,
    ShowLispServerSubscriptionSchema,
    ShowLispServerSubscriptionSuperParser,
    ShowLispSiteDetailSuperParser,
    ShowLispSiteSuperParser,
    ShowLispSubscriberSchema,
    ShowLispSubscriberSuperParser,
    ShowLispSubscriptionSchema,
    ShowLispSubscriptionSuperParser,
)

# Import parsers from show_lisp
from genie.libs.parser.iosxe.show_lisp import (
    ShowLispAFSubscriptionPrefix,
)


# ========================================================================
# Parser for 'show lisp instance-id <instance_id> named-services map-cache'
# ========================================================================
class ShowLispNamedServicesMapCache(ShowLispMapCacheSuperParser):
    """Parser for:
        * show lisp {lisp_id} instance-id {instance_id} named-services map-cache
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services map-cache
        * show lisp instance-id {instance_id} named-services map-cache
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} named-services map-cache',
        'show lisp locator-table {locator_table} instance-id {instance_id} named-services map-cache',
        'show lisp instance-id {instance_id} named-services map-cache'
    ]

    def cli(self, command=None, output=None, lisp_id=None, locator_table=None,
            instance_id=None, **kwargs):
        if output is None:
            output = self.device.execute(command)

        return super().cli(output=output)


# ========================================================================
# Schema for 'show lisp instance-id <instance_id> named-services map-cache <eid_prefix>'
# ========================================================================
class ShowLispNamedServicesMapCachePrefixSchema(MetaParser):
    """Schema for named-services map-cache prefix commands."""

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_table': str,
                        'entries': int,
                        'eid_prefix': str,
                        'uptime': str,
                        'expires': str,
                        'via': str,
                        Optional('site'): str,
                        'sources': str,
                        'state': str,
                        'last_modified': str,
                        'map_source': str,
                        Optional('activity'): str,
                        Optional('packets_out'): int,
                        Optional('packets_out_bytes'): int,
                        Optional('encap'): str,
                        'locators': {
                            str: {
                                'uptime': str,
                                'state': str,
                                'priority': int,
                                'weight': int,
                                'encap_iid': str,
                                Optional('state_change_time'): str,
                                Optional('state_change_count'): int,
                                Optional('route_reachability_change_time'): str,
                                Optional('route_reachability_change_count'): int,
                                Optional('priority_change'): str,
                                Optional('weight_change'): str,
                                Optional('rloc_probe_sent'): str
                            }
                        }
                    }
                }
            }
        }
    }


# ========================================================================
# Parser for 'show lisp instance-id <instance_id> named-services map-cache <eid_prefix>'
# ========================================================================
class ShowLispNamedServicesMapCachePrefix(
        ShowLispNamedServicesMapCachePrefixSchema,
        ShowLispIpMapCachePrefixSuperParser):
    """Parser for:
        * show lisp {lisp_id} instance-id {instance_id} named-services map-cache {eid_prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services map-cache {eid_prefix}
        * show lisp instance-id {instance_id} named-services map-cache {eid_prefix}
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} named-services map-cache {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} named-services map-cache {eid_prefix}',
        'show lisp instance-id {instance_id} named-services map-cache {eid_prefix}'
    ]

    def cli(self, command=None, output=None, lisp_id=None, instance_id=None,
            eid_prefix=None, locator_table=None, **kwargs):
        if output is None:
            output = self.device.execute(command)

        return super().cli(eid_prefix, output=output, lisp_id=lisp_id,
                           instance_id=instance_id, locator_table=locator_table)


# =============================================================================
# Parser for 'show lisp instance-id <instance_id> named-services server'
# =============================================================================
class ShowLispNamedServicesServer(ShowLispSiteSuperParser):
    """ Parser for:
        * show lisp instance-id {instance_id} named-services server
        * show lisp {lisp_id} instance-id {instance_id} named-services server
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services server
    """

    cli_command = ['show lisp instance-id {instance_id} named-services server',
                   'show lisp {lisp_id} instance-id {instance_id} named-services server',
                   'show lisp locator-table {locator_table} instance-id {instance_id} named-services server']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vrf=None,
            locator_table=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].
                                             format(lisp_id=lisp_id,
                                                    instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].
                                             format(locator_table=locator_table,
                                                    instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].
                                             format(instance_id=instance_id))
        return super().cli(lisp_id=lisp_id, instance_id=instance_id, output=output)


# =============================================================================
# Parser for 'show lisp instance-id <instance_id> named-services server detail'
# =============================================================================
class ShowLispNamedServicesServerDetail(ShowLispSiteDetailSuperParser):
    """Parser for show lisp named-services server detail

    Inherits from ShowLispSiteDetailSuperParser
    Follows ShowLispEthernetServerDetail pattern
    """
    cli_command = ['show lisp instance-id {instance_id} named-services server detail',
                   'show lisp instance-id {instance_id} named-services server name {site_name}',
                   'show lisp instance-id {instance_id} named-services server {eid}',
                   'show lisp instance-id {instance_id} named-services server etr-address {etr_address}',
                   'show lisp {lisp_id} instance-id {instance_id} named-services server detail',
                   'show lisp {lisp_id} instance-id {instance_id} named-services server name {site_name}',
                   'show lisp {lisp_id} instance-id {instance_id} named-services server {eid}',
                   'show lisp {lisp_id} instance-id {instance_id} named-services server etr-address {etr_address}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} named-services server detail',
                   'show lisp locator-table {locator_table} instance-id {instance_id} named-services server name {site_name}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} named-services server {eid}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} named-services server etr-address {etr_address}']

    def cli(self, output=None, lisp_id=None, eid=None, instance_id=None,
            eid_table=None, vrf=None, locator_table=None, site_name=None,
            etr_address=None):

        if output is None:
            if locator_table and instance_id and site_name:
                output = self.device.execute(self.cli_command[9].
                                             format(locator_table=locator_table,
                                                    instance_id=instance_id,
                                                    site_name=site_name))
            elif locator_table and instance_id and eid:
                output = self.device.execute(self.cli_command[10].
                                             format(locator_table=locator_table,
                                                    instance_id=instance_id,
                                                    eid=eid))
            elif locator_table and instance_id and etr_address:
                output = self.device.execute(self.cli_command[11].
                                             format(locator_table=locator_table,
                                                    instance_id=instance_id,
                                                    etr_address=etr_address))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[8].
                                             format(locator_table=locator_table,
                                                    instance_id=instance_id))
            elif lisp_id and instance_id and site_name:
                output = self.device.execute(self.cli_command[5].
                                             format(lisp_id=lisp_id,
                                                    instance_id=instance_id,
                                                    site_name=site_name))
            elif lisp_id and instance_id and eid:
                output = self.device.execute(self.cli_command[6].
                                             format(lisp_id=lisp_id,
                                                    instance_id=instance_id,
                                                    eid=eid))
            elif lisp_id and instance_id and etr_address:
                output = self.device.execute(self.cli_command[7].
                                             format(lisp_id=lisp_id,
                                                    instance_id=instance_id,
                                                    etr_address=etr_address))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[4].
                                             format(lisp_id=lisp_id,
                                                    instance_id=instance_id))
            elif etr_address and instance_id:
                output = self.device.execute(self.cli_command[3].
                                             format(etr_address=etr_address,
                                                    instance_id=instance_id))
            elif eid and instance_id:
                output = self.device.execute(self.cli_command[2].
                                             format(eid=eid,
                                                    instance_id=instance_id))
            elif site_name and instance_id:
                output = self.device.execute(self.cli_command[1].
                                             format(site_name=site_name,
                                                    instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].
                                             format(instance_id=instance_id))

        return super().cli(output=output)


# =============================================================================
# Parser for 'show lisp instance-id <instance_id> named-services publication'
# =============================================================================
class ShowLispNamedServicesPublication(ShowLispIpv4PublicationSchema):
    """Parser for show lisp named-services publication

    Inherits from ShowLispIpv4PublicationSchema (list view)
    Based on ShowLispEthernetPublication with DN-specific regex
    """
    cli_command = ['show lisp instance-id {instance_id} named-services publication',
                   'show lisp {lisp_id} instance-id {instance_id} named-services publication',
                   'show lisp locator-table {vrf} instance-id {instance_id} named-services publication']

    def cli(self, lisp_id=None, instance_id=None, vrf=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id)
            elif vrf and instance_id:
                cmd = self.cli_command[2].format(vrf=vrf, instance_id=instance_id)
            else:
                cmd = self.cli_command[0].format(instance_id=instance_id)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Publication Information for LISP 0 EID-table N/A (IID 4)
        p0 = re.compile(r"^Publication\s+Information\s+for\s+LISP\s+"
                        r"(?P<lisp_id>\d+)\s+EID-table\s+(?P<eid_table>\S+)\s+"
                        r"\(IID\s+(?P<instance_id>\d+)\)$")

        # Output for router lisp 0 instance-id 101
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)\s+"
                        r"instance-id\s+(?P<instance_id>\d+)$")

        # Entries total 2
        p2 = re.compile(r"^Entries\s+total\s+(?P<total_entries>\d+)$")

        # DN format: firewall   2d07h   100.55.55.55   -
        # Old format with RLOC: 100.100.100.100 15:52:51  firewall  11.11.11.11  -
        # DN string without dots or colons
        p3 = re.compile(r"^(?P<publisher_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                        r"(?P<last_published>\S+)\s+(?P<eid_prefix>[^\s\.\:,]+)\s+"
                        r"(?P<rloc>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                        r"(?P<encap_iid>\S+)$")

        # New format (Locators are no longer displayed): firewall  2d07h  100.55.55.55  -
        # DN string without dots or colons
        p4 = re.compile(r"^(?P<eid_prefix>[^\s\.\:,]+)\s+(?P<last_published>\S+)\s+"
                        r"(?P<publisher_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                        r"(?P<encap_iid>\S+)$")
        count = 0

        for line in output.splitlines():
            line = line.strip()
            count += 1

            # Publication Information for LISP 0 EID-table N/A (IID 4)
            m = p0.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                continue

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})

            if not m and count < 2 and lisp_id != "all":
                if lisp_id and instance_id:
                    lisp_id = int(lisp_id)
                    lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                    count += 1
                    continue
                if not lisp_id and instance_id:
                    lisp_id = 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                    count += 1
                    continue

            # Entries total 2
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                entries = int(groups['total_entries'])
                instance_id_dict.update({'total_entries': entries})
                continue

            # Old format with RLOC: 100.100.100.100 15:52:51  firewall  11.11.11.11  -
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                publications = groups['eid_prefix']
                publisher_ip = groups['publisher_ip']
                last_published = groups['last_published']
                rloc = groups['rloc']
                encap_iid = groups['encap_iid']
                eid_prefix = instance_id_dict.setdefault('eid_prefix', {}).setdefault(publications, {})
                eid_prefix.update({'publisher_ip': publisher_ip})
                eid_prefix.update({'last_published': last_published})
                eid_prefix.update({'rloc': rloc})
                eid_prefix.update({'encap_iid': encap_iid})
                continue

            # New format (Locators are no longer displayed): firewall  2d07h  100.55.55.55  -
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                publications = groups['eid_prefix']
                publisher_ip = groups['publisher_ip']
                last_published = groups['last_published']
                encap_iid = groups['encap_iid']
                eid_prefix = instance_id_dict.setdefault('eid_prefix', {}).setdefault(publications, {})
                eid_prefix.update({'publisher_ip': publisher_ip})
                eid_prefix.update({'last_published': last_published})
                eid_prefix.update({'encap_iid': encap_iid})
                continue

        return ret_dict


# =============================================================================
# Parser for 'show lisp instance-id <instance_id> named-services publication {eid_prefix}'
# =============================================================================
class ShowLispNamedServicesPublicationPrefix(ShowLispPublicationPrefixSuperParser):
    """Parser for show lisp named-services publication {eid_prefix}

    Inherits from ShowLispPublicationPrefixSuperParser
    Super parser now supports DN strings in addition to IPv4/IPv6 prefixes
    """
    cli_command = ['show lisp instance-id {instance_id} named-services publication {eid_prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} named-services publication {eid_prefix}',
                   'show lisp locator-table {vrf} instance-id {instance_id} named-services publication {eid_prefix}',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} named-services publication {eid_prefix}']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, eid_prefix=None, vrf=None, output=None):
        if output is None:
            if lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif vrf and instance_id and eid_prefix:
                if "vrf" in self.cli_command[3]:
                    output = self.device.execute(self.cli_command[3].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
                else:
                    output = self.device.execute(self.cli_command[2].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id, eid_prefix=eid_prefix))

        return super().cli(lisp_id=lisp_id, instance_id=instance_id, eid_table=eid_table,
                          eid_prefix=eid_prefix, vrf=vrf, output=output)


# =========================================================================
# Parser for 'show lisp instance-id <instance_id> named-services subscription'
# =========================================================================
class ShowLispNamedServicesSubscription(ShowLispSubscriptionSuperParser, ShowLispSubscriptionSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} named-services subscription
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription
        * show lisp instance-id {instance_id} named-services subscription
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} named-services subscription',
        'show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription',
        'show lisp instance-id {instance_id} named-services subscription'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, locator_table=None,
            eid_table=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[1].
                                             format(locator_table=locator_table, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


# =========================================================================
# Parser for 'show lisp instance-id <instance_id> named-services subscription <prefix>'
# =========================================================================
class ShowLispNamedServicesSubscriptionPrefix(ShowLispAFSubscriptionPrefix):
    """ Parser for:
        * show lisp instance-id {instance_id} named-services subscription {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} named-services subscription {eid_prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription {eid_prefix}
        * show lisp instance-id {instance_id} named-services subscription detail
        * show lisp {lisp_id} instance-id {instance_id} named-services subscription detail
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription detail
    """

    cli_command = [
        'show lisp instance-id {instance_id} named-services subscription {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} named-services subscription {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription {eid_prefix}',
        'show lisp instance-id {instance_id} named-services subscription detail',
        'show lisp {lisp_id} instance-id {instance_id} named-services subscription detail',
        'show lisp locator-table {locator_table} instance-id {instance_id} named-services subscription detail'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, locator_table=None,
            eid=None, eid_prefix=None):
        if output is None:
            if lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[1].
                                                format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[0].
                                                format(instance_id=instance_id, eid_prefix=eid_prefix))
            elif locator_table and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[2].
                                                format(locator_table=locator_table, instance_id=instance_id, eid_prefix=eid_prefix))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[4].
                                                format(lisp_id=lisp_id, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[3].
                                                format(instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[5].
                                                format(locator_table=locator_table, instance_id=instance_id))

        return super().cli(output=output)


# =========================================================================
# Parser for 'show lisp instance-id <instance_id> named-services server subscription'
# =========================================================================
class ShowLispNamedServicesServerSubscription(ShowLispServerSubscriptionSuperParser, ShowLispServerSubscriptionSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} named-services server subscription
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription
        * show lisp instance-id {instance_id} named-services server subscription
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} named-services server subscription',
        'show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription',
        'show lisp instance-id {instance_id} named-services server subscription'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, locator_table=None,
            eid_table=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[1].
                                             format(locator_table=locator_table, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))

        return super().cli(output=output)


# =========================================================================
# Parser for 'show lisp instance-id <instance_id> named-services server subscription <prefix>'
# =========================================================================
class ShowLispNamedServicesServerSubscriptionPrefix(ShowLispServerSubscriptionPrefixSuperParser, ShowLispServerSubscriptionPrefixSchema):
    """ Parser for:
        * show lisp instance-id {instance_id} named-services server subscription {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} named-services server subscription {eid_prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription {eid_prefix}
        * show lisp instance-id {instance_id} named-services server subscription detail
        * show lisp {lisp_id} instance-id {instance_id} named-services server subscription detail
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription detail
    """

    cli_command = [
        'show lisp instance-id {instance_id} named-services server subscription {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} named-services server subscription {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription {eid_prefix}',
        'show lisp instance-id {instance_id} named-services server subscription detail',
        'show lisp {lisp_id} instance-id {instance_id} named-services server subscription detail',
        'show lisp locator-table {locator_table} instance-id {instance_id} named-services server subscription detail'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, locator_table=None,
            eid_table=None, eid_prefix=None):
        if output is None:
            if lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[1].
                                             format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif locator_table and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[2].
                                             format(locator_table=locator_table, instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[0].
                                             format(instance_id=instance_id, eid_prefix=eid_prefix))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[4].
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[5].
                                             format(locator_table=locator_table, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[3].
                                             format(instance_id=instance_id))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)



# =========================================================================
# Parser for 'show lisp instance-id <instance_id> named-services subscriber'
# =========================================================================
class ShowLispNamedServicesSubscriber(ShowLispSubscriberSuperParser, ShowLispSubscriberSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} named-services subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} named-services subscriber
        * show lisp instance-id {instance_id} named-services subscriber
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} named-services subscriber',
        'show lisp locator-table {locator_table} instance-id {instance_id} named-services subscriber',
        'show lisp instance-id {instance_id} named-services subscriber'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, locator_table=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[1].
                                             format(locator_table=locator_table, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


# =========================================================================
# Parser for 'show lisp instance-id <instance_id> named-services publisher'
# =========================================================================
class ShowLispNamedServicesPublisher(ShowLispPublisherSuperParser, ShowLispPublisherSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} named-services publisher
        * show lisp locator-table {vrf} instance-id {instance_id} named-services publisher
        * show lisp instance-id {instance_id} named-services publisher
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} named-services publisher',
        'show lisp locator-table {vrf} instance-id {instance_id} named-services publisher',
        'show lisp instance-id {instance_id} named-services publisher'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, vlan=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif vrf and instance_id:
                output = self.device.execute(self.cli_command[1].
                                             format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)
