import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('US Legislators 2017').sheet1

values = sheet.get_all_records()
pprint(values)
