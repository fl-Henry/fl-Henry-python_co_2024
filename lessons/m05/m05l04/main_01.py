from google.oauth2 import service_account
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "***************"
SAMPLE_RANGE_NAME = "Sheet1!A1:B10"

# Load service account credentials
credentials = service_account.Credentials.from_service_account_file('credentials.json')

# Build the service
sheets_service = build('sheets', 'v4', credentials=credentials)

values = [
    ["Anna", 22],
    ["Tom", 32]
]
body = {
    'values': values
}
result = sheets_service.spreadsheets().values().append(
    spreadsheetId=SAMPLE_SPREADSHEET_ID,
    range="Sheet1!A1",  # Вставка в конец данных
    valueInputOption="RAW",
    body=body
).execute()