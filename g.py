import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)



spreadsheet_name = "zillow_listing"
try:
    spreadsheet = client.open(spreadsheet_name)
    print(f"Successfully opened the spreadsheet: {spreadsheet_name}")

    # List all sheets
    worksheets = spreadsheet.worksheets()
    print("List of sheets:")
    for sheet in worksheets:
        print(f"- {sheet.title}")

except gspread.exceptions.SpreadsheetNotFound:
    print(f"Spreadsheet '{spreadsheet_name}' not found. Please check the name and ensure the service account has access.")



spreadsheetsheet = client.open("zillow_listing") # Open the Google Sheet
sheet = spreadsheet.worksheet("Property list")


detail_link="https://www.redfin.com/WA/Bellevue/1011-148th-Pl-SE-98007/home/427101"


def row_exists(sheet, detail_link):
    existing_rows = sheet.get_all_values()
    for row in existing_rows:
        if detail_link in row:
            return True
    return False

print(row_exists(sheet, detail_link))
