#connect the following URL and extract all links from the page
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#from fp.fp import FreeProxy
import random
from time import sleep, time
import pip._vendor.requests as requests
from bs4 import BeautifulSoup
from run import main
from fix import main2


def row_exists(sheet, detail_link):
    existing_rows = sheet.get_all_values()
    for row in existing_rows:
        if detail_link in row:
            return True
    return False

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
#sheet = client.open("zillow_listing").sheet2 # Open the Google Sheet
spreadsheet = client.open("zillow_listing") # Open the Google Sheet
sheet = spreadsheet.worksheet("Property list")

for row in sheet.get_all_records():
    print(row['Detail link'])
    #main(row['URL'])
    #sleep(10)


url = 'https://www.redfin.com/city/1387/WA/Bellevue'
#set browser to show as a chrome browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}  
#connect to the website
r = requests.get(url, headers=headers)
#r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
#define a new list 
links = []
for link in soup.find_all('a'):
    href = link.get('href')
    #only show urls in this format use regex and dont use string matching /WA/Bellevue/4519-Lake-Heights-St-98006/home/416494
    if href and "/home/" in href:
        #add the urls to the list
        full_url = "https://www.redfin.com" + href.replace(" ", "")

        links.append(full_url)
        #full_url = "https://www.redfin.com" + link.get('herf').replace(" ", "")
        #print (full_url)   
        
        if row_exists(sheet, full_url):
            print(f"Skipping {full_url}")
            
            
        else:
            print(f"Processing {full_url}")    
            try:
                row=main2(full_url)
                if row is not None:
                    sheet.append_row(row)
            except Exception as e:
                print(f"Failed to process {full_url}: {e}")
