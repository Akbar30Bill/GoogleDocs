def get_worksheet(sheets_url, keyfile):
  import gspread
  from oauth2client.service_account import ServiceAccountCredentials

  scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

  credentials = ServiceAccountCredentials.from_json_keyfile_name(keyfile, scope)

  sheets_url = 'https://docs.google.com/spreadsheets/d/13EcQlxTGkirllkSx60CbZbjCNDjgQEkWi50LZVftBcM/'

  gc = gspread.authorize(credentials)

  wks = gc.open_by_url(sheets_url)
  return wks