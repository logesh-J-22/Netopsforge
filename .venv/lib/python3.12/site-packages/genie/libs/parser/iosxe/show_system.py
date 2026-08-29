"""show_system.py

"""
# Python
import re
import logging
import xml.etree.ElementTree as ET
from xml.dom import minidom
from genie.libs.parser.utils.common import Common

log = logging.getLogger(__name__)

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (
    Schema,
    Any,
    Optional,
    Or,
    And,
    Default,
    Use,
    ListOf
)


class ShowClockSchema(MetaParser):
    """Schema for show clock"""

    schema = {
        "timezone": str,
        "day": str,
        "day_of_week": str,
        "month": str,
        "year": str,
        "time": str,
    }


class ShowClock(ShowClockSchema):
    """Parser for show clock"""

    cli_command = "show clock"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # 05:26:38.035 EST Wed JAN 4 2019
        # *05:26:38.035 EST Wed JAN 4 2019
        # .05:26:38.035 EST Wed JAN 4 2019
        p1 = re.compile(
            r"^[\*|\.]?(?P<time>[\d\:\.]+) +(?P<timezone>\w+)"
            r" +(?P<day_of_week>\w+) +(?P<month>\w+) +"
            r"(?P<day>\d+) +(?P<year>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # 18:56:04.554 EST Mon Oct 17 2016
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k: str(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowSystemIntegrityAllMeasurementNonceSchema(MetaParser):
    """Schema for show system integrity all measurement nonce <nonce>"""

    schema = {
        "bay": str,
        "fru": str,
        "node": str,
        "chassis": str,
        "slot": {
            int: {
                "platform": str,
                "boot_hashes": {Any(): str},
                "os": {
                    "version": str,
                    "hashes": {
                        Any(): str,
                    },
                },
                "registers": {"PCR0": str, "PCR8": str},
                "signature": {"version": int, "value": str},
            },
        },
    }


class ShowSystemIntegrityAllMeasurementNonce(ShowSystemIntegrityAllMeasurementNonceSchema):
    """Parser for show system integrity all measurement nonce <nonce>"""

    cli_command = "show system integrity all measurement nonce {nonce}"

    def cli(self, nonce="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(nonce=nonce))

        # initial return dictionary
        ret_dict = {}
        # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
        p1 = re.compile(
            r"^LOCATION FRU=+(?P<fru>\S+) +SLOT=+(?P<slot>\d+) +BAY=+(?P<bay>\d+) +CHASSIS=+(?P<chassis>\S+) +NODE=+(?P<node>\d+)$"
        )
        # Platform: C9410R
        p2 = re.compile(r"^Platform: +(?P<platform>\S+)$")
        # MA1004R06.1604052017: 6243F41868F21144E7D5CE30683
        # 17.8.1r[FC1]: 48E0DD991BCD6274B842A42C0F9DEDCD8809E6187928F0
        # 112312_UEFI_SOC1_v12.1.33: F5A5FD42D16A20302798EF6ED309979B43003D2320D9F0E8EA9831A92759FB4BFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        p3 = re.compile(r"^(?P<boot_hash>[\(\)\[\]\.\_\:A-Z0-9a-z]+)\s(?P<value>[0-9A-F]+)$")
        # Version: BLD_POLARIS_DEV_LATEST_20220313_143357
        p4 = re.compile(r"^Version: +(?P<version>.*\_\S+)$")
        # cat9k_iosxe.BLD_POLARIS_DEV_LATEST_20220313_143357.SSA.bin: 452997E880E6CEF
        # cat9k-wlc.BLD_POLARIS_DEV_LATEST_20220313_143357.SSA.pkg: 9456F1B1CFB3A25C9
        # cat9k_iosxe.BLD_POLARIS_DEV_LATEST_20220313_143357.0.NODEFECT.SSA.smu.bin: 9D7CC2C73A688FAF294C4BB90CAA6FDB26B9B
        p5 = re.compile(r"^(?P<hashes>(.*bin)|(.*pkg))\:\s(?P<value>\S+)$")
        # PCR0: 6DEC62AF32505978BD553E7
        p6 = re.compile(r"^PCR0: +(?P<pcr0>([0-9A-F])+)$")
        # PCR8: 6DEC62AF32505978BD553E7
        p7 = re.compile(r"^PCR8: +(?P<pcr8>([0-9A-F])+)$")
        # Version: 1
        p8 = re.compile(r"^Version: +(?P<version>\d)$")
        # 922D10C26D9DFF33278B4EBD9935A968DD5641C51EF496251
        p9 = re.compile(r"^(?P<value>([0-9A-F])+)$")
        for line in output.splitlines():
            line = line.strip()

            # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
            m = p1.match(line)
            if m:
                count = 0
                group = m.groupdict()
                tmp = int(group["slot"])
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                ret_dict.update({"fru": group["fru"]})
                ret_dict.update({"chassis": group["chassis"]})
                ret_dict.update({"bay": group["bay"]})
                ret_dict.update({"node": group["node"]})
                continue

            # Platform: C9410R
            m = p2.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                device.update({"platform": group["platform"]})
                continue

            # MA1004R06.1604052017: 6243F41868F21144E7D5CE30683
            # 17.8.1r[FC1]: 48E0DD991BCD6274B842A42C0F9DEDCD8809E6187928F0
            m = p3.match(line)
            if m:
                if count <= 1:
                    slot = ret_dict.setdefault("slot", {})
                    device = slot.setdefault(tmp, {})
                    boot_hashes = device.setdefault("boot_hashes", {})
                    group = m.groupdict({})
                    boot_hashes.update({group["boot_hash"][:-1]: group["value"]})
                    count += 1
                    continue

            # Version: BLD_POLARIS_DEV_LATEST_20220313_143357
            m = p4.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                os = device.setdefault("os", {})
                os.update({"version": group["version"]})
                continue

            # cat9k_iosxe.BLD_POLARIS_DEV_LATEST_20220313_143357.SSA.bin: 452997E880E6CEF
            m = p5.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                os = device.setdefault("os", {})
                hashes = os.setdefault("hashes", {})
                hashes.update({group["hashes"]: group["value"]})
                continue

            # PCR0: 6DEC62AF32505978BD553E7
            m = p6.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                reg = device.setdefault("registers", {})
                reg.update({"PCR0": group["pcr0"]})
                continue

            # PCR8: 6DEC62AF32505978BD553E7
            m = p7.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                reg = device.setdefault("registers", {})
                reg.update({"PCR8": group["pcr8"]})
                continue

            # Version: 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                signature = device.setdefault("signature", {})
                signature.update({"version": int(group["version"])})
                continue

            # Value: 922D10C26D9DFF33278B4EBD9935A968DD5641C51EF496251
            m = p9.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                signature = device.setdefault("signature", {})
                signature.update({"value": group["value"]})
                continue
        return ret_dict

    def yang(self, nonce="", output=None):
        if not output:
            output = self.device.get(filter=('xpath', f'/system-integrity-oper-data/location/integrity[nonce={nonce}][request="choice-measurement"]')).data_xml
        log.info(minidom.parseString(output).toprettyxml())
        root = ET.fromstring(output)
        system_integrity_oper_data = Common.retrieve_xml_child(root=root, key='system-integrity-oper-data')
        ret_dict = {}
        name = None
        version = None
        for parent in system_integrity_oper_data:
            for child in parent:
                if child.tag.endswith('slot'):
                    slot = int(child.text)
                    slot_dict = ret_dict.setdefault('slot', {})
                    slot_id = slot_dict.setdefault(slot, {})
                elif child.tag.endswith('fru'):
                    ret_dict.update({'fru': child.text})
                elif child.tag.endswith('chassis'):
                    ret_dict.update({'chassis': child.text})
                elif child.tag.endswith('bay'):
                    ret_dict.update({'bay': child.text})
                elif child.tag.endswith('node'):
                    ret_dict.update({'node': child.text})
                elif child.tag.endswith('integrity'):
                    for sub_child in child:
                        if sub_child.tag.endswith('measurement'):
                            for sub_child1 in sub_child:
                                if sub_child1.tag.endswith('boot-loader'):
                                    for sub_child2 in sub_child1:
                                        boot_hash_dict = slot_id.setdefault('boot_hashes',{})
                                        if sub_child2.tag.endswith('version'):
                                            version = sub_child2.text
                                        elif version and sub_child2.tag.endswith('hash'):
                                            boot_hash_dict.update({version: sub_child2.text})
                                elif sub_child1.tag.endswith('platform'):
                                    slot_id.update({'platform': sub_child1.text})
                                elif sub_child1.tag.endswith('operating-system'):
                                    for sub_child2 in sub_child1:
                                        os_dict = slot_id.setdefault('os', {})
                                        if sub_child2.tag.endswith('version'):
                                            os_dict.update({'version': sub_child2.text})
                                        elif sub_child2.tag.endswith('package-integrity'):
                                            for sub_child3 in sub_child2:
                                                os_dict1 = slot_id.setdefault('os', {}). \
                                                                setdefault('hashes', {})
                                                if sub_child3.tag.endswith('name'):
                                                    name = sub_child3.text
                                                elif name and sub_child3.tag.endswith('hash'):
                                                    os_dict1.update({name: sub_child3.text})
                                elif sub_child1.tag.endswith('register'):
                                    for sub_child2 in sub_child1:
                                        regs_dict = slot_id.setdefault('registers', {})
                                        if sub_child2.tag.endswith('index'):
                                            name = 'PCR{}'.format(sub_child2.text)
                                        elif sub_child2.tag.endswith('pcr-content'):
                                            regs_dict.update({name: sub_child2.text})
                                            name = None
                                elif sub_child1.tag.endswith('signature'):
                                    for sub_child2 in sub_child1:
                                        sign_dict = slot_id.setdefault('signature', {})
                                        if sub_child2.tag.endswith('signature'):
                                            sign_dict.update({'value': sub_child2.text})
                                        elif sub_child2.tag.endswith('version'):
                                            sign_dict.update({'version': int(sub_child2.text)})
        return ret_dict


class ShowSystemIntegrityAllComplianceNonceSchema(MetaParser):
    """Schema for show system integrity all compliance nonce <nonce>"""

    schema = {
        "bay": str,
        "fru": str,
        "node": str,
        "chassis": str,
        "slot": {
            int: {
                "compliance": {
                    "secure_boot": str,
                    "tam_service": str,
                    "ldwm_envelope": str,
                    "num_btlstage": int,
                    "bivlen": int,
                    "register_pcr0_disabled": str,
                    "register_pcr8_disabled": str,
                },
                "signature": {"version": int, "value": str},
            },
        },
    }


class ShowSystemIntegrityAllComplianceNonce(ShowSystemIntegrityAllComplianceNonceSchema):
    """Parser for Show system integrity all compliance nonce <nonce>"""

    cli_command = "show system integrity all compliance nonce {nonce}"

    def cli(self, nonce="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(nonce=nonce))

        # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
        p1 = re.compile(
            r"^LOCATION FRU=+(?P<fru>\S+) +SLOT=+(?P<slot>\d+) +BAY=+(?P<bay>\d+) +CHASSIS=+(?P<chassis>\S+) +NODE=+(?P<node>\d+)$"
        )
        # secure_boot: true
        p2 = re.compile(r"^secure_boot: +(?P<secure_boot>\S+)$")
        # tam_service: hardware
        p3 = re.compile(r"^tam_service: +(?P<tam_service>\S+)$")
        # ldwm_envelope: false
        p4 = re.compile(r"^ldwm_envelope: +(?P<ldwm_envelope>\S+)$")
        # num_btlstage: 2
        p5 = re.compile(r"^num_btlstage: +(?P<num_btlstage>\S+)$")
        # bivlen: 64
        p6 = re.compile(r"^bivlen: +(?P<bivlen>\S+)$")
        # register.pcr0.disabled: false
        p7 = re.compile(r"^register.pcr0.disabled: +(?P<pcr0>\S+)$")
        # register.pcr8.disabled: false
        p8 = re.compile(r"^register.pcr8.disabled: +(?P<pcr8>\S+)$")
        # Version: 1
        p9 = re.compile(r"^Version: +(?P<version>\d)$")
        # Value: AA2B82869BD48E0CFFAF75133E14AE891F5592E61C8C3
        p10 = re.compile(r"^(?P<value>([0-9A-F])+)$")
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tmp = int(group["slot"])
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                ret_dict.update({"fru": group["fru"]})
                ret_dict.update({"chassis": group["chassis"]})
                ret_dict.update({"bay": group["bay"]})
                ret_dict.update({"node": group["node"]})
                continue

            # secure_boot: true
            m = p2.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update({"secure_boot": group["secure_boot"]})
                continue

            # tam_service: hardware
            m = p3.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update({"tam_service": group["tam_service"]})
                continue

            # ldwm_envelope: false
            m = p4.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update(
                    {"ldwm_envelope": group["ldwm_envelope"]}
                )
                continue

            # num_btlstage: 2
            m = p5.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update({"num_btlstage": int(group["num_btlstage"])})
                continue

            # bivlen: 64
            m = p6.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update({"bivlen": int(group["bivlen"])})
                continue

            # register.pcr0.disabled: false
            m = p7.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update(
                    {"register_pcr0_disabled": group["pcr0"]}
                )
                continue

            # register.pcr8.disabled: false
            m = p8.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update(
                    {"register_pcr8_disabled": group["pcr8"]}
                )
                continue

            # Version: 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("signature", {})
                slot[tmp]["signature"].update({"version": int(group["version"])})
                continue

            # Value: AA2B82869BD48E0CFFAF75133E14AE891F5592E61C8C3
            m = p10.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("signature", {})
                slot[tmp]["signature"].update({"value": group["value"]})
                continue
        return ret_dict

    def yang(self, nonce="", output=None):
        if not output:
            output = self.device.get(filter=('xpath', f'/system-integrity-oper-data/location/integrity[nonce={nonce}][request="choice-compliance"]')).data_xml
        log.debug(minidom.parseString(output).toprettyxml())
        root = ET.fromstring(output)
        system_integrity_oper_data = Common.retrieve_xml_child(root=root, key='system-integrity-oper-data')
        ret_dict = {}
        for parent in system_integrity_oper_data:
            for child in parent:
                if child.tag.endswith('slot'):
                    slot = int(child.text)
                    slot_dict = ret_dict.setdefault('slot', {})
                    slot_id = slot_dict.setdefault(slot, {})
                elif child.tag.endswith('fru'):
                    ret_dict.update({'fru': child.text})
                elif child.tag.endswith('chassis'):
                    ret_dict.update({'chassis': child.text})
                elif child.tag.endswith('bay'):
                    ret_dict.update({'bay': child.text})
                elif child.tag.endswith('node'):
                    ret_dict.update({'node': child.text})
                elif child.tag.endswith('integrity'):
                    for sub_child in child:
                        if sub_child.tag.endswith('compliance'):
                            for comp_child in sub_child:
                                if comp_child.tag.endswith('capability'):
                                    attr = None
                                    val = None
                                    for cap_elem in comp_child:
                                        if cap_elem.tag.endswith('attribute'):
                                            attr = cap_elem.text
                                        elif cap_elem.tag.endswith('value'):
                                            val = cap_elem.text
                                    if attr and val is not None:
                                        # Map XML attribute names to dict keys
                                        key_map = {
                                            'secure_boot': 'secure_boot',
                                            'tam_service': 'tam_service',
                                            'ldwm_envelope': 'ldwm_envelope',
                                            'num_btlstage': 'num_btlstage',
                                            'bivlen': 'bivlen',
                                            'register.pcr0.disabled': 'register_pcr0_disabled',
                                            'register.pcr8.disabled': 'register_pcr8_disabled',
                                        }
                                        dict_key = key_map.get(attr, attr)
                                        # Convert to int if appropriate
                                        if dict_key in ['num_btlstage', 'bivlen']:
                                            val = int(val)
                                        slot_id.setdefault('compliance', {}).update({dict_key: val})
                                elif comp_child.tag.endswith('signature'):
                                    sign_dict = slot_id.setdefault('signature', {})
                                    for sign_elem in comp_child:
                                        if sign_elem.tag.endswith('signature'):
                                            sign_dict.update({'value': sign_elem.text})
                                        elif sign_elem.tag.endswith('version'):
                                            sign_dict.update({'version': int(sign_elem.text)})
        return ret_dict
    

class ShowSystemIntegrityAllTrustChainNonceSchema(MetaParser):
    """Schema for system integrity all trust_chain nonce <nonce>"""

    schema = {
        "bay": str,
        "fru": str,
        "node": str,
        "chassis": str,
        "slot": {
            int: {
                "crca_certificate": str,
                "cmca_certificate": str,
                "sudi_certificate": str,
                "signature": {"version": int, "value": str},
            },
        },
    }


class ShowSystemIntegrityAllTrustChainNonce(ShowSystemIntegrityAllTrustChainNonceSchema):
    """Parser for system integrity all trust_chain nonce <nonce>"""

    cli_command = "show system integrity all trust_chain nonce {nonce}"

    def cli(self, nonce="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(nonce=nonce))

        # initial return dictionary
        ret_dict = {}

        # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=3 NODE=0
        p1 = re.compile(
            r"^LOCATION FRU=+(?P<fru>\S+) +SLOT=+(?P<slot>\d+) +BAY=+(?P<bay>\d+) +CHASSIS=+(?P<chassis>\S+) +NODE=+(?P<node>\d+)$"
        )
        # Version: 1
        p2 = re.compile(r"^Version: +(?P<version>\d)$")
        #   Value: 9DA0FB31FA0BF959BDE14FEE6E20D6CD837E8108E4D37E9088C67E8CD1E7A7C015C1
        p3 = re.compile(r"^(?P<value>[A-F0-9]+)$")
        # Certificate Name: CMCA CERTIFICATE
        p4 = re.compile(r"^Certificate Name: +(?P<certificate_name>\S+\s\S+)$")
        # -----BEGIN CERTIFICATE-----
        p5 = re.compile(r"^\-+BEGIN CERTIFICATE\-+$")
        # -----END CERTIFICATE-----
        p6 = re.compile(r"^\-+END CERTIFICATE\-+$")
        # MIIDfTCCAmWgAwIBAgIEAfLTJTANBgkqhkiG9w0BAQsFADAnMQ4wDAYDVQQKEwVDaXNjbzEVMBMG
        p7 = re.compile(r"^([a-zA-Z0-9/+=]+)$")

        certificate_name = ""
        certificate = ""
        begin_certificate = None

        for line in output.splitlines():
            line = line.strip()

            # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=3 NODE=0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tmp = int(group["slot"])
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                ret_dict.update({"fru": group["fru"]})
                ret_dict.update({"chassis": group["chassis"]})
                ret_dict.update({"bay": group["bay"]})
                ret_dict.update({"node": group["node"]})
                continue

            # Version: 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                signature = device.setdefault("signature", {})
                signature.update({"version": int(group["version"])})
                continue

            # Value: 9DA0FB31FA0BF959BDE14FEE6E20D6CD837E8108E4D37E9088C67E8CD1E7A7C015C1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                signature = device.setdefault("signature", {})
                signature.update({"value": group["value"]})
                continue

            # Certificate Name: CMCA CERTIFICATE
            m = p4.match(line)
            if m:
                group = m.groupdict()
                certificate_id = group["certificate_name"]
                continue

            # -----BEGIN CERTIFICATE-----
            m = p5.match(line)
            if m:
                begin_certificate = True
                certificate_name = certificate_id.replace(" ", "_").lower()
                continue

            # -----END CERTIFICATE-----
            m = p6.match(line)
            if m:
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                device.update({certificate_name: certificate})
                certificate = ""
                begin_certificate = False
                continue

            # MIIDfTCCAmWgAwIBAgIEAfLTJTANBgkqhkiG9w0BAQsFADAnMQ4wDAYDVQQKEwVDaXNjbzEVMBMG
            m = p7.match(line)
            if m:
                if begin_certificate:
                    certificate = certificate + m.group()
                    continue

        return ret_dict

    def yang(self, nonce="", output=None):
        if not output:
            output = self.device.get(filter=('xpath', f'/system-integrity-oper-data/location/integrity[nonce={nonce}][request="choice-trust-chain"]')).data_xml
        
        log.debug(minidom.parseString(output).toprettyxml())
        
        root = ET.fromstring(output)
        system_integrity_oper_data = Common.retrieve_xml_child(root=root, key='system-integrity-oper-data')
        ret_dict = {}
        name = None
        for parent in system_integrity_oper_data:
            for child in parent:
                if child.tag.endswith('slot'):
                    slot = int(child.text)
                    slot_dict = ret_dict.setdefault('slot', {})
                    slot_id = slot_dict.setdefault(slot, {})
                elif child.tag.endswith('fru'):
                    ret_dict.update({'fru': child.text})
                elif child.tag.endswith('chassis'):
                    ret_dict.update({'chassis': child.text})
                elif child.tag.endswith('bay'):
                    ret_dict.update({'bay': child.text})
                elif child.tag.endswith('node'):
                    ret_dict.update({'node': child.text})
                elif child.tag.endswith('integrity'):
                    for sub_child in child:
                        if sub_child.tag.endswith('trust-chain'):
                            for sub_child1 in sub_child:
                                if sub_child1.tag.endswith('trust-chain'):
                                    for sub_child2 in sub_child1:
                                        if sub_child2.tag.endswith('name'):
                                            name = sub_child2.text.replace(" ","_").lower()
                                        elif name and sub_child2.tag.endswith('value'):
                                            slot_id.update({name: sub_child2.text})
                                            name = None
                                elif sub_child1.tag.endswith('signature'):
                                    for sub_child2 in sub_child1:
                                        sign_dict = slot_id.setdefault('signature',{})
                                        if sub_child2.tag.endswith('signature'):
                                            sign_dict.update({'value': sub_child2.text})
                                        elif sub_child2.tag.endswith('version'):
                                            sign_dict.update({'version': int(sub_child2.text)})
        return ret_dict

class ShowSystemSecurityModeSchema(MetaParser):
    """Schema for show system security mode"""

    schema = {
        "system_security_mode": str,
    }

class ShowSystemSecurityMode(ShowSystemSecurityModeSchema):
    """Parser for show system security mode"""

    cli_command = "show system security mode"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        
        # System Security Mode : Insecure
        p1 = re.compile(r"^System Security Mode\s*:\s*(?P<mode>\S+)$")
        
        for line in output.splitlines():
            line = line.strip()

            # System Security Mode : Insecure
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({"system_security_mode": group["mode"]})
                continue
        
        return ret_dict

class ShowSystemInsecureConfigurationSchema(MetaParser):
    """Schema for show system insecure configuration"""

    schema = {
        "total_active_insecure_commands": int,
        "database_type": str,
        "scan_status": str,
        "database_state": str,
        Optional("insecure_entries"): {
            Any(): {
                Optional("module"): str,
                Optional("parent_command"): str,
                Optional("cli_command"): str,
                Optional("description"): str,
                Optional("reason"): str,
                Optional("remediation"): str,
                Optional("config_mode"): str,
                Optional("status"): str,
                Optional("severity"): str,
            },
        },
        "database_summary": {
            "total_active_entries_processed": int,
            "queue_status": str,
            "memory_status": str,
            "database_integrity": str,
        }
    }

class ShowSystemInsecureConfiguration(ShowSystemInsecureConfigurationSchema):
    """Parser for show system insecure configuration"""

    cli_command = "show system insecure configuration"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        
        # Total Active Insecure Commands: 9
        p1 = re.compile(r"^Total Active Insecure Commands:\s+(?P<total>\d+)$")

        # Database Type: Active (Current State)
        p2 = re.compile(r"^Database Type:\s+(?P<type>.+)$")

        # Scan Status: Complete
        p3 = re.compile(r"^Scan Status:\s+(?P<status>\S+)$")

        # Database State: Stable
        p4 = re.compile(r"^Database State:\s+(?P<state>\S+)$")

        # | ACTIVE INSECURE CONFIGURATION ENTRY [1/9]
        p5 = re.compile(r"^\|\s+ACTIVE INSECURE CONFIGURATION ENTRY\s+\[(?P<entry_number>\d+)/\d+\]")

        # |               Module: TFTP
        p6 = re.compile(r"^\|\s+Module:\s+(?P<module>\S+)$")

        # |       Parent Command: NA
        p7 = re.compile(r"^\|\s+Parent Command:\s+(?P<parent>.+)$")

        # |          CLI Command: ip tftp source-interface GigabitEthernet0/0
        p8 = re.compile(r"^\|\s+CLI Command:\s+(?P<command>.+)$")

        # |          Description: TFTP service enabled...
        p9 = re.compile(r"^\|\s+Description:\s+(?P<description>.+)$")

        # |               Reason: Legacy protocol...
        p10 = re.compile(r"^\|\s+Reason:\s+(?P<reason>.+)$")

        # |          Remediation: Transition to secure...
        p11 = re.compile(r"^\|\s+Remediation:\s+(?P<remediation>.+)$")

        # |          Config Mode: configure
        p12 = re.compile(r"^\|\s+Config Mode:\s+(?P<config_mode>\S+)$")

        # |               Status: ACTIVE
        p13 = re.compile(r"^\|\s+Status:\s+(?P<status>\S+)$")

        # |             Severity: HIGH
        p14 = re.compile(r"^\|\s+Severity:\s+(?P<severity>\S+)$")
        
        # DATABASE SUMMARY
        p15 = re.compile(r"^DATABASE SUMMARY$")

        # Total Active Entries Processed: 2
        p16 = re.compile(r"^Total Active Entries Processed:\s+(?P<total_active_entries_processed>\d+)$")

        # Queue Status: Preserved (read-only traversal)
        p17 = re.compile(r"^Queue Status:\s+(?P<queue_status>.+)$")

        # Memory Status: Allocated and stable
        p18 = re.compile(r"^Memory Status:\s+(?P<memory_status>.+)$")

        # Database Integrity: Verified
        p19 = re.compile(r"^Database Integrity:\s+(?P<database_integrity>\S+)$")
        
        for line in output.splitlines():
            line = line.strip()
         
            # Total Active Insecure Commands: 9
            m = p1.match(line)
            if m:
                ret_dict["total_active_insecure_commands"] = int(m.group("total"))
                continue
            
            # Database Type: Active (Current State)
            m = p2.match(line)
            if m:
                ret_dict["database_type"] = m.group("type")
                continue
            
            # Scan Status: Complete
            m = p3.match(line)
            if m:
                ret_dict["scan_status"] = m.group("status")
                continue
            
            # Database State: Stable
            m = p4.match(line)
            if m:
                ret_dict["database_state"] = m.group("state")
                continue
            
            # | ACTIVE INSECURE CONFIGURATION ENTRY [1/9]
            m = p5.match(line)
            if m:
                insecure_dict = ret_dict.setdefault("insecure_entries", {}).setdefault(int(m.group("entry_number")), {})
                continue
            
            # |               Module: TFTP
            m = p6.match(line)
            if m:
                insecure_dict["module"] = m.group("module")
                continue
            
            # |       Parent Command: NA
            m = p7.match(line)
            if m:
                insecure_dict["parent_command"] = m.group("parent")
                continue
            
            # |          CLI Command: ip tftp source-interface GigabitEthernet0/0
            m = p8.match(line)
            if m:
                insecure_dict["cli_command"] = m.group("command")
                continue
            
            # |          Description: TFTP service enabled...
            m = p9.match(line)
            if m:
                insecure_dict["description"] = m.group("description")
                continue
            
            # |               Reason: Legacy protocol...
            m = p10.match(line)
            if m:
                insecure_dict["reason"] = m.group("reason")
                continue
            
            # |          Remediation: Transition to secure...
            m = p11.match(line)
            if m:
                insecure_dict["remediation"] = m.group("remediation")
                continue

            # |          Config Mode: configure
            m = p12.match(line)
            if m:
                insecure_dict["config_mode"] = m.group("config_mode")
                continue
            
            # |          Status: Active
            m = p13.match(line)
            if m:
                insecure_dict["status"] = m.group("status")
                continue
            
            # |             Severity: HIGH
            m = p14.match(line)
            if m:
                insecure_dict["severity"] = m.group("severity")
                continue
        
            # DATABASE SUMMARY
            m = p15.match(line)
            if m:
                data_dict = ret_dict.setdefault("database_summary", {})
                continue
            
            # Total Active Entries Processed: 2
            m = p16.match(line)
            if m:
                data_dict["total_active_entries_processed"] = int(m.group("total_active_entries_processed"))
                continue
            
            # Queue Status: Preserved (read-only traversal)
            m = p17.match(line)
            if m:
                data_dict["queue_status"] = m.group("queue_status")
                continue
            
            # Memory Status: Allocated and stable
            m = p18.match(line)
            if m:
                data_dict["memory_status"] = m.group("memory_status")
                continue
            
            # Database Integrity: OK
            m = p19.match(line)
            if m:
                data_dict["database_integrity"] = m.group("database_integrity")
                continue

        return ret_dict

class ShowSystemInsecureProfileSchema(MetaParser):
    """Schema for show system insecure profile"""

    schema = {
        "total_patterns_loaded": int,
        "profile_type": str,
        "profile_status": str,
        "total_configuration_submodes": int,
        "modules": {
            str: {
                "entries": ListOf({
                    "entry_number": int,
                    "submode": str,
                    "submode_string": str,
                    "command_regex": str,
                    "description": str,
                    "reason": str,
                    "remediation": str,
                    "restriction": str,
                    "execmode": str,
                }),
            }
        },
        "profile_summary": {
            "total_security_patterns": int,
            "hash_table_status": str,
            "bloom_filter_status": str,
        },
        "insecure_cli_submode_database": {
            Any(): {
                "configuration_submode": str,
            }
        },
        "submode_summary": {
            "submode_database_status": str,
            "submode_hash_table_status": str,
        },

    }

class ShowSystemInsecureProfile(ShowSystemInsecureProfileSchema):
    """Parser for show system insecure profile"""

    cli_command = "show system insecure profile"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Total Patterns Loaded: 82
        p1 = re.compile(r"^Total Patterns Loaded: +(?P<total>\d+)$")

        # Profile Type: Security Policy Database
        p2 = re.compile(r"^Profile Type: +(?P<type>.+)$")

        # Profile Status: Active and Loaded
        p3 = re.compile(r"^Profile Status: +(?P<status>.+)$")

        # Total Configuration Submodes: 19
        p4 = re.compile(r"^Total Configuration Submodes: +(?P<total>\d+)$")

        # | MODULE:                                            LOGGING |
        p5 = re.compile(r"^\|\s+MODULE:\s+(?P<module>\S+)\s+\|$")

        # | ENTRY 1 FOR MODULE:                               LOGGING |
        p6 = re.compile(r"^\|\s+ENTRY (?P<num>\d+) FOR MODULE:\s+(?P<module>\S+) \|$")

        # |              Submode: tls-profile
        p7 = re.compile(r"^\|\s+Submode:\s+(?P<submode>.+)$")

        # |       Submode String: logging tls-profile
        p8 = re.compile(r"^\|\s+Submode String:\s+(?P<submode_string>.+)$")

        # |        Command Regex: ^tls-version[[:space:]]+TLSv1.1[[:space:]]*$
        p9 = re.compile(r"^\|\s+Command Regex:\s+(?P<regex>.+)$")

        # |          Description: Logging TLS profile configured with TLS version 1.1
        p10 = re.compile(r"^\|\s+Description:\s+(?P<description>.+)$")

        # |               Reason: Weak tls version
        p11 = re.compile(r"^\|\s+Reason:\s+(?P<reason>.+)$")

        # |          Remediation: Use stronger tls version to enhance security
        p12 = re.compile(r"^\|\s+Remediation:\s+(?P<remediation>.+)$")

        # |          Restriction: YES
        p13 = re.compile(r"^\|\s+Restriction:\s+(?P<restriction>\S+)$")

        # |             Execmode: NO
        p14 = re.compile(r"^\|\s+Execmode:\s+(?P<execmode>\S+)$")

        # PROFILE SUMMARY
        p15 = re.compile(r"^PROFILE SUMMARY$")

        # Total Security Patterns: 82
        p16 = re.compile(r"^Total Security Patterns: +(?P<total>\d+)$")

        # Hash Table Status: Operational
        p17 = re.compile(r"^Hash Table Status: +(?P<hash_status>.+)$")

        # Bloom Filter Status: Active
        p18 = re.compile(r"^Bloom Filter Status: +(?P<bloom_status>.+)$")

        # INSECURE CLI SUBMODE DATABASE
        p19 = re.compile(r"^INSECURE CLI SUBMODE DATABASE$")

        # |   1 |                                  sep-listen-config |
        p20 = re.compile(r"^\|\s+(?P<num>\d+)\s+\|\s+(?P<configuration_submode>.+)\s+\|$")

        # SUBMODE SUMMARY
        p21 = re.compile(r"^SUBMODE SUMMARY$")

        # Submode Database Status: Active and Loaded
        p22 = re.compile(r"^Submode Database Status: +(?P<submode_status>.+)$")

        # Submode Hash Table Status: Operational
        p23 = re.compile(r"^Submode Hash Table Status: +(?P<submode_hash_status>.+)$")

        for line in output.splitlines():
            line = line.strip()

            # Total Patterns Loaded: 82
            m = p1.match(line)
            if m:
                ret_dict["total_patterns_loaded"] = int(m.group("total"))
                continue

            # Profile Type: Security Policy Database
            m = p2.match(line)
            if m:
                ret_dict["profile_type"] = m.group("type")
                continue

            # Profile Status: Active and Loaded
            m = p3.match(line)
            if m:
                ret_dict["profile_status"] = m.group("status")
                continue

            # Total Configuration Submodes: 19
            m = p4.match(line)
            if m:
                ret_dict["total_configuration_submodes"] = int(m.group("total"))
                continue

            # | MODULE:                                            LOGGING |
            m = p5.match(line)
            if m:
                module_dict = ret_dict.setdefault("modules", {}).setdefault(m.group("module"), {})
                continue

            # | ENTRY 1 FOR MODULE:                               LOGGING |
            m = p6.match(line)
            if m:
                entries = module_dict.setdefault("entries", [])
                entries.append({
                    "entry_number": int(m.group("num")),
                })

            # |              Submode: tls-profile
            m = p7.match(line)
            if m:
                if entries:
                    entries[-1]["submode"] = m.group("submode").strip()
                continue

            # |       Submode String: logging tls-profile
            m = p8.match(line)
            if m:
                if entries:
                    entries[-1]["submode_string"] = m.group("submode_string").strip()
                continue

            # |        Command Regex: ^tls-version[[:space:]]+TLSv1.1[[:space:]]*$
            m = p9.match(line)
            if m:
                if entries:
                    entries[-1]["command_regex"] = m.group("regex").strip()
                continue

            # |          Description: Logging TLS profile configured with TLS version 1.1
            m = p10.match(line)
            if m:
                if entries:
                    entries[-1]["description"] = m.group("description").strip()
                continue

            # |               Reason: Weak tls version
            m = p11.match(line)
            if m:
                if entries:
                    entries[-1]["reason"] = m.group("reason").strip()
                continue

            # |          Remediation: Use stronger tls version to enhance security
            m = p12.match(line)
            if m:
                if entries:
                    entries[-1]["remediation"] = m.group("remediation").strip()
                continue

            # |          Restriction: YES
            m = p13.match(line)
            if m:
                if entries:
                    entries[-1]["restriction"] = m.group("restriction").strip()
                continue

            # |             Execmode: NO
            m = p14.match(line)
            if m:
                if entries:
                    entries[-1]["execmode"] = m.group("execmode").strip()
                continue

            # PROFILE SUMMARY
            m = p15.match(line)
            if m:
                profile_dict = ret_dict.setdefault("profile_summary", {})
                continue

            # Total Security Patterns: 82
            m = p16.match(line)
            if m:
                profile_dict["total_security_patterns"] = int(m.group("total"))
                continue

            # Hash Table Status: Operational
            m = p17.match(line)
            if m:
                profile_dict["hash_table_status"] = m.group("hash_status")
                continue

            # Bloom Filter Status: Active
            m = p18.match(line)
            if m:
                profile_dict["bloom_filter_status"] = m.group("bloom_status")
                continue

            # INSECURE CLI SUBMODE DATABASE
            m = p19.match(line)
            if m:
                submode_db_dict = ret_dict.setdefault("insecure_cli_submode_database", {})
                continue

            # |   1 |                                  sep-listen-config |
            m = p20.match(line)
            if m:
                config_dict = submode_db_dict.setdefault(int(m.group("num")), {})
                config_dict["configuration_submode"] = m.group("configuration_submode").strip()
                continue

            # SUBMODE SUMMARY
            m = p21.match(line)
            if m:
                submode_summary_dict = ret_dict.setdefault("submode_summary", {})
                continue

            # Submode Database Status: Active and Loaded
            m = p22.match(line)
            if m:
                submode_summary_dict["submode_database_status"] = m.group("submode_status")
                continue

            # Submode Hash Table Status: Operational
            m = p23.match(line)
            if m:
                submode_summary_dict["submode_hash_table_status"] = m.group("submode_hash_status")
                continue

        return ret_dict
