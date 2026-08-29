expected_output = {
    'security_associations': {
        'EGRESS': {
            1122018512: {
                'algorithm': 'AES_GCM_256',
                'direction': 'EGRESS',
                'encrypt_bytes': 0,
                'encrypt_pkts': 0,
                'errors': 0,
                'h_value': '0xe54a4e843a24505c6c987d685cfe7777140382ed15a6729131959c2347e1c341',
                'key': '0x7d7cc3468a45a93adf4bb7c0c27f0eff0076d4f493abe23cd1040aa827d44ba4',
                'key_extra': '0x1724eecd0000000000000000',
                'next_pn': 1,
                'spi': 1122018512,
            },
        },
        'INGRESS': {
            3229334400: {
                'algorithm': 'AES_GCM_256',
                'current_pn': 1,
                'decrypt_bytes': 0,
                'decrypt_pkts': 0,
                'direction': 'INGRESS',
                'errors': 0,
                'h_value': '0x77588c0e8d8fac1ab5a377e1aea399cd500d099d214103fbeb653fb7fec65f12',
                'key': '0x3b0d61bd760f67581dbfb17090a1b038b81efd2646b7e271d4ad70563586fb8d',
                'key_extra': '0x9bfb55570000000000000000',
                'spi': 3229334400,
            },
        },
    },
}
