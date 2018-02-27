def getSheetId(module):
    sheetIdDictionary = {
        # real 'audit-management': '19lI5XuNerr5Bw01CpAR0D7RoDtEIPPB9P7Sn6RES-Qc',1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c
        'audit-management': '19lI5XuNerr5Bw01CpAR0D7RoDtEIPPB9P7Sn6RES-Qc',
        'auth-service': '1-6m7IE-gR1LnJcXxjl3WeEl_2btNG3-VsWe5rqNsivc',
        'bidding-management': '1GG5m_q9TWZ3RO9We4KjAVAZym1KbfNDBv-UW8VgzCy0',
        'bidding-tool': '1nVLBJ-msBIE_JyzOFw-mjT5Wm6CZcx8bIZn1qAJise8',
        'currency-exchange': '1xu3rAB_60N_KNQogQM9maD-mNPbgYfOqy-MDYXkwpRA',
        'currency-exchange-api': '1tCUAt0QL5RftAH6Fwb_NEUskd9gg_m6JvceiA-hNQ5k',
        'feature-engine': '1gD55GGgBItzzwmDkU0nB_O97H_xF6fWcv0q4BV_o_z0',
        'membership': '1wjG6SdEshl903UxrowV8yj3uPWJKA7cT_NWpyeIo5pU',
        'ml-model-evaluator': '1hmzKGP-pdGX2wOTFDqxQXeOZMA2ThaW60H9742zj5cw',
        'ml-model-evaluator-api': '1Wuf1zlWbbkyAFaEH4QzDhgnbhxz6fMzfFK0SBcyDsAs',
        'pim-api': '1fgPn7fpRE0VfVlgi9aADwdObItXCfvcziiranQLlxiM',
        'pricing-engine': '1rLFLUwgxeBFZ-T_POZl6jdiuoNRedaZ_bKe9b9BM1WA',
        'pricing-engine-api': '1fHKeUXv11Rr24gvnvZOCQH2I8I1uuCQeKTP2dJQ-B94',
        'pricing-management': '1nSv2AtHVZFVDx6jdVoAbMPrB5t3qNujENe0HG1eb5to'}
    return sheetIdDictionary[module]


def getRangeName(layer, month):
    rangeName = {1: month + '!L1',
                 2: month + '!N1',
                 3: month + '!P1',
                 4: month + '!R1',
                 5: month + '!T1'}

    return rangeName[layer]


def getRangeUnit(layer, month):
    rangeUnit = {1: month + '!L3:M4',
                 2: month + '!N3:O4',
                 3: month + '!P3:Q4',
                 4: month + '!R3:S4',
                 5: month + '!T3:U4'}
    return rangeUnit[layer]


def getRangeMutation(layer, month):
    rangeMutation = {1: month + '!L8:M14',
                     2: month + '!N8:O14',
                     3: month + '!P8:Q14',
                     4: month + '!R8:S14',
                     5: month + '!T8:U14'}

    return rangeMutation[layer]


def getMonth(month):
    months = {'01': 'Jan',
              '02': 'Feb',
              '03': 'Mar',
              '04': 'Apr',
              '05': 'May',
              '06': 'Jun',
              '07': 'Jul',
              '08': 'Aug',
              '09': 'Sep',
              '10': 'Out',
              '11': 'Nov',
              '12': 'Dec'}
    return months[month]
