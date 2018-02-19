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

    #spreadsheetId = '1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c'

def updateSheetMutation(layerName):
    credentials = getCredentials.get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    rangeMutation = 'Jan!L1'
    values = [[layerName]]

    body = {
        'values': values
    }

    result = service.spreadsheets().values().update(
        spreadsheetId='1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c', range=rangeMutation,
        valueInputOption='USER_ENTERED', body=body).execute()

    print('{0} cells updated.'.format(result.get('updatedCells')));

def updateSheetUnit():

    rangeUnit = 'Jan!L3:W4'

def updateLayersName(layerName, layer):

    credentials = getCredentials.get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    if layer == 1:
        rangeName = 'Jan!L1'
        values = [[layerName]]

        body = {
            'values': values
        }

        result = service.spreadsheets().values().update(
            spreadsheetId='1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c', range=rangeName,
            valueInputOption='USER_ENTERED', body=body).execute()

        print('{0} cells updated.'.format(result.get('updatedCells')));

    if layer == 2:
        rangeName = 'Jan!N1'
        values = [[layerName]]

        body = {
            'values': values
        }

        result = service.spreadsheets().values().update(
            spreadsheetId='1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c', range=rangeName,
            valueInputOption='USER_ENTERED', body=body).execute()

        print('{0} cells updated.'.format(result.get('updatedCells')));


    if layer == 3:
        rangeName = 'Jan!P1'
        values = [[layerName]]

        body = {
            'values': values
        }

        result = service.spreadsheets().values().update(
            spreadsheetId='1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c', range=rangeName,
            valueInputOption='USER_ENTERED', body=body).execute()

        print('{0} cells updated.'.format(result.get('updatedCells')));

    if layer == 4:
        rangeName = 'Jan!R1'
        values = [[layerName]]

        body = {
            'values': values
        }

        result = service.spreadsheets().values().update(
            spreadsheetId='1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c', range=rangeName,
            valueInputOption='USER_ENTERED', body=body).execute()

        print('{0} cells updated.'.format(result.get('updatedCells')));

    if layer == 5:
        rangeName = 'Jan!T1'
        values = [[layerName]]

        body = {
            'values': values
        }

        result = service.spreadsheets().values().update(
            spreadsheetId='1MYosSG79lF_hgVo4GbsJ9Uzo8RoNT5DA4ZefjVequ4c', range=rangeName,
            valueInputOption='USER_ENTERED', body=body).execute()

        print('{0} cells updated.'.format(result.get('updatedCells')));











if __name__ == '__main__':
    updateLayersName("teste",1)
