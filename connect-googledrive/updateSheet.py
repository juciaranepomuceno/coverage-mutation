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
                        mutantConditionalsBoundaryMutatorKiller, \
                        mutantIncrementsMutator, \
                        mutantIncrementsMutatorKilled, \
                        mutantMathMutator, \
                        mutantMathMutatorKilled):

    service = openSheet()

    valuesMutation = [[totalMutants, totalMutantsKilled],
                      [mutantReturnValsMutator, mutantReturnValsMutatorKilled],
                      [mutantNegateConditionalsMutator, mutantNegateConditionalsMutatorKilled],
                      [mutantVoidMethodCallMutator, mutantVoidMethodCallMutatorKilled],
                      [mutantConditionalsBoundaryMutator, mutantConditionalsBoundaryMutatorKiller],
                      [mutantIncrementsMutator, mutantIncrementsMutatorKilled],
                      [mutantMathMutator, mutantMathMutatorKilled],
                      ]

    bodyMutation = {
        'values': valuesMutation
    }

    if layer == 1:
        rangeMutation = 'Jan!L8:M14'
    if layer == 2:
        rangeMutation = 'Jan!N8:O14'
    if layer == 3:
        rangeMutation = 'Jan!P8:Q14'
    if layer == 4:
        rangeMutation = 'Jan!R8:S14'
    if layer == 5:
        rangeMutation = 'Jan!T8:U14'

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

    if layer == 1:
        rangeUnit = 'Jan!L3:M4'
    if layer == 2:
        rangeUnit = 'Jan!N3:O4'
    if layer == 3:
        rangeUnit = 'Jan!P3:Q4'
    if layer == 4:
        rangeUnit = 'Jan!R3:S4'
    if layer == 5:
        rangeUnit = 'Jan!T3:U4'


    service.spreadsheets().values().update(
        spreadsheetId='1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c', range=rangeUnit,
        valueInputOption='USER_ENTERED', body=bodyUnit).execute()


def updateLayersName(layerName, layer):

    service = openSheet()
    valuesName = [[layerName]]
    bodyName = {
    'values': valuesName
    }

    if layer == 1:
        rangeName = 'Jan!L1'
    if layer == 2:
        rangeName = 'Jan!N1'
    if layer == 3:
        rangeName = 'Jan!P1'
    if layer == 4:
        rangeName = 'Jan!R1'
    if layer == 5:
        rangeName = 'Jan!T1'

    service.spreadsheets().values().update(
        spreadsheetId='1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c', range=rangeName,
        valueInputOption='USER_ENTERED', body=bodyName).execute()

if __name__ == '__main__':
    updateLayersName("teste",1)
