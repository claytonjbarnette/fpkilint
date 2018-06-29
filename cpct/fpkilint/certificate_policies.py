
policies_display_map = {
    '2.5.29.32.0': 'any-policy',

    # CITE / Test Polcies
    '2.16.840.1.101.3.2.1.48.1': 'TEST FBCA Rudimentary',
    '2.16.840.1.101.3.2.1.48.2': 'TEST FBCA Basic',
    '2.16.840.1.101.3.2.1.48.3': 'TEST FBCA Medium',
    '2.16.840.1.101.3.2.1.48.4': 'TEST FBCA Medium Hardware',
    '2.16.840.1.101.3.2.1.48.5': 'TEST FBCA Medium CBP',
    '2.16.840.1.101.3.2.1.48.6': 'TEST FBCA Medium Hardware CBP',
    '2.16.840.1.101.3.2.1.48.7': 'TEST FBCA High',
    '2.16.840.1.101.3.2.1.48.99': 'TEST FBCA devices',
    '2.16.840.1.101.3.2.1.48.100': 'TEST FBCA devices Hardware',
    '2.16.840.1.101.3.2.1.48.8': 'TEST id-fpki-common-policy',
    '2.16.840.1.101.3.2.1.48.9': 'TEST id-fpki-common-hardware',
    '2.16.840.1.101.3.2.1.48.10': 'TEST id-fpki-common-devices',
    '2.16.840.1.101.3.2.1.48.98': 'TEST id-fpki-common-devicesHardware',
    '2.16.840.1.101.3.2.1.48.11': 'TEST id-fpki-common-authentication',
    '2.16.840.1.101.3.2.1.48.12': 'TEST id-fpki-common-High',
    '2.16.840.1.101.3.2.1.48.13': 'TEST id-fpki-common-cardAuth',
    '2.16.840.1.101.3.2.1.48.109': 'TEST id-fpki-common-pivAuth-derived',
    '2.16.840.1.101.3.2.1.48.110': 'TEST id-fpki-common-pivAuth-derived-hardware',
    '2.16.840.1.101.3.2.1.48.14': 'TEST id-eGov-Level1',
    '2.16.840.1.101.3.2.1.48.15': 'TEST id-eGov-Level2',
    '2.16.840.1.101.3.2.1.48.16': 'TEST id-eGov-Applications',
    '2.16.840.1.101.3.2.1.48.78': 'TEST id-fpki-certpcy-pivi-hardware',
    '2.16.840.1.101.3.2.1.48.79': 'TEST id-fpki-certpcy-pivi-cardAuth',
    '2.16.840.1.101.3.2.1.48.80': 'TEST id-fpki-certpcy-pivi-contentSigning',
    '2.16.840.1.101.3.2.1.48.101': 'TEST id-sha1-medium-CBP',
    '2.16.840.1.101.3.2.1.48.102': 'TEST id-sha1-mediumHW-CBP',
    '2.16.840.1.101.3.2.1.48.81': 'TEST id-sha1-policy',
    '2.16.840.1.101.3.2.1.48.82': 'TEST id-sha1-hardware',
    '2.16.840.1.101.3.2.1.48.83': 'TEST id-sha1-devices',
    '2.16.840.1.101.3.2.1.48.84': 'TEST id-sha1-authentication',
    '2.16.840.1.101.3.2.1.48.85': 'TEST id-sha1-cardAuth',
    '2.16.840.1.101.3.2.1.48.86': 'TEST id- fpki-common-piv-contentSigning',
    '2.16.840.1.101.3.2.1.48.17': 'TEST Citizen & Commerce Provisional',
    '2.16.840.1.101.3.2.1.48.18': 'TEST Citizen & Commerce Approved',
    '2.16.840.1.101.3.2.1.48.19': 'TEST doe-basic',
    '2.16.840.1.101.3.2.1.48.20': 'TEST doe-medium',
    '2.16.840.1.101.3.2.1.48.21': 'TEST doe-high',
    '2.16.840.1.101.3.2.1.48.22': 'TEST doe-medium-v2',
    '2.16.840.1.101.3.2.1.48.23': 'TEST id-doj-Class1',
    '2.16.840.1.101.3.2.1.48.24': 'TEST id-doj-Class2',
    '2.16.840.1.101.3.2.1.48.25': 'TEST id-doj-Class3',
    '2.16.840.1.101.3.2.1.48.26': 'TEST id-doj-Class4',
    '2.16.840.1.101.3.2.1.48.27': 'TEST id-doj-Class5',
    '2.16.840.1.101.3.2.1.48.28': 'TEST id-fbi-mediumAssurance',
    '2.16.840.1.101.3.2.1.48.29': 'TEST id-fbi-highAssurance',
    '2.16.840.1.101.3.2.1.48.30': 'TEST aces-ca',
    '2.16.840.1.101.3.2.1.48.31': 'TEST aces-identity',
    '2.16.840.1.101.3.2.1.48.32': 'TEST aces-business-rep',
    '2.16.840.1.101.3.2.1.48.33': 'TEST aces-relying-party',
    '2.16.840.1.101.3.2.1.48.34': 'TEST aces-SSL',
    '2.16.840.1.101.3.2.1.48.35': 'TEST aces-fed-employee',
    '2.16.840.1.101.3.2.1.48.36': 'TEST aces-fed-employee-hw',
    '2.16.840.1.101.3.2.1.48.37': 'TEST id-gpo-medium',
    '2.16.840.1.101.3.2.1.48.38': 'TEST State of Illinois Level I (software)',
    '2.16.840.1.101.3.2.1.48.39': 'TEST State of Illinois Level I (hardware)',
    '2.16.840.1.101.3.2.1.48.40': 'TEST State of Illinois Level II (software)',
    '2.16.840.1.101.3.2.1.48.41': 'TEST State of Illinois Level II (hardware)',
    '2.16.840.1.101.3.2.1.48.42': 'TEST State of Illinois Level III (software)',
    '2.16.840.1.101.3.2.1.48.43': 'TEST State of Illinois Level III (hardware)',
    '2.16.840.1.101.3.2.1.48.44': 'TEST State of Illinois Level IV (hardware only)',
    '2.16.840.1.101.3.2.1.48.45': 'TEST State of Illinois MEDI Single-Use Certificate',
    '2.16.840.1.101.3.2.1.48.46': 'TEST nfc-basicAssurance',
    '2.16.840.1.101.3.2.1.48.47': 'TEST nfc-mediumAssurance',
    '2.16.840.1.101.3.2.1.48.48': 'TEST nfc-highAssurance',
    '2.16.840.1.101.3.2.1.48.49': 'TEST state-basic',
    '2.16.840.1.101.3.2.1.48.50': 'TEST state-low',
    '2.16.840.1.101.3.2.1.48.51': 'TEST state-moderate',
    '2.16.840.1.101.3.2.1.48.52': 'TEST state-high',
    '2.16.840.1.101.3.2.1.48.53': 'TEST state-mrtd',
    '2.16.840.1.101.3.2.1.48.54': 'TEST treasury-cp1',
    '2.16.840.1.101.3.2.1.48.55': 'TEST treasury-level 1',
    '2.16.840.1.101.3.2.1.48.56': 'TEST treasury-level 2',
    '2.16.840.1.101.3.2.1.48.57': 'TEST treasury-level 3',
    '2.16.840.1.101.3.2.1.48.58': 'TEST treasury-level 4',
    '2.16.840.1.101.3.2.1.48.111': 'TEST treasury-pivi-hardware',
    '2.16.840.1.101.3.2.1.48.112': 'TEST treasury-pivi-cardAuth',
    '2.16.840.1.101.3.2.1.48.113': 'TEST treasury-pivi-contentSigning',
    '2.16.840.1.101.3.2.1.48.59': 'TEST id-US-IRS-Securemail',
    '2.16.840.1.101.3.2.1.48.60': 'TEST pto-registered-practitioner',
    '2.16.840.1.101.3.2.1.48.61': 'TEST pto-inventor',
    '2.16.840.1.101.3.2.1.48.62': 'TEST pto-practitioner-employee',
    '2.16.840.1.101.3.2.1.48.63': 'TEST pto-basic',
    '2.16.840.1.101.3.2.1.48.64': 'TEST pto-service-provider',
    '2.16.840.1.101.3.2.1.48.65': 'TEST pto-service-provider-registrar',
    '2.16.840.1.101.3.2.1.48.66': 'TEST pto-basic-2003',
    '2.16.840.1.101.3.2.1.48.67': 'TEST pto-medium-2003',
    '2.16.840.1.101.3.2.1.48.68': 'TEST id-US-dod-basic',
    '2.16.840.1.101.3.2.1.48.69': 'TEST id-US-dod-medium-2048',
    '2.16.840.1.101.3.2.1.48.70': 'TEST id-US-dod-mediumhardware-2048',
    '2.16.840.1.101.3.2.1.48.71': 'TEST id-US-dod-FORTEZZA',
    '2.16.840.1.101.3.2.1.48.72': 'TEST id-US-dod-type1',
    '2.16.840.1.101.3.2.1.48.73': 'TEST Wells Fargo CPS',
    '2.16.840.1.101.3.2.1.48.74': 'TEST NASA',
    '2.16.840.1.101.3.2.1.48.75': 'TEST Treasury Medium-Software',
    '2.16.840.1.101.3.2.1.48.76': 'TEST Treasury Basic Org',
    '2.16.840.1.101.3.2.1.48.77': 'TEST State Medium Hardware',
    '2.16.840.1.101.3.2.1.48.90': 'TEST id-eGov-BAE-Broker',
    '2.16.840.1.101.3.2.1.48.91': 'TEST id-eGov-RelyingParty',
    '2.16.840.1.101.3.2.1.48.92': 'TEST id-eGov-MetaSigner-',
    '2.16.840.1.101.3.2.1.48.93': 'TEST id-eGov-MetaSigner-Hardware',
    '2.16.840.1.101.3.2.1.48.94': 'TEST id-eGov-Level1-IdP',
    '2.16.840.1.101.3.2.1.48.95': 'TEST id-eGov-Level2-IdP',
    '2.16.840.1.101.3.2.1.48.96': 'TEST id-eGov-Level3-IdP',
    '2.16.840.1.101.3.2.1.48.97': 'TEST id-eGov-Level4-IdP',
    '2.16.840.1.101.3.2.1.15.31': 'TEST id-dhs-certpcy-rudimentary',
    '2.16.840.1.101.3.2.1.15.32': 'TEST id-dhs-certpcy-basic',
    '2.16.840.1.101.3.2.1.15.33': 'TEST id-dhs-certpcy-medium',
    '2.16.840.1.101.3.2.1.15.34': 'TEST id-dhs-certpcy-high',
    '2.16.840.1.101.3.2.1.15.35': 'TEST id-dhs-certpcy-mediumHardware',
    '2.16.840.1.113733.1.7.21.1.1': 'TEST Class -1-VTN SSP-rudimentary',
    '2.16.840.1.113733.1.7.21.2.1': 'TEST Class 2-VTN SSP-basic',
    '2.16.840.1.113733.1.7.21.3.6': 'TEST Class 3-VTN SSP-medium',
    '2.16.840.1.113733.1.7.21.3.7': 'TEST Class 3-VTN SSP-mediumHardware',
    '2.16.840.1.113733.1.7.21.3.8': 'TEST Class 3-VTN SSP-Devices',
    '2.16.840.1.113733.1.7.21.3.13': 'TEST Class 3-VTN SSP-PIV-I Hardware',
    '2.16.840.1.113733.1.7.21.3.14': 'TEST Class 3-VTN SSP-Medium CBP',
    '2.16.840.1.113733.1.7.21.3.15': 'TEST Class 3-VTN SSP-Medium Hardware CBP',
    '2.16.840.1.113733.1.7.21.3.17': 'TEST Class 3-VTN SSP-PIV-I CardAuth',
    '2.16.840.1.113733.1.7.21.3.20': 'TEST Class 3-VTN SSP-PIV-I ContentSigning',
    '2.16.840.1.114027.200.3.10.10.1.8': 'TEST id-emspki-nfssp-rudimentary-policy',
    '2.16.840.1.114027.200.3.10.10.1.7': 'TEST id-emspki-nfssp-basic-policy',
    '2.16.840.1.114027.200.3.10.10.1.3': 'TEST id-emspki-nfssp-medium-policy',
    '2.16.840.1.114027.200.3.10.10.1.4': 'TEST id-emspki-nfssp-medium-hardware',
    '2.16.840.1.114027.200.3.10.10.1.6': 'TEST id-emspki-nfssp-medium-authentication',
    '2.16.840.1.114027.200.3.10.10.1.5': 'TEST id-emspki-nfssp-medium-cardAuth',
    '2.16.840.1.114027.200.3.10.10.1.9': 'TEST id-emspki-nfssp-pivi-contentSigning',
    '1.3.6.1.4.1.24019.1.1.1.101': 'TEST CertiPath Medium Software',
    '1.3.6.1.4.1.24019.1.1.1.102': 'TEST CertiPath Medium Hardware',
    '1.3.6.1.4.1.24019.1.1.1.103': 'TEST CertiPath High Hardware',
    '1.3.6.1.4.1.24019.1.1.1.104': 'TEST CertiPath Medium CBP Software',
    '1.3.6.1.4.1.24019.1.1.1.105': 'TEST CertiPath Medium CBP Hardware',
    '1.3.6.1.4.1.24019.1.1.1.106': 'TEST CertiPath highCBPHardware',
    '1.3.6.1.4.1.24019.1.1.1.107': 'TEST CertiPath IceCAP-hardware',
    '1.3.6.1.4.1.24019.1.1.1.108': 'TEST CertiPath IceCAP-cardAuth',
    '1.3.6.1.4.1.24019.1.1.1.109': 'TEST CertiPath IceCAP-contentSigning',
    '1.3.6.1.4.1.24019.1.1.1.110': 'TEST CertiPath variant medium Software',
    '1.3.6.1.4.1.24019.1.1.1.111': 'TEST CertiPath variant medium Hardware',
    '1.3.6.1.4.1.24019.1.1.1.112': 'TEST CertiPath variant high Hardware',
    '1.3.6.1.4.1.24019.1.1.1.113': 'TEST CertiPath variant medium CBP Software',
    '1.3.6.1.4.1.24019.1.1.1.114': 'TEST CertiPath variant medium CBP Hardware',
    '1.3.6.1.4.1.24019.1.1.1.115': 'TEST CertiPath variant high CBP Hardware',
    '2.16.840.1.114412.99.4.1.1': 'TEST DigiCert Level 1 Client Certificate - Personal',
    '2.16.840.1.114412.99.4.1.2': 'TEST DigiCert Level 1 Client Certificate - Enterprise',
    '2.16.840.1.114412.99.4.2': 'TEST DigiCert Level 2 Client Certificate - Basic',
    '2.16.840.1.114412.99.4.3.1': 'TEST DigiCert Level 3 Client Certificate – US -Medium',
    '2.16.840.1.114412.99.4.3.2': 'TEST DigiCert Level 3 Client Certificate – CBP -Medium',
    '2.16.840.1.114412.99.4.4.1': 'TEST Digicert Level 4 Client Certificate – US - Hardware',
    '2.16.840.1.114412.99.4.4.2': 'TEST Digicert Level 4 Client Certificate –CBP - Hardware',
    '2.16.840.1.114412.99.4.5.1': 'TEST Level 4 PIV-I - Hardware',
    '2.16.840.1.114412.99.4.5.2': 'TEST DigiCert Level 4 PIV-I – Card Authentication',
    '2.16.840.1.114412.99.4.5.3': 'TEST DigiCert Level 4 PIV-I – Content Signing',
    '2.16.840.1.114412.99.1.11': 'TEST DigiCert OV SSL',
    '2.16.840.1.101.3.2.1.48.103': 'TEST idusps-certpcy-rudimentaryAssurance',
    '2.16.840.1.101.3.2.1.48.104': 'TEST idusps-certpcy-basicAssurance',
    '2.16.840.1.101.3.2.1.48.105': 'TEST idusps-certpcy-mediumAssurance',
    '2.16.840.1.101.3.2.1.48.106': 'TEST idusps-certpcy-mediumHardware',
    '2.16.840.1.101.3.2.1.48.107': 'TEST idusps-certpcy-mediumDevice',
    '2.16.840.1.101.3.2.1.48.108': 'TEST idusps-certpcy-mediumDeviceHardware',

    '2': 'joint-iso-itu-t',
    '2.16': 'country',
    '2.16.840': 'us',
    '2.16.840.1': 'organization',
    '2.16.840.1.101': 'gov',
    '2.16.840.1.101.3': 'csor',
    '2.16.840.1.101.3.2': 'pki',
    '2.16.840.1.101.3.2.1': 'csor-certpolicy',
    '2.16.840.1.101.3.2.1.3': 'fbca-policies',
    '2.16.840.1.101.3.2.1.3.1': 'id-fpki-certpcy-rudimentaryAssurance',
    '2.16.840.1.101.3.2.1.3.2': 'id-fpki-certpcy-basicAssurance',
    '2.16.840.1.101.3.2.1.3.3': 'id-fpki-certpcy-mediumAssurance',
    '2.16.840.1.101.3.2.1.3.4': 'id-fpki-certpcy-highAssurance',
    '2.16.840.1.101.3.2.1.3.5': 'id-fpki-certpcy-testAssurance',
    '2.16.840.1.101.3.2.1.3.12': 'id-fpki-certpcy-mediumHardware',
    '2.16.840.1.101.3.2.1.3.14': 'id-fpki-certpcy-medium-CBP',
    '2.16.840.1.101.3.2.1.3.15': 'id-fpki-certpcy-mediumHW-CBP',
    '2.16.840.1.101.3.2.1.3.18': 'id-fpki-certpcy-pivi-hardware',
    '2.16.840.1.101.3.2.1.3.19': 'id-fpki-certpcy-pivi-cardAuth',
    '2.16.840.1.101.3.2.1.3.20': 'id-fpki-certpcy-pivi-contentSigning',
    '2.16.840.1.101.3.2.1.3.21': 'id-fpki-SHA1-medium-CBP',
    '2.16.840.1.101.3.2.1.3.22': 'id-fpki-SHA1-mediumHW-CBP',
    '2.16.840.1.101.3.2.1.3.23': 'id-fpki-SHA1-policy',
    '2.16.840.1.101.3.2.1.3.24': 'id-fpki-SHA1-hardware',
    '2.16.840.1.101.3.2.1.3.25': 'id-fpki-SHA1-devices',
    '2.16.840.1.101.3.2.1.3.37': 'id-fpki-certpcy-mediumDevice',
    '2.16.840.1.101.3.2.1.3.38': 'id-fpki-certpcy-mediumDeviceHardware',
    '2.16.840.1.101.3.2.1.3.6': 'id-fpki-common-policy',
    '2.16.840.1.101.3.2.1.3.7': 'id-fpki-common-hardware',
    '2.16.840.1.101.3.2.1.3.8': 'id-fpki-common-devices',
    '2.16.840.1.101.3.2.1.3.13': 'id-fpki-common-authentication',
    '2.16.840.1.101.3.2.1.3.16': 'id-fpki-common-high',
    '2.16.840.1.101.3.2.1.3.17': 'id-fpki-common-cardAuth',
    '2.16.840.1.101.3.2.1.3.26': 'id-fpki-SHA1-authentication',
    '2.16.840.1.101.3.2.1.3.27': 'id-fpki-SHA1-cardAuth',
    '2.16.840.1.101.3.2.1.3.36': 'id-fpki-common-devicesHardware',
    '2.16.840.1.101.3.2.1.3.39': 'id-fpki-common-piv-contentSigning',
    '2.16.840.1.101.3.2.1.3.40': 'id-fpki-common-derived-pivAuth',
    '2.16.840.1.101.3.2.1.3.41': 'id-fpki-common-derived-pivAuth-hardware',
    '2.16.840.1.101.3.2.1.3.42': 'id-fpki-common-public-trusted-serverAuth',
    '2.16.840.1.101.3.2.1.3.9': 'id-eGov-Level1',
    '2.16.840.1.101.3.2.1.3.10': 'id-eGov-Level2',
    '2.16.840.1.101.3.2.1.3.11': 'id-eGov-Applications',
    '2.16.840.1.101.3.2.1.3.28': 'id-eGov-Level1-IdP',
    '2.16.840.1.101.3.2.1.3.29': 'id-eGov-Level2-IdP',
    '2.16.840.1.101.3.2.1.3.30': 'id-eGov-Level3-IdP',
    '2.16.840.1.101.3.2.1.3.31': 'id-eGov-Level4-IdP',
    '2.16.840.1.101.3.2.1.3.32': 'id-eGov-BAE-Broker',
    '2.16.840.1.101.3.2.1.3.33': 'id-eGov-RelyingParty',
    '2.16.840.1.101.3.2.1.3.34': 'id-eGov-MetaSigner',
    '2.16.840.1.101.3.2.1.3.35': 'id-eGov-MetaSigner-Hardware',
    '2.16.840.1.101.3.2.1.1': 'aces',
    '2.16.840.1.101.3.2.1.1.1': 'aces-ca',
    '2.16.840.1.101.3.2.1.1.2': 'aces-identity',
    '2.16.840.1.101.3.2.1.1.3': 'aces-business-rep',
    '2.16.840.1.101.3.2.1.1.4': 'aces-relying-party',
    '2.16.840.1.101.3.2.1.1.5': 'aces-SSL',
    '2.16.840.1.101.3.2.1.1.6': 'aces-fed-employee',
    '2.16.840.1.101.3.2.1.1.7': 'aces-fed-employee-hw',
    '2.16.840.1.101.3.2.1.2': 'pto-policies',
    '2.16.840.1.101.3.2.1.2.1': 'pto-registered-practitioner',
    '2.16.840.1.101.3.2.1.2.2': 'pto-inventor',
    '2.16.840.1.101.3.2.1.2.3': 'pto-practitioner-employee',
    '2.16.840.1.101.3.2.1.2.4': 'pto-basic',
    '2.16.840.1.101.3.2.1.2.5': 'pto-service-provider',
    '2.16.840.1.101.3.2.1.2.6': 'pto-service-provider-registrar',
    '2.16.840.1.101.3.2.1.2.7': 'pto-basic-2003',
    '2.16.840.1.101.3.2.1.2.8': 'pto-medium-2003',
    '2.16.840.1.101.3.2.1.2.9': 'id-pto-mediumHardware',
    '2.16.840.1.101.3.2.1.2.10': 'id-pto-cardAuth',
    '2.16.840.1.101.3.2.1.2.11': 'id-pto-mediumDevice',
    '2.16.840.1.101.3.2.1.2.12': 'id-pto-mediumDeviceHardware',
    '2.16.840.1.101.3.2.1.2.13': 'id-pto-basicDevice',
    '2.16.840.1.101.3.2.1.4': 'nist-policies',
    '2.16.840.1.101.3.2.1.4.1': 'nist-cp1',
    '2.16.840.1.101.3.2.1.5': 'treasury-policies',
    '2.16.840.1.101.3.2.1.5.1': 'treasury-cp1',
    '2.16.840.1.101.3.2.1.5.2': 'id-treasury-certpcy-rudimentary',
    '2.16.840.1.101.3.2.1.5.3': 'id-treasury-certpcy-basicindividual',
    '2.16.840.1.101.3.2.1.5.8': 'id-treasury-certpcy-basicorganizational',
    '2.16.840.1.101.3.2.1.5.7': 'id-treasury-certpcy-medium',
    '2.16.840.1.101.3.2.1.5.4': 'id-treasury-certpcy-mediumhardware',
    '2.16.840.1.101.3.2.1.5.5': 'id-treasury-certpcy-high',
    '2.16.840.1.101.3.2.1.5.10': 'id-treasury-certpcy-pivi-hardware',
    '2.16.840.1.101.3.2.1.5.11': 'id-treasury-certpcy-pivi-cardAuth',
    '2.16.840.1.101.3.2.1.5.12': 'id-treasury-certpcy-pivi-contentSigning',
    '2.16.840.1.101.3.2.1.5.6': 'id-US-IRS-Securemail',
    '2.16.840.1.101.3.2.1.5.9': 'id-treacertpcy-internalnpe ',
    '2.16.840.1.101.3.2.1.5.13': 'id-treasury-certpcy-personDeviceAuth',
    '2.16.840.1.101.3.2.1.5.14': 'id-treasury-certpcy-internalperson',
    '2.16.840.1.101.3.2.1.6': 'state-policies',
    '2.16.840.1.101.3.2.1.6.1': 'state-basic',
    '2.16.840.1.101.3.2.1.6.2': 'state-low',
    '2.16.840.1.101.3.2.1.6.3': 'state-moderate',
    '2.16.840.1.101.3.2.1.6.4': 'state-high',
    '2.16.840.1.101.3.2.1.6.12': 'state-certpcy-mediumHardware',
    '2.16.840.1.101.3.2.1.6.14': 'state-certpcy-citizen-and-commerce',
    '2.16.840.1.101.3.2.1.6.37': 'state-certpcy-mediumDevice',
    '2.16.840.1.101.3.2.1.6.38': 'state-certpcy-mediumDeviceHardware',
    '2.16.840.1.101.3.2.1.6.100': 'state-mrtd',
    '2.16.840.1.101.3.2.1.7': 'fdic-policies',
    '2.16.840.1.101.3.2.1.7.1': 'fdic-basic',
    '2.16.840.1.101.3.2.1.7.2': 'fdic-low',
    '2.16.840.1.101.3.2.1.7.3': 'fdic-moderate',
    '2.16.840.1.101.3.2.1.7.4': 'fdic-high',
    '2.16.840.1.101.3.2.1.8': 'usda-nfc-policies',
    '2.16.840.1.101.3.2.1.8.1': 'nfc-basicAssurance',
    '2.16.840.1.101.3.2.1.8.2': 'nfc-mediumAssurance',
    '2.16.840.1.101.3.2.1.8.3': 'nfc-highAssurance',
    '2.16.840.1.101.3.2.1.9': 'dea-policies',
    '2.16.840.1.101.3.2.1.9.1': 'dea-csos-cp',
    '2.16.840.1.101.3.2.1.9.2': 'dea-epcs-policy',
    '2.16.840.1.101.3.2.1.10': 'doe-policies',
    '2.16.840.1.101.3.2.1.10.1': 'doe-basic',
    '2.16.840.1.101.3.2.1.10.2': 'doe-medium',
    '2.16.840.1.101.3.2.1.10.3': 'doe-high',
    '2.16.840.1.101.3.2.1.10.4': 'doe-medium-v2',
    '2.16.840.1.101.3.2.1.11': 'dol-policies',
    '2.16.840.1.101.3.2.1.11.1': 'dol-basic',
    '2.16.840.1.101.3.2.1.11.2': 'dol-medium',
    '2.16.840.1.101.3.2.1.12': 'eca-policies',
    '2.16.840.1.101.3.2.1.12.1': 'id-eca-medium',
    '2.16.840.1.101.3.2.1.12.3': 'id-eca-medium-token',
    '2.16.840.1.101.3.2.1.12.2': 'id-eca-medium-hardware',
    '2.16.840.1.101.3.2.1.12.4': 'id-eca-medium-sha256',
    '2.16.840.1.101.3.2.1.12.5': 'id-eca-medium-token-sha256',
    '2.16.840.1.101.3.2.1.12.6': 'id-eca-medium-hardware-pivi',
    '2.16.840.1.101.3.2.1.12.7': 'id-eca-cardauth-pivi',
    '2.16.840.1.101.3.2.1.12.8': 'id-eca-contentsigning-pivi',
    '2.16.840.1.101.3.2.1.12.9': 'id-eca-medium-device-sha256',
    '2.16.840.1.101.3.2.1.12.10': 'id-eca-medium-hardware-sha256',
    '2.16.840.1.101.3.2.1.13': 'fda-policies',
    '2.16.840.1.101.3.2.1.13.1': 'id-ORApki-assurance-test',
    '2.16.840.1.101.3.2.1.13.2': 'id-ORApki-assurance-basic',
    '2.16.840.1.101.3.2.1.13.3': 'id-ORApki-assurance-medium',
    '2.16.840.1.101.3.2.1.13.4': 'id-ORApki-assurance-high',
    '2.16.840.1.101.3.2.1.13.5': 'id-pki-HHSdomains',
    '2.16.840.1.101.3.2.1.13.5.1': 'id-HHSdomains-LoA',
    '2.16.840.1.101.3.2.1.13.5.1.1': 'id-HHSdomains-assurance-basic',
    '2.16.840.1.101.3.2.1.13.5.1.2': 'id-HHSdomains-assurance-high',
    '2.16.840.1.101.3.2.1.13.5.2': 'id-HHSdomains-OPDIVpolicies',
    '2.16.840.1.101.3.2.1.13.5.2.1': 'id-pki-IHSdomains',
    '2.16.840.1.101.3.2.1.13.5.2.2': 'id-pki-NIHdomains',
    '2.16.840.1.101.3.2.1.13.5.2.3': 'id-pki-FDAdomains',
    '2.16.840.1.101.3.2.1.14': 'citizen-and-commerce-policies',
    '2.16.840.1.101.3.2.1.14.1': 'citizen-and-commerce-provisional',
    '2.16.840.1.101.3.2.1.14.2': 'citizen-and-commerce-approved',
    '2.16.840.1.101.3.2.1.15': 'dhs-policies',
    '2.16.840.1.101.3.2.1.15.0': 'id-dhs-pkiObjects',
    '2.16.840.1.101.3.2.1.15.0.1': 'id-dhs-USVISITsigner',
    '2.16.840.1.101.3.2.1.15.0.2': 'id-dhs-MRTDValidationV4',
    '2.16.840.1.101.3.2.1.15.0.3': 'id-dhs-ValidationList',
    '2.16.840.1.101.3.2.1.15.0.4': 'id-dhs-CertStatus',
    '2.16.840.1.101.3.2.1.15.0.5': 'id-dhs-CountryStatus',
    '2.16.840.1.101.3.2.1.15.1': 'id-dhs-certpcy-rudimentary',
    '2.16.840.1.101.3.2.1.15.2': 'id-dhs-certpcy-basic',
    '2.16.840.1.101.3.2.1.15.3': 'id-dhs-certpcy-medium',
    '2.16.840.1.101.3.2.1.15.4': 'id-dhs-certpcy-high',
    '2.16.840.1.101.3.2.1.15.5': 'id-dhs-certpcy-mediumHardware',
    '2.16.840.1.101.3.2.1.15.6': 'id-dhs-certpcy-cardAuth',
    '2.16.840.1.101.3.2.1.15.7': 'id-dhs-certpcy-internalBasic',
    '2.16.840.1.101.3.2.1.15.8': 'id-dhs-certpcy-internalNpe',
    '2.16.840.1.101.3.2.1.15.9': 'id-dhs-certpcy-HSDNMACMediumDevice',
    '2.16.840.1.101.3.2.1.15.10': 'id-dhs-certpcy-HSDNMediumDevice',
    '2.16.840.1.101.3.2.1.15.11': 'id-dhs-certpcy-HSDNMediumHuman',
    '2.16.840.1.101.3.2.1.15.12': 'id-dhs-certpcy-HSDNMediumHumanDerived',
    '2.16.840.1.101.3.2.1.15.13': 'id-dhs-certpcy-HSDNCodeSigning',
    '2.16.840.1.101.3.2.1.15.36': 'id-dhs-certpcy-testCardAuth',
    '2.16.840.1.101.3.2.1.15.37': 'id-dhs-certpcy-testInternalBasic',
    '2.16.840.1.101.3.2.1.15.38': 'id-dhs-certpcy-testInternalNpe',
    '2.16.840.1.101.3.2.1.16': 'doj-policies',
    '2.16.840.1.101.3.2.1.16.1': 'id-doj-Class1',
    '2.16.840.1.101.3.2.1.16.2': 'id-doj-Class2',
    '2.16.840.1.101.3.2.1.16.3': 'id-doj-Class3',
    '2.16.840.1.101.3.2.1.16.4': 'id-doj-Class4',
    '2.16.840.1.101.3.2.1.16.5': 'id-doj-Class5',
    '2.16.840.1.101.3.2.1.16.6.1': 'id-fbi-mediumAssurance',
    '2.16.840.1.101.3.2.1.16.6.2': 'id-fbi-highAssurance',
    '2.16.840.1.101.3.2.1.16.6.3': 'id-fbi-cjis-basic-individual',
    '2.16.840.1.101.3.2.1.16.6.4': 'id-fbi-cjis-basic-organizational',
    '2.16.840.1.101.3.2.1.16.6.5': 'id-fbi-cjis-medium',
    '2.16.840.1.101.3.2.1.16.6.6': 'id-fbi-cjis-mediumSW',
    '2.16.840.1.101.3.2.1.16.6.7': 'id-fbi-cjismediumHW',
    '2.16.840.1.101.3.2.1.16.6.8': 'id-fbi-cjis-mediumDevice',
    '2.16.840.1.101.3.2.1.16.6.9': 'id-fbi-cjis-high',
    '2.16.840.1.101.3.2.1.17': 'gpo-policies',
    '2.16.840.1.101.3.2.1.17.1': 'id-gpo-medium',
    '2.16.840.1.101.3.2.1.17.2': 'id-gpo-medium-hardware',
    '2.16.840.1.101.3.2.1.17.3': 'id-gpo-certpcy-devices',
    '2.16.840.1.101.3.2.1.17.4': 'id-gpo-certpcy-authentication',
    '2.16.840.1.101.3.2.1.17.5': 'id-gpo-certpcy-cardAuth',
    '2.16.840.1.101.3.2.1.18': 'nrc-policies',
    '2.16.840.1.101.3.2.1.18.1': 'id-nrc-level3',
    '2.16.840.1.101.3.2.1.18.2': 'id-nrc-level2',
    '2.16.840.1.101.3.2.1.19': 'doi-policies',
    '2.16.840.1.101.3.2.1.19.1': 'id-doi-basic',
    '2.16.840.1.101.3.2.1.19.2': 'id-doi-medium',
    '2.16.840.1.101.3.2.1.20': 'usps-policies',
    '2.16.840.1.101.3.2.1.20.1': 'id-usps-certpcy-rudimentaryAssurance',
    '2.16.840.1.101.3.2.1.20.2': 'id-usps-certpcy-basicAssurance',
    '2.16.840.1.101.3.2.1.20.3': 'id-usps-certpcy-mediumAssurance',
    '2.16.840.1.101.3.2.1.20.12': 'id-usps-certpcy-mediumHardware',
    '2.16.840.1.101.3.2.1.20.18': 'id-usps-certpcy-pivi-hardware',
    '2.16.840.1.101.3.2.1.20.19': 'id-usps-certpcy-pivi-cardAuth',
    '2.16.840.1.101.3.2.1.20.20': 'id-usps-certpcy-pivi-contentSigning',
    '2.16.840.1.101.3.2.1.20.37': 'id-usps-certpcy-mediumDevice',
    '2.16.840.1.101.3.2.1.20.38': 'id-usps-certpcy-mediumDeviceHardware',
    '2.16.840.1.101.3.2.1.20.4.1': 'id-usps-Testcertpcy-rudimentaryAssurance',
    '2.16.840.1.101.3.2.1.20.4.2': 'id-usps-Testcertpcy-basicAssurance',
    '2.16.840.1.101.3.2.1.20.4.3': 'id-usps-Testcertpcy-mediumAssurance',
    '2.16.840.1.101.3.2.1.20.4.12': 'id-usps-Testcertpcy-mediumHardware',
    '2.16.840.1.101.3.2.1.20.4.18': 'id-usps-Testcertpcy-pivi-hardware',
    '2.16.840.1.101.3.2.1.20.4.19': 'id-usps-Testcertpcy-pivi-cardAuth',
    '2.16.840.1.101.3.2.1.20.4.20': 'id-usps-Testcertpcy-pivi-contentSigning',
    '2.16.840.1.101.3.2.1.20.4.37': 'id-usps-Testcertpcy-mediumDevice',
    '2.16.840.1.101.3.2.1.20.4.38': 'id-usps-Testcertpcy-mediumDeviceHardware',
    '2.16.840.1.101.3.2.1.21': 'cnss-policies',
    '2.16.840.1.101.3.2.1.22': 'ferc-policies',
    '2.16.840.1.101.3.2.1.22.1': 'id-ferc-Test',
    '2.16.840.1.101.3.2.1.22.2': 'id-ferc-Basic',
    '2.16.840.1.101.3.2.1.22.3': 'id-ferc-Medium',
    '2.16.840.1.101.3.2.1.22.4': 'id-ferc-Medium-Hardware',
    '2.16.840.1.101.3.2.1.22.5': 'id-ferc-High',
    '2.16.840.1.101.3.2.1.23': 'usaid-policies',
    '2.16.840.1.101.3.2.1.23.1': 'id-usaid-basic',
    '2.16.840.1.101.3.2.1.23.2': 'id-usaid-medium',
    '2.16.840.1.101.3.2.1.24': 'ussocom-policies',
    '2.16.840.1.101.3.2.1.24.1': 'id-ussocom-basic',
    '2.16.840.1.101.3.2.1.24.2': 'id-ussocom-medium',
    '2.16.840.1.101.3.2.1.25': 'nnpp-policies',
    '2.16.840.1.101.3.2.1.26': 'cftc-policies',
    '2.16.840.1.101.3.2.1.26.1': 'id-us-cftc-cp',
    '2.16.840.1.101.3.2.1.48': 'csor-test-policies',
    '1': 'iso',
    '1.3': 'identified-organization',
    '1.3.6': 'dod',
    '1.3.6.1': 'internet',
    '1.3.6.1.4': 'private',
    '1.3.6.1.4.1': 'enterprise',
    '1.3.6.1.4.1.24019': 'certipath',
    '1.3.6.1.4.1.24019.1': 'certipath-id-security',
    '1.3.6.1.4.1.24019.1.1': 'certipath-id-pki',
    '1.3.6.1.4.1.24019.1.1.1': 'certipath-certificate-policies',
    '1.3.6.1.4.1.24019.1.1.1.1': 'certipath-mediumSoftware',
    '1.3.6.1.4.1.24019.1.1.1.2': 'certipath-mediumHardware',
    '1.3.6.1.4.1.24019.1.1.1.3': 'certipath-highHardware',
    '1.3.6.1.4.1.24019.1.1.1.4': 'certipath-mediumCBPSoftware',
    '1.3.6.1.4.1.24019.1.1.1.5': 'certipath-mediumCBPHardware',
    '1.3.6.1.4.1.24019.1.1.1.6': 'certipath-highCBPHardware',
    '1.3.6.1.4.1.24019.1.1.1.7': 'certipath-IceCAP-hardware',
    '1.3.6.1.4.1.24019.1.1.1.8': 'certipath-IceCAP-cardAuth',
    '1.3.6.1.4.1.24019.1.1.1.9': 'certipath-IceCAP-contentSigning',
    '1.3.6.1.4.1.24019.1.1.1.23': 'certipath-medium-device-software',
    '1.3.6.1.4.1.24019.1.1.1.24': 'certipath-medium-device-hardware',
    '1.3.6.1.4.1.24019.1.1.1.17': 'certipath-variant-mediumSoftware',
    '1.3.6.1.4.1.24019.1.1.1.18': 'certipath-variant-mediumHardware',
    '1.3.6.1.4.1.24019.1.1.1.19': 'certipath-variant-highHardware',
    '1.3.6.1.4.1.24019.1.1.1.20': 'certipath-variant-mediumCBPSoftware',
    '1.3.6.1.4.1.24019.1.1.1.21': 'certipath-variant-mediumCBPHardware',
    '1.3.6.1.4.1.24019.1.1.1.22': 'certipath-variant-highCBPHardware',
    '1.3.6.1.4.1.24019.1.1.1.25': 'certipath-variant-medium-device-software',
    '1.3.6.1.4.1.24019.1.1.1.26': 'certipath-variant-medium-device-hardware',

    '1.3.6.1.4.1.73.15.3.1.5': 'boeing-mediumHardware-SHA1',
    '1.3.6.1.4.1.73.15.3.1.4': 'boeing-mediumSoftware-SHA1',
    '1.3.6.1.4.1.73.15.3.1.8': 'boeing-mediumCBPSoftware-SHA1',
    '1.3.6.1.4.1.73.15.3.1.9': 'boeing-mediumCBPHardware-SHA1',
    '1.3.6.1.4.1.73.15.3.1.10': 'boeing-cardAuthentication',
    '1.3.6.1.4.1.73.15.3.1.11': 'boeing-mediumSoftware-SHA256',
    '1.3.6.1.4.1.73.15.3.1.12': 'boeing-mediumHardware-SHA256',
    '1.3.6.1.4.1.73.15.3.1.13': 'boeing-mediumCBPSoftware-SHA256',
    '1.3.6.1.4.1.73.15.3.1.14': 'boeing-mediumCBPHardware-SHA256',
    '1.3.6.1.4.1.73.15.3.1.15': 'boeing-mediumHardware-cardAuth-SHA256',
    '1.3.6.1.4.1.73.15.3.1.16': 'boeing-mediumHardware-contentSigning-SHA1',
    '1.3.6.1.4.1.73.15.3.1.17': 'boeing-mediumHardware-contentSigning-SHA256',

    '1.3.6.1.4.1.25054.3.1.1': 'carillon-CISINFRASTRUCTURE',
    '1.3.6.1.4.1.25054.3.1.2': 'carillon-CISINFRASTRUCTURE-256',
    '1.3.6.1.4.1.25054.3.1.3': 'carillon-basicSoftware',
    '1.3.6.1.4.1.25054.3.1.4': 'carillon-basicHardware',
    '1.3.6.1.4.1.25054.3.1.5': 'carillon-mediumSoftwareCBP',
    '1.3.6.1.4.1.25054.3.1.6': 'carillon-mediumHardwareCBP',
    '1.3.6.1.4.1.25054.3.1.7': 'carillon-mediumSoftware',
    '1.3.6.1.4.1.25054.3.1.8': 'carillon-mediumHardware',
    '1.3.6.1.4.1.25054.3.1.9': 'carillon-basicSoftware-256',
    '1.3.6.1.4.1.25054.3.1.10': 'carillon-basicHardware-256',
    '1.3.6.1.4.1.25054.3.1.11': 'carillon-mediumSoftware-256',
    '1.3.6.1.4.1.25054.3.1.12': 'carillon-mediumHardware-256',
    '1.3.6.1.4.1.25054.3.1.13': 'carillon-mediumDeviceSoftware-256',
    '1.3.6.1.4.1.25054.3.1.14': 'carillon-mediumDeviceHardware-256',
    '1.3.6.1.4.1.25054.3.1.20': 'carillon-iceCAPHardware',
    '1.3.6.1.4.1.25054.3.1.21': 'carillon-iceCAPCardAuth',
    '1.3.6.1.4.1.25054.3.1.22': 'carillon-iceCAPContentSigning',
    '1.3.6.1.4.1.25054.3.1.30': 'carillon-mediumSoftwareCBP-256',
    '1.3.6.1.4.1.25054.3.1.31': 'carillon-mediumHardwareCBP-256',

    '1.3.6.1.4.1.45606.3.1.1': 'carillon-fedSvcs-CFSINFRASTRUCTURE',
    '1.3.6.1.4.1.45606.3.1.2': 'carillon-fedSvcs-CFSINFRASTRUCTURE-256',
    '1.3.6.1.4.1.45606.3.1.3': 'carillon-fedSvcs-basicSoftware',
    '1.3.6.1.4.1.45606.3.1.4': 'carillon-fedSvcs-basicHardware',
    '1.3.6.1.4.1.45606.3.1.7': 'carillon-fedSvcs-mediumSoftware',
    '1.3.6.1.4.1.45606.3.1.8': 'carillon-fedSvcs-mediumHardware',
    '1.3.6.1.4.1.45606.3.1.9': 'carillon-fedSvcs-basicSoftware-256',
    '1.3.6.1.4.1.45606.3.1.10': 'carillon-fedSvcs-basicHardware-256',
    '1.3.6.1.4.1.45606.3.1.11': 'carillon-fedSvcs-mediumSoftware-256',
    '1.3.6.1.4.1.45606.3.1.12': 'carillon-fedSvcs-mediumHardware-256',
    '1.3.6.1.4.1.45606.3.1.13': 'carillon-fedSvcs-mediumDeviceSoftware-256',
    '1.3.6.1.4.1.45606.3.1.14': 'carillon-fedSvcs-mediumDeviceHardware-256',
    '1.3.6.1.4.1.45606.3.1.20': 'carillon-fedSvcs-AIVHardware',
    '1.3.6.1.4.1.45606.3.1.21': 'carillon-fedSvcs-AIVCardAuth',
    '1.3.6.1.4.1.45606.3.1.22': 'carillon-fedSvcs-AIVContentSigning',

    '1.3.6.1.4.1.103.100.1.1.3.1': 'lockheed-mediumHardware-SHA1',
    '1.3.6.1.4.1.103.100.1.1.3.2': 'lockheed-mediumSoftware-SHA1',
    '1.3.6.1.4.1.103.100.1.1.3.3': 'lockheed-mediumHardware-SHA2',
    '1.3.6.1.4.1.103.100.1.1.3.4': 'lockheed-mediumSoftware-SHA2',
    '1.3.6.1.4.1.103.100.1.1.3.5': 'lockheed-mediumDerived',
    '1.3.6.1.4.1.103.100.1.1.3.6': 'lockheed-mediumDevice',

    '2.16.528.1.1003.1.2.5.1': 'netherlands-mod-Authenticity',
    '2.16.528.1.1003.1.2.5.2': 'netherlands-mod-Signature',
    '2.16.528.1.1003.1.2.5.3': 'netherlands-mod-Confidentiality',

    '1.3.6.1.4.1.16334.509.2.6': 'northrop-mediumHardware-SHA1',
    '1.3.6.1.4.1.16334.509.2.5': 'northrop-mediumSoftware-SHA1',
    '1.3.6.1.4.1.16334.509.2.8': 'northrop-mediumHardware-SHA2',
    '1.3.6.1.4.1.16334.509.2.7': 'northrop-mediumSoftware-SHA2',
    '1.3.6.1.4.1.16334.509.2.9': 'northrop-pivi-hardware',
    '1.3.6.1.4.1.16334.509.2.10': 'northrop-pivi-cardAuth',
    '1.3.6.1.4.1.16334.509.2.11': 'northrop-pivi-contentSigning',

    '1.3.6.1.4.1.1569.10.1.2': 'raytheon-mediumHardware',
    '1.3.6.1.4.1.1569.10.1.3': 'raytheon-mediumSoftware',
    '1.3.6.1.4.1.1569.10.1.4': 'raytheon-mediumCBPHardware',
    '1.3.6.1.4.1.1569.10.1.5': 'raytheon-mediumCBPSoftware',
    '1.3.6.1.4.1.1569.10.1.1': 'raytheon-high',
    '1.3.6.1.4.1.1569.10.1.9': 'raytheon-medium-device-Software',
    '1.3.6.1.4.1.1569.10.1.8': 'raytheon-medium-device-Hardware',
    '1.3.6.1.4.1.1569.10.1.12': 'raytheon-SHA2-mediumHardware',
    '1.3.6.1.4.1.1569.10.1.13': 'raytheon-SHA2-mediumSoftware',
    '1.3.6.1.4.1.1569.10.1.14': 'raytheon-SHA2-mediumCBPHardware',
    '1.3.6.1.4.1.1569.10.1.15': 'raytheon-SHA2-mediumCBPSoftware',
    '1.3.6.1.4.1.1569.10.1.19': 'raytheon-SHA2-medium-device-Software',
    '1.3.6.1.4.1.1569.10.1.18': 'raytheon-SHA2-medium-device-Hardware',
    '1.3.6.1.4.1.1569.10.1.11': 'raytheon-SHA2-high',

    '2.16.840.1.101.2.1.11.10': 'id-US-dod-PIV-Auth',
    '2.16.840.1.101.2.1.11.17': 'id-US-dod-mediumNPE',
    '2.16.840.1.101.2.1.11.18': 'id-US-dod-medium-2048',
    '2.16.840.1.101.2.1.11.19': 'id-US-dod-mediumHardware-2048',
    '2.16.840.1.101.2.1.11.2': 'id-US-dod-basic',
    '2.16.840.1.101.2.1.11.20': 'id-US-dod-PIV-Auth-2048',
    '2.16.840.1.101.2.1.11.31': 'id-US-dod-peerInterop',
    '2.16.840.1.101.2.1.11.32': 'id-US-dod-S-InteropHardware',
    '2.16.840.1.101.2.1.11.33': 'id-US-dod-S-InteropSoftware',
    '2.16.840.1.101.2.1.11.34': 'id-US-dod-S-InteropDevice',
    '2.16.840.1.101.2.1.11.36': 'id-US-dod-mediumNPE-112',
    '2.16.840.1.101.2.1.11.37': 'id-US-dod-mediumNPE-128',
    '2.16.840.1.101.2.1.11.38': 'id-US-dod-mediumNPE-192',
    '2.16.840.1.101.2.1.11.39': 'id-US-dod-medium-112',
    '2.16.840.1.101.2.1.11.4': 'id-US-dod-FORTEZZA',
    '2.16.840.1.101.2.1.11.40': 'id-US-dod-medium-128',
    '2.16.840.1.101.2.1.11.41': 'id-US-dod-medium-192',
    '2.16.840.1.101.2.1.11.42': 'id-US-dod-mediumHardware-112',
    '2.16.840.1.101.2.1.11.43': 'id-US-dod-mediumHardware-128',
    '2.16.840.1.101.2.1.11.44': 'id-US-dod- mediumHardware-192',
    '2.16.840.1.101.2.1.11.5': 'id-US-dod-medium',
    '2.16.840.1.101.2.1.11.6': 'id-US-dod-type1',
    '2.16.840.1.101.2.1.11.9': 'id-US-dod-mediumHardware',

    '1.3.6.1.4.1.49758.1.1.1.1': 'nextgenid-lowSoftware',
    '1.3.6.1.4.1.49758.1.1.1.2': 'nextgenid-lowHardware',
    '1.3.6.1.4.1.49758.1.1.1.3': 'nextgenid-mediumSoftware',
    '1.3.6.1.4.1.49758.1.1.1.4': 'nextgenid-mediumHardware',
    '1.3.6.1.4.1.49758.1.1.1.5': 'nextgenid-mediumCBPSoftware',
    '1.3.6.1.4.1.49758.1.1.1.6': 'nextgenid-mediumCBPHardware',
    '1.3.6.1.4.1.49758.1.1.1.7': 'nextgenid-IceCAP-hardware',
    '1.3.6.1.4.1.49758.1.1.1.8': 'nextgenid-IceCAP-cardAuth',
    '1.3.6.1.4.1.49758.1.1.1.9': 'nextgenid-IceCAP-contentSigning',
    '1.3.6.1.4.1.49758.1.1.1.23': 'nextgenid-medium-device-software',
    '1.3.6.1.4.1.49758.1.1.1.24': 'nextgenid-medium-device-hardware',

    '1.3.6.1.4.1.49507.1.1.1': 'airCanada-?? Not in CP ??',
    '1.3.6.1.4.1.49507.1.1.9': 'airCanada-basicSoftware-256',
    '1.3.6.1.4.1.49507.1.1.10': 'airCanada-basicHardware-256',
    '1.3.6.1.4.1.49507.1.1.11': 'airCanada-mediumSoftware-256',
    '1.3.6.1.4.1.49507.1.1.12': 'airCanada-mediumHardware-256',
    '1.3.6.1.4.1.49507.1.1.13': 'airCanada-mediumDeviceSoftware-256',
    '1.3.6.1.4.1.49507.1.1.14': 'airCanada-mediumDeviceHardware-256',
    '1.3.6.1.4.1.49507.1.2.1': 'airCanada-begss',
    '1.3.6.1.4.1.49507.1.3.1': 'airCanada-eegs',

    '1.3.6.1.4.1.311.21.30': 'microsoft-tpm-ekverifykey',
    '1.3.6.1.4.1.311.21.31': 'microsoft-tpm-ekverifycert',
    '1.3.6.1.4.1.311.21.32': 'microsoft-tpm-ekverifycreds',

    '1.3.6.1.4.1.23165.1.1': 'SAFE Basic',
    '1.3.6.1.4.1.23165.1.2': 'SAFE Medium Software',
    '1.3.6.1.4.1.23165.1.3': 'SAFE Medium Hardware',
}