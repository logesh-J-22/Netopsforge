expected_output = {
    "insecure_cli_submode_database":{
        1:{
            "configuration_submode":"sep-listen-config"
        },
        10:{
            "configuration_submode":"sip-ua"
        },
        11:{
            "configuration_submode":"archive"
        },
        12:{
            "configuration_submode":"eap-profile-mode"
        },
        13:{
            "configuration_submode":"voiceclass"
        },
        14:{
            "configuration_submode":"exec"
        },
        15:{
            "configuration_submode":"tls-profile"
        },
        16:{
            "configuration_submode":"key-chain-key"
        },
        17:{
            "configuration_submode":"key-chain-macsec-key"
        },
        18:{
            "configuration_submode":"sep-init-config"
        },
        19:{
            "configuration_submode":"cm-fallback"
        },
        2:{
            "configuration_submode":"dspfarmprofile"
        },
        3:{
            "configuration_submode":"dot1x-credential-mode"
        },
        4:{
            "configuration_submode":"router"
        },
        5:{
            "configuration_submode":"configure"
        },
        6:{
            "configuration_submode":"tls_tunnel"
        },
        7:{
            "configuration_submode":"line"
        },
        8:{
            "configuration_submode":"eap-mprofile-mode"
        },
        9:{
            "configuration_submode":"parameter-submode"
        }
    },
    "modules":{
        "BOOTP":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ip[[:space:]]+bootp[[:space:]]+server[[:space:]]*$",
                "description":"BOOTP server enabled - legacy protocol vulnerable to man-in-the-middle attacks and lacks security features",
                "reason":"Legacy protocol poses data confidentiality and integrity risks due to lack of encryption and authentication",
                "remediation":"Use DHCP to automatically configure network settings",
                "restriction":"YES",
                "execmode":"NO"
                }
            ]
        },
        "CALLMANAGER":{
            "entries":[
                {
                "entry_number":1,
                "submode":"cm-fallback",
                "submode_string":"call-manager-fallback",
                "command_regex":"^transport-tcp-tls[[:space:]]+v1\\.[01][[:space:]]*$",
                "description":"Call manager fallback configured with weak TLS version 1.0 or 1.1 - deprecated and vulnerable",
                "reason":"Weak tls version",
                "remediation":"Use stronger tls version to enhance security",
                "restriction":"YES",
                "execmode":"NO"
                }
            ]
        },
        "CAPWAP":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ap[[:space:]]+dtls-version[[:space:]]+dtls_1_0[[:space:]]*$",
                "description":"Access Point DTLS version configured with DTLS 1.0 - deprecated and vulnerable to various attacks",
                "reason":"Weak tls version",
                "remediation":"Use stronger tls version to enhance security",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":2,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ap[[:space:]]+dtls-ciphersuite[[:space:]]+priority[[:space:]]+[0-9]+[[:space:]]+(AES128-SHA|DHE-RSA-AES128-SHA|DHE-RSA-AES256-SHA)[[:space:]]*$",
                "description":"Access Point DTLS cipher suite configured with weak ciphers using SHA-1 - vulnerable to collision attacks",
                "reason":"Weak cipher(s) are present in the command",
                "remediation":"Use stronger cipher(s) to enhance security",
                "restriction":"YES",
                "execmode":"NO"
                }
            ]
        },
        "CDP":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^router odr",
                "description":"On-Demand Routing (ODR) enabled - obsolete routing protocol with security vulnerabilities",
                "reason":"On Demand Routing need to be disabled as in conjunction with cdp protocol static default routes will be added",
                "remediation":"This is a legacy feature, please consider disabling it",
                "restriction":"YES",
                "execmode":"NO"
                }
            ]
        },
        "DSPFARM_PROFILE":{
            "entries":[
                {
                "entry_number":1,
                "submode":"dspfarmprofile",
                "submode_string":"NULL",
                "command_regex":"^tls-version[[:space:]]+v1\\.[0,1]",
                "description":"DSP farm profile configured with TLS version 1.0 or 1.1 - deprecated and vulnerable to attacks",
                "reason":"Weak tls version",
                "remediation":"Use stronger tls version to enhance security",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "FTP":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ip[[:space:]]+ftp([[:space:]]+.*)?[[:space:]]*$",
                "description":"FTP service enabled - transmits credentials and data in plaintext, vulnerable to interception",
                "reason":"No encryption is configured",
                "remediation":"Transition to secure file transfer methods using SCP, SFTP, HTTPS protocols",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "HTTP":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ip[[:space:]]+http[[:space:]]+server[[:space:]]*$",
                "description":"HTTP server enabled - unencrypted protocol vulnerable to eavesdropping and man-in-the-middle attacks",
                "reason":"Legacy protocol poses data confidentiality and integrity risks due to lack of encryption and authentication",
                "remediation":"Use http secure server to ensure secure web access",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":2,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"ip[[:space:]]+http([[:space:]]+client)?[[:space:]]+tls-version[[:space:]]+TLSv1.(0|1)",
                "description":"HTTP client configured with weak TLS version 1.0 or 1.1 - vulnerable to various cryptographic attacks",
                "reason":"Weak tls version",
                "remediation":"Use stronger tls version to enhance security",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":3,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ip[[:space:]]+http([[:space:]]+client)?[[:space:]]+secure-ciphersuite[[:space:]]+.*aes-(128|256)-cbc-sha.*$",
                "description":"HTTP client using weak cipher suite with CBC mode and SHA-1 - vulnerable to padding oracle and collision attacks",
                "reason":"Weak cipher(s) are present in the command",
                "remediation":"Use stronger cipher(s) to enhance security",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "HTTPCLIENT":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^http[[:space:]]+client[[:space:]]+secure-ciphersuite[[:space:]]+(3des-cbc-sha|aes-128-cbc-sha|des-cbc-sha|null-md5|rc4-128-(md5|sha))[[:space:]]*$",
                "description":"HTTP client secure ciphersuite configured with weak algorithms - vulnerable to cryptographic attacks",
                "reason":"Weak cipher(s) are present in the command",
                "remediation":"Use stronger cipher(s) to enhance security",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":2,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^no[[:space:]]+http[[:space:]]+client[[:space:]]+secure-ciphersuite[[:space:]]*$",
                "description":"HTTP client secure ciphersuite disabled - allows weak cipher negotiations",
                "reason":"Weak cipher(s) are present in the command",
                "remediation":"Use stronger cipher(s) to enhance security",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "IP":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ip[[:space:]]+finger([[:space:]]+.*)?[[:space:]]*$",
                "description":"IP finger service enabled - provides system information that can be used for reconnaissance attacks",
                "reason":"IP Finger service can potentially expose system information to unauthorized users",
                "remediation":"Disable finger service and use secure SSH-based show commands for system information retrieval",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":2,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ip[[:space:]]+source-route([[:space:]]+.*)?[[:space:]]*$",
                "description":"IP source routing enabled - allows attackers to specify packet routing and bypass security controls",
                "reason":"IP source routing allows attackers to bypass network security controls and routing policies",
                "remediation":"This is a legacy feature, please consider disabling it",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":3,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^service[[:space:]]+finger([[:space:]]+.*)?[[:space:]]*$",
                "description":"Finger service enabled - provides detailed user information that can be exploited for social engineering",
                "reason":"IP Finger service can potentially expose system information to unauthorized users",
                "remediation":"Disable finger service and use secure SSH-based show commands for system information retrieval",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "KEY_CHAIN":{
            "entries":[
                {
                "entry_number":1,
                "submode":"key-chain-key",
                "submode_string":"key chain",
                "command_regex":"^key-string[[:space:]]+([^6].*|[[:space:]]*$)[[:space:]]*$",
                "description":"key-string in key-chain configured with weak encryption (type 0, 7, or plaintext) instead of secure type 6 encryption",
                "reason":"Configuration employs an Insecure method for password storage",
                "remediation":"Please consider migrating to a secure alternative such as Type-6",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "KEY_CHAIN_MACSEC":{
            "entries":[
                {
                "entry_number":1,
                "submode":"key-chain-macsec-key",
                "submode_string":"key chain",
                "command_regex":"^key-string[[:space:]]+([^6].*|[[:space:]]*$)[[:space:]]*$",
                "description":"key-string in macsec key-chain configured with weak encryption (type 0, 7, or plaintext) instead of secure type 6 encryption",
                "reason":"Configuration employs an Insecure method for password storage",
                "remediation":"Please consider migrating to a secure alternative such as Type-6",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "LINE":{
            "entries":[
                {
                "entry_number":1,
                "submode":"line",
                "submode_string":"line",
                "command_regex":"^transport[[:space:]]+(input|output|preferred)[[:space:]]+.*(telnet|rlogin|all|lat|mop|nasi|pad|udptn|acercon|v120|labp-ta).*$",
                "description":"Line transport configured with unencrypted protocols - allows plaintext transmission of sensitive data",
                "reason":"Legacy protocol poses data confidentiality and integrity risks due to lack of encryption and authentication",
                "remediation":"Migrate to secure SSH-based remote access",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":2,
                "submode":"line",
                "submode_string":"line",
                "command_regex":"^telnet[[:space:]]+.*(break-on-ip|ip-on-break|refuse-negotiations|speed|sync-on-break|transparent).*$",
                "description":"Telnet line options configured - enables unencrypted remote access vulnerable to session hijacking",
                "reason":"No encryption is configured",
                "remediation":"Migrate to secure SSH-based remote access",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "LOGGING":{
            "entries":[
                {
                "entry_number":1,
                "submode":"tls-profile",
                "submode_string":"logging tls-profile",
                "command_regex":"^tls-version[[:space:]]+TLSv1.1[[:space:]]*$",
                "description":"Logging TLS profile configured with TLS version 1.1 - deprecated and vulnerable to attacks",
                "reason":"Weak tls version",
                "remediation":"Use stronger tls version to enhance security",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":2,
                "submode":"tls-profile",
                "submode_string":"logging tls-profile",
                "command_regex":"^ciphersuite .*aes-(128|256)-cbc-sha.*",
                "description":"Logging TLS profile configured with weak cipher suite using CBC mode and SHA-1",
                "reason":"Weak cipher(s) are present in the command",
                "remediation":"Use stronger cipher(s) to enhance security",
                "restriction":"YES",
                "execmode":"NO"
                }
            ]
        },
        "NTP":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ntp[[:space:]]+authentication-key([[:space:]]+.*)+md5([[:space:]]+.*)?[[:space:]]*$",
                "description":"NTP authentication using MD5 - vulnerable to collision attacks and should use stronger algorithms",
                "reason":"Weak cipher(s) are present in the command",
                "remediation":"Transition to more secure algorithms like SHA and AES",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "PARSER":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^logging filter (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":2,
                "submode":"exec",
                "submode_string":"NULL",
                "command_regex":"^configure replace (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"YES"
                },
                {
                "entry_number":3,
                "submode":"exec",
                "submode_string":"NULL",
                "command_regex":"^configure network (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"YES"
                },
                {
                "entry_number":4,
                "submode":"sep-listen-config",
                "submode_string":"wsma profile listener",
                "command_regex":"^transport http .*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":5,
                "submode":"sep-init-config",
                "submode_string":"wsma profile initiator",
                "command_regex":"^transport http .*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":6,
                "submode":"exec",
                "submode_string":"NULL",
                "command_regex":"^write network (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"YES"
                },
                {
                "entry_number":7,
                "submode":"exec",
                "submode_string":"NULL",
                "command_regex":"^acm replace (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"YES"
                },
                {
                "entry_number":8,
                "submode":"exec",
                "submode_string":"NULL",
                "command_regex":"^acm configlet create (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"YES"
                },
                {
                "entry_number":9,
                "submode":"exec",
                "submode_string":"NULL",
                "command_regex":"^acm merge (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"YES"
                },
                {
                "entry_number":10,
                "submode":"exec",
                "submode_string":"NULL",
                "command_regex":"^acm save (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"YES"
                },
                {
                "entry_number":11,
                "submode":"exec",
                "submode_string":"NULL",
                "command_regex":"^acm rules (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"YES"
                },
                {
                "entry_number":12,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^scripting tcl init (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":13,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^scripting tcl encdir (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":14,
                "submode":"archive",
                "submode_string":"archive",
                "command_regex":"^path (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":15,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^shell init file (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":16,
                "submode":"exec",
                "submode_string":"NULL",
                "command_regex":"^shell environment save (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"YES"
                },
                {
                "entry_number":17,
                "submode":"exec",
                "submode_string":"NULL",
                "command_regex":"^shell environment load (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"YES"
                },
                {
                "entry_number":18,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^shell map [^[:space:]]+ script-file (ftp|tftp|rcp|http)://.*$",
                "description":"Command uses insecure transport protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "RCMD":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ip[[:space:]]+rcmd([[:space:]]+.*)?[[:space:]]*$",
                "description":"Remote command (rcmd) service enabled - allows unencrypted remote command execution without proper authentication",
                "reason":"No encryption is configured",
                "remediation":"This is a legacy feature, please consider disabling it",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "SANET":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^access-session[[:space:]]+tls-version[[:space:]]+1.0[[:space:]]*$",
                "description":"Access session configured with TLS version 1.0 - deprecated and vulnerable to various attacks",
                "reason":"Weak tls version",
                "remediation":"Use stronger tls version to enhance security",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":2,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^access-session[[:space:]]+tls-version[[:space:]]+all[[:space:]]*$",
                "description":"Access session allowing all TLS versions - includes deprecated and vulnerable versions",
                "reason":"Weak tls version",
                "remediation":"Use stronger tls version to enhance security",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":3,
                "submode":"eap-mprofile-mode",
                "submode_string":"eap method fast profile",
                "command_regex":"^pac-password[[:space:]]+[07][[:space:]]+.*$",
                "description":"EAP FAST profile PAC password configured with weak encryption instead of secure type 6 or 9",
                "reason":"Configuration employs an Insecure method for password storage",
                "remediation":"Please consider migrating to a secure alternative such as Type-6 or Type-9",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":4,
                "submode":"dot1x-credential-mode",
                "submode_string":"dot1x credentials",
                "command_regex":"^password[[:space:]]+[07][[:space:]]+.*$",
                "description":"Dot1x credentials password configured with weak encryption instead of secure type 6 or 9",
                "reason":"Configuration employs an Insecure method for password storage",
                "remediation":"Please consider migrating to a secure alternative such as Type-6 or Type-9",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":5,
                "submode":"eap-mprofile-mode",
                "submode_string":"eap method fast profile",
                "command_regex":"^local-key[[:space:]]+[07][[:space:]]+.*$",
                "description":"EAP FAST profile local key configured with weak encryption (type 0 or 7) instead of secure type 6 or 9",
                "reason":"Configuration employs an Insecure method for password storage",
                "remediation":"Please consider migrating to a secure alternative such as Type-6 or Type-9",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":6,
                "submode":"eap-profile-mode",
                "submode_string":"eap profile",
                "command_regex":"^method[[:space:]]+(md5|leap)[[:space:]]*$",
                "description":"EAP profile configured with weak authentication method MD5 or LEAP - vulnerable to dictionary attacks",
                "reason":"A weak authentication method is being configured as part of EAP profile",
                "remediation":"Please consider configuring a stronger method such as EAP-FAST, EAP-PEAP or EAP-TLS",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":7,
                "submode":"eap-profile-mode",
                "submode_string":"eap profile",
                "command_regex":"^ciphersuite[[:space:]]+(aes128-sha|aes256-sha|dhe-rsa-aes128-sha|dhe-rsa-aes256-sha|ecdhe-ecdsa-aes-sha|ecdhe-rsa-aes-sha)[[:space:]]*$",
                "description":"EAP profile configured with weak cipher suite using SHA-1 - vulnerable to collision attacks",
                "reason":"Weak cipher(s) are present in the command",
                "remediation":"Use stronger cipher(s) to enhance security",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":8,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^mab[[:space:]]+request[[:space:]]+format[[:space:]]+attribute[[:space:]]+2[[:space:]]+[07][[:space:]]+.*$",
                "description":"MAB request format password configured with weak encryption instead of secure type 6 or 9",
                "reason":"Configuration employs an Insecure method for password storage",
                "remediation":"Please consider migrating to a secure alternative such as Type-6 or Type-9",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":9,
                "submode":"parameter-submode",
                "submode_string":"parameter-map type webauth global",
                "command_regex":"^secure-webauth-disable[[:space:]]*",
                "description":"Secure web authentication disabled - allows unencrypted HTTP authentication vulnerable to credential theft",
                "reason":"Secure web authentication is disabled, forcing insecure web-based authentication via HTTP",
                "remediation":"Remove secure-webauth-disable configuration to ensure secure web-based authentication via HTTPS",
                "restriction":"YES",
                "execmode":"NO"
                }
            ]
        },
        "SIPUA":{
            "entries":[
                {
                "entry_number":1,
                "submode":"sip-ua",
                "submode_string":"sip-ua",
                "command_regex":"^transport[[:space:]]+tcp[[:space:]]+tls[[:space:]]+v1\\.[01][[:space:]]*$",
                "description":"SIP-UA transport configured with weak TLS version 1.0 or 1.1 - deprecated and vulnerable",
                "reason":"Weak tls version",
                "remediation":"Use stronger tls version to enhance security",
                "restriction":"YES",
                "execmode":"NO"
                }
            ]
        },
        "SNMP":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server community [^[:space:]]+.*$",
                "description":"SNMP community string configured - uses insecure SNMPv1/v2c protocol vulnerable to eavesdropping",
                "reason":"Legacy protocol poses data confidentiality and integrity risks due to lack of encryption and authentication",
                "remediation":"Configure snmp v3 user",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":2,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp mib community-map [^[:space:]]+.*$",
                "description":"SNMP MIB community map configured - exposes community strings in insecure SNMPv1/v2c",
                "reason":"Legacy protocol poses data confidentiality and integrity risks due to lack of encryption and authentication",
                "remediation":"Configure snmp v3 user",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":3,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server group [^[:space:]]+ v(1|2c).*$",
                "description":"SNMP group configured with insecure version 1 or 2c - lacks encryption and authentication",
                "reason":"Legacy protocol poses data confidentiality and integrity risks due to lack of encryption and authentication",
                "remediation":"Configure snmp v3 user",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":4,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server host [^[:space:]]+.* version (1|2c).*$",
                "description":"SNMP host configured with insecure version 1 or 2c - transmits data without encryption",
                "reason":"Legacy protocol poses data confidentiality and integrity risks due to lack of encryption and authentication",
                "remediation":"Configure snmp v3 user",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":5,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server host [^[:space:]]+.* version 3 (auth|noauth).*$",
                "description":"SNMP host configured with insufficient authentication - missing privacy encryption",
                "reason":"SNMP host with Auth/Noauth security level",
                "remediation":"Use SNMP host with Priv security level",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":6,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server host [^[:space:]]+( vrf [^[:space:]]+)?( (informs|traps))?( [067])?( [^[:space:]]+)?[[:space:]]*$",
                "description":"SNMP host configured without explicit version - defaults to insecure SNMPv1/v2c",
                "reason":"Legacy protocol poses data confidentiality and integrity risks due to lack of encryption and authentication",
                "remediation":"Configure snmp v3 user",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":7,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server user [^[:space:]]+ [^[:space:]]+.* v(1|2c).*$",
                "description":"SNMP user configured with insecure version 1 or 2c - uses plaintext community strings",
                "reason":"Legacy protocol poses data confidentiality and integrity risks due to lack of encryption and authentication",
                "remediation":"Configure snmp v3 user",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":8,
                "submode":"router",
                "submode_string":"router",
                "command_regex":"^snmp context [^[:space:]]+ community.*$",
                "description":"SNMP context using community string - vulnerable to packet sniffing and replay attacks",
                "reason":"Legacy protocol poses data confidentiality and integrity risks due to lack of encryption and authentication",
                "remediation":"Configure snmp v3 user",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":9,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server user [^[:space:]]+ [^[:space:]]+ v3 (encrypted )?auth md5 .+$",
                "description":"SNMP user configured with MD5 authentication - vulnerable to collision attacks",
                "reason":"Insecure hash digest",
                "remediation":"Use secure hash digest such as sha and sha-2",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":10,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server user [^[:space:]]+ [^[:space:]]+ v3 (encrypted )?auth sha ([067] )?[^[:space:]]+ priv (3des|des) .+$",
                "description":"SNMP user configured with weak privacy encryption DES/3DES - vulnerable to cryptographic attacks",
                "reason":"Configuration employs an Insecure method for password storage",
                "remediation":"Use secure cipher such as aes",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":11,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server user [^[:space:]]+ [^[:space:]]+ v3 (encrypted )?auth sha-2 (256|384|512) ([067] )?[^[:space:]]+ priv (3des|des) .+$",
                "description":"SNMP user configured with SHA-2 authentication but weak DES/3DES privacy encryption - vulnerable to cryptographic attacks",
                "reason":"Configuration employs an Insecure method for password storage",
                "remediation":"Use secure cipher such as aes",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":12,
                "submode":"router",
                "submode_string":"router",
                "command_regex":"^snmp context [^[:space:]]+ user [^[:space:]]+ (encrypted )?auth sha [^[:space:]]+ priv (3des|des|des56) .+$",
                "description":"SNMP context user configured with weak DES/3DES/DES56 privacy encryption - vulnerable to cryptographic attacks",
                "reason":"Configuration employs an Insecure method for password storage",
                "remediation":"Use secure cipher such as aes",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":13,
                "submode":"router",
                "submode_string":"router",
                "command_regex":"^snmp context [^[:space:]]+ user [^[:space:]]+ (encrypted )?auth md5 .+$",
                "description":"SNMP context user configured with MD5 authentication - vulnerable to collision attacks",
                "reason":"Insecure hash digest",
                "remediation":"Use secure hash digest such as sha and sha-2",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":14,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server group [^[:space:]]+ v3 (auth|noauth).*",
                "description":"SNMP group configured with insufficient authentication level - missing privacy encryption",
                "reason":"SNMP group with Auth/Noauth security level",
                "remediation":"Use SNMP group with Priv security level",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":15,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server user [^[:space:]]+ [^[:space:]]+ v3 (encrypted )?auth sha ([067] )?[^[:space:]]+( access.*)?[[:space:]]*$",
                "description":"SNMP user configured with SHA authentication but no privacy encryption - data transmitted in plaintext",
                "reason":"SNMP user with Auth/Noauth security level",
                "remediation":"Use SNMP user with Priv security level",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":16,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server user [^[:space:]]+ [^[:space:]]+ v3 (encrypted )?auth sha-2 (256|384|512) ([067] )?[^[:space:]]+( access.*)?[[:space:]]*$",
                "description":"SNMP user configured with SHA-2 authentication but no privacy encryption - data transmitted in plaintext",
                "reason":"SNMP user with Auth/Noauth security level",
                "remediation":"Use SNMP user with Priv security level",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":17,
                "submode":"router",
                "submode_string":"router",
                "command_regex":"^snmp context [^[:space:]]+ user [^[:space:]]+ (encrypted )?auth sha [^[:space:]]+( access.*)?[[:space:]]*$",
                "description":"SNMP context user configured with SHA authentication but no privacy encryption - data transmitted in plaintext",
                "reason":"SNMP user with Auth/Noauth security level",
                "remediation":"Use SNMP user with Priv security level",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":18,
                "submode":"router",
                "submode_string":"router",
                "command_regex":"snmp context [^[:space:]]+ user [^[:space:]]+( (credential|encrypted))?( access.*)?[[:space:]]*$",
                "description":"SNMP context user configured with minimal security settings - missing proper authentication and privacy",
                "reason":"SNMP user with Auth/Noauth security level",
                "remediation":"Use SNMP user with Priv security level",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":19,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server user [^[:space:]]+ [^[:space:]]+ v3( access.*)?[[:space:]]*$",
                "description":"SNMP user configured with no auth and no privacy encryption - data transmitted in plaintext",
                "reason":"SNMP user with Auth/Noauth security level",
                "remediation":"Use SNMP user with Priv security level",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":20,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server user [^[:space:]]+ [^[:space:]]+ v3 (encrypted )?auth sha ([067] )?[^[:space:]]+ priv aes (128|192|256) ([067] )?[^[:space:]]+[[:space:]]*$",
                "description":"SNMP user configured with AES privacy encryption but without access control lists - allows unrestricted SNMP access",
                "reason":"SNMP user without ACL",
                "remediation":"Use SNMP user with AccessList",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":21,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server user [^[:space:]]+ [^[:space:]]+ v3 (encrypted )?auth sha-2 (256|384|512) ([067] )?[^[:space:]]+ priv aes (128|192|256) ([067] )?[^[:space:]]+[[:space:]]*$",
                "description":"SNMP user configured with SHA-2 authentication and AES privacy but without access control lists - allows unrestricted SNMP access",
                "reason":"SNMP user without ACL",
                "remediation":"Use SNMP user with AccessList",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":22,
                "submode":"router",
                "submode_string":"router",
                "command_regex":"snmp context [^[:space:]]+ user [^[:space:]]+ (encrypted )?auth sha [^[:space:]]+ priv aes (128|192|256) [^[:space:]]+[[:space:]]*$",
                "description":"SNMP context user configured with AES privacy encryption but without access control lists - allows unrestricted SNMP access",
                "reason":"SNMP user without ACL",
                "remediation":"Use SNMP user with AccessList",
                "restriction":"YES",
                "execmode":"NO"
                },
                {
                "entry_number":23,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^snmp-server file-transfer access-group ([1-9][0-9]?|[^ ]+)( protocol (tftp|ftp|rcp).*)?$",
                "description":"SNMP file transfer using TFTP/FTP/RCP protocol",
                "reason":"Usage of weak file transfer protocol like FTP/TFTP/RCP/HTTP",
                "remediation":"Use secure File Transfer protocol like SFTP/HTTPS/SCP",
                "restriction":"YES",
                "execmode":"NO"
                }
            ]
        },
        "STCAPP":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^stcapp[[:space:]]+security[[:space:]]+tls-version[[:space:]]+v1\\.[0,1]",
                "description":"STCAPP security configured with TLS version 1.0 or 1.1 - deprecated and vulnerable to attacks",
                "reason":"Weak tls version",
                "remediation":"Use stronger tls version to enhance security",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "TELNET":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ip[[:space:]]+telnet([[:space:]]+.*)?[[:space:]]*$",
                "description":"IP telnet service enabled - transmits credentials and data in plaintext over the network",
                "reason":"IP traffic is not encrypted",
                "remediation":"Migrate to secure SSH-based remote access",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":2,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^service[[:space:]]+telnet-zeroidle([[:space:]]+.*)?[[:space:]]*$",
                "description":"Telnet zero-idle service enabled - unencrypted remote access protocol vulnerable to credential theft",
                "reason":"Telnet sessions are not configured with an idle timeout",
                "remediation":"Migrate to secure SSH-based remote access",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "TFTP":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^ip[[:space:]]+tftp([[:space:]]+.*)?[[:space:]]*$",
                "description":"TFTP service enabled - unencrypted file transfer protocol vulnerable to eavesdropping and tampering",
                "reason":"Legacy protocol poses data confidentiality and integrity risks due to lack of encryption and authentication",
                "remediation":"Transition to secure file transfer methods using SCP, SFTP, HTTPS protocols",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "TLS_TUNNEL":{
            "entries":[
                {
                "entry_number":1,
                "submode":"tls_tunnel",
                "submode_string":"crypto tls-tunnel",
                "command_regex":"^protection[[:space:]]+dhe-rsa-aes256-cbc-sha1[[:space:]]$",
                "description":"tls-tunnel using weak cipher suite dhe-rsa-aes256-cbc-sha1",
                "reason":"Weak cipher(s) are present in the command",
                "remediation":"Use stronger cipher(s) to enhance security",
                "restriction":"YES",
                "execmode":"NO"
                }
            ]
        },
        "TRANSPORT":{
            "entries":[
                {
                "entry_number":1,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^service[[:space:]]+tcp-small-servers([[:space:]]+.*)?[[:space:]]*$",
                "description":"TCP small servers enabled - provides unnecessary services like echo, discard, and daytime that can be exploited",
                "reason":"TCP small servers expose unnecessary network services and potential attack vectors",
                "remediation":"Disable small servers and use modern network diagnostic tools like ping, traceroute, or SSH-based commands",
                "restriction":"NO",
                "execmode":"NO"
                },
                {
                "entry_number":2,
                "submode":"configure",
                "submode_string":"NULL",
                "command_regex":"^service[[:space:]]+udp-small-servers([[:space:]]+.*)?[[:space:]]*$",
                "description":"UDP small servers enabled - provides unnecessary services that can be used for DDoS amplification attacks",
                "reason":"UDP small servers expose unnecessary network services and potential attack vectors",
                "remediation":"Disable small servers and use modern network diagnostic tools like ping, traceroute, or SSH-based commands",
                "restriction":"NO",
                "execmode":"NO"
                }
            ]
        },
        "VOICE":{
            "entries":[
                {
                "entry_number":1,
                "submode":"voiceclass",
                "submode_string":"voice class",
                "command_regex":"^cipher[[:space:]]+[0-9]+[[:space:]]+(DHE_RSA_WITH_AES_(128|256)_CBC_SHA|RSA_WITH_AES_(128|256)_CBC_SHA)[[:space:]]*$",
                "description":"Voice class configured with weak cipher suite - vulnerable to cryptographic attacks",
                "reason":"Weak cipher(s) are present in the command",
                "remediation":"Use stronger cipher(s) to enhance security",
                "restriction":"YES",
                "execmode":"NO"
                }
            ]
        }
    },
    "profile_status":"Active and Loaded",
    "profile_summary":{
        "bloom_filter_status":"Active",
        "hash_table_status":"Operational",
        "total_security_patterns":82
    },
    "profile_type":"Security Policy Database",
    "submode_summary":{
        "submode_database_status":"Active and Loaded",
        "submode_hash_table_status":"Operational"
    },
    "total_configuration_submodes":19,
    "total_patterns_loaded":82
    }