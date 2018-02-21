import httplib2
from apiclient import discovery

import dataMap
import getCredentials


def openSpreadSheet():
    credentials = getCredentials.get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    return service


def requestUpdate(thisRange, thisBody):
    thisSpreadsheetId = dataMap.getSheetId('audit-management')

    openSpreadSheet().spreadsheets().values().update(
        spreadsheetId=thisSpreadsheetId, range=thisRange,
        valueInputOption='USER_ENTERED', body=thisBody).execute()
