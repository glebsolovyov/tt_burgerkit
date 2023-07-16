import config

import httplib2

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'src/tt-burgerkit-2640a13317ce.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = build('sheets', 'v4', http=httpAuth)

spreadsheetId = config.SPREADSHEETID

results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                   ranges='A2:E2',
                                                   valueRenderOption='FORMATTED_VALUE',
                                                   dateTimeRenderOption='FORMATTED_STRING').execute()

def get_sheet_values():
    return results['valueRanges'][0]['values'][0]
