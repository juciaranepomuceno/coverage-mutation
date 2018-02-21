from __future__ import print_function
import httplib2
from apiclient import discovery
import getCredentials


def openSheet():
    credentials = getCredentials.get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                          discoveryServiceUrl=discoveryUrl)
    return service


def updateSheetMutation(layer, totalMutants, \
                        totalMutantsKilled, \
                        mutantReturnValsMutator, \
                        mutantReturnValsMutatorKilled, \
                        mutantNegateConditionalsMutator, \
                        mutantNegateConditionalsMutatorKilled, \
                        mutantVoidMethodCallMutator, \
                        mutantVoidMethodCallMutatorKilled, \
                        mutantConditionalsBoundaryMutator, \
                        mutantConditionalsBoundaryMutatorKilled, \
                        mutantIncrementsMutator, \
                        mutantIncrementsMutatorKilled, \
                        mutantMathMutator, \
                        mutantMathMutatorKilled):

    service = openSheet()

    valuesMutation = [[totalMutants, totalMutantsKilled],
                      [mutantReturnValsMutator, mutantReturnValsMutatorKilled],
                      [mutantNegateConditionalsMutator, mutantNegateConditionalsMutatorKilled],
                      [mutantVoidMethodCallMutator, mutantVoidMethodCallMutatorKilled],
                      [mutantConditionalsBoundaryMutator, mutantConditionalsBoundaryMutatorKilled],
                      [mutantIncrementsMutator, mutantIncrementsMutatorKilled],
                      [mutantMathMutator, mutantMathMutatorKilled],
                      ]

    bodyMutation = {
        'values': valuesMutation
    }

    rangeMutation = {1:'Jan!L8:M14',
                     2:'Jan!N8:O14',
                     3:'Jan!P8:Q14',
                     4:'Jan!R8:S14',
                     5:'Jan!T8:U14'}

    service.spreadsheets().values().update(
        spreadsheetId='1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c', range=rangeMutation,
        valueInputOption='USER_ENTERED', body=bodyMutation).execute()

def updateSheetUnit(layer,
                    total_lines_covered,total_lines_total,
                    total_branch_covered, total_branch_total):

    service = openSheet()

    valuesUnit = [[total_lines_covered, total_lines_total],[total_branch_covered, total_branch_total]]

    bodyUnit = {
        'values': valuesUnit
    }

    rangeUnit = {    1:'Jan!L3:M4',
                     2:'Jan!N3:O4',
                     3:'Jan!P3:Q4',
                     4:'Jan!R3:S4',
                     5:'Jan!T3:U4'}

    service.spreadsheets().values().update(
        spreadsheetId='1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c', range=rangeUnit,
        valueInputOption='USER_ENTERED', body=bodyUnit).execute()


def updateLayersName(layerName, layer):

    service = openSheet()
    valuesName = [[layerName]]
    bodyName = {
    'values': valuesName
    }

    rangeName = {    1:'Jan!L1',
                     2:'Jan!N1',
                     3:'Jan!P1',
                     4:'Jan!R1',
                     5:'Jan!T1'}


    service.spreadsheets().values().update(
        spreadsheetId='1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c', range=rangeName[layer],
        valueInputOption='USER_ENTERED', body=bodyName).execute()


