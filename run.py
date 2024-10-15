#connect the following URL and extract all links from the page
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#from fp.fp import FreeProxy
import random
from time import sleep, time
import pip._vendor.requests as requests
from bs4 import BeautifulSoup
useragentarray = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.48 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
]
proxy_list = [
    "http://206.42.19.56:8080",
    "http://79.110.201.235:8081",
    "http://79.175.138.142:3128",
    "http://51.89.134.65:80",
    "http://190.94.212.244:999",
    "http://176.113.73.102:3128",
    "http://132.255.223.1:9500",
    "http://87.247.186.40:1081",
    "http://146.59.243.214:80",
    "http://5.104.174.199:23500",
    "http://103.30.43.183:3128",
    "http://164.92.164.95:80",
    "http://103.82.233.2:1089",
    "http://121.13.229.211:61401",
    "http://67.43.227.226:6847",
    "http://165.16.27.105:1976",
    "http://168.126.68.80:80",
    "http://191.7.8.149:80",
    "http://79.110.200.148:8081"
]
# Function to get a random user agent
def get_random_user_agent():
    return random.choice(useragentarray)

# Function to get a random proxy
def get_random_proxy():
    #return ""# free_proxy.get()
    return random.choice(proxy_list)

def fetch_url(url):
    headers = {'User-Agent': get_random_user_agent()}
    #proxy = {'http': get_random_proxy(), 'https': get_random_proxy()}
    proxy=get_random_proxy()
    proxies = {'http': proxy, 'https': proxy}
    proxy=proxies
    try:
        #response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
        #response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        response = requests.get(url,   timeout=10)
        #print(proxy)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
def main (url):
    html_content = fetch_url(url)
    print (html_content)
    if html_content  :
        soup = BeautifulSoup(html_content, 'html.parser')
        # Process the soup object as needed
        
        print(soup.title.text)
        price_element = soup.find('div', {'class': 'statsValue'})
        price = price_element.text.strip() if price_element else 'N/A'  # Price
        
        bedrooms_element = soup.find('div', {'data-rf-test-id': 'abp-beds'})
        bedrooms = bedrooms_element.text.strip() if bedrooms_element else 'N/A'  # Bedroom(s)
        
        bathrooms_element = soup.find('div', {'data-rf-test-id': 'abp-baths'})
        bathrooms = bathrooms_element.text.strip() if bathrooms_element else 'N/A'  # Bathroom(s)
        
        area_element = soup.find('div', {'data-rf-test-id': 'abp-sqFt'})
        area = area_element.text.strip() if area_element else 'N/A'  # Area (sqft)
        
        description_element = soup.find('div', {"data-rf-test-id" :"mhi-housesummary"})
        description = description_element.text.strip() if description_element else 'N/A'  # Description
        
        address_element = soup.find('div', {'class': 'street-address'})
        address = address_element.text.strip() if address_element else 'N/A'  # Address
        
        other_info_element = soup.find('div', {'class': 'keyDetailsList'})
        other_info = other_info_element.text.strip() if other_info_element else 'N/A'  # Other info
        
        # Find the image element with class 'landscape'
        image_element = soup.find('img', {'class': 'landscape'})
        # Extract the 'src' attribute if the image element is found
        image = image_element['src'] if image_element else 'N/A'  # Image link
        
        detail_link = url  # Detail link

        # Display results
        print(f"Price: {price}") 
        print(f"Bedrooms: {bedrooms}")
        print(f"Bathrooms: {bathrooms}")
        print(f"Area (sqft): {area}")
        print(f"Description: {description}")
        print(f"Address: {address}")
        print(f"Other info: {other_info}")
        print(f"Image link: {image}")
        print(f"Detail link: {detail_link}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        from datetime import datetime
        

        
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create the row with the timestamp and other data
        row = [timestamp, "", "", "", "", price, bedrooms, bathrooms, area, description, address, other_info, image, detail_link]
        
        # Check if the row already exists based on detail_link

        print(f"Row added: {row}")
        # Check if any of the required values are "N/A"
        # if any(value == 'N/A' for value in [price, bedrooms, bathrooms, area, description, address, other_info, image]):
        print(f"Skipping row due to missing data: {row}")
        #sheet.append_row(row)
        #    continue
        #if all([price, bedrooms, bathrooms, area, description, address, other_info, image, detail_link]):
            
        #else:
        #    print(f"Skipping row due to missing data: {row}")
        #sheet.append_row(row)
        row = [timestamp, "", "", "", "", price, bedrooms, bathrooms, area, description, address, other_info, image, detail_link]
    else:
        row = None
        
        # print(f"Failed to retrieve content from {full_url} "+ random.choice(useragentarray) + " " + proxy)
    return row