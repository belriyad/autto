from datetime import datetime
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


import time
import argparse
from time import sleep, time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a URL.')
    parser.add_argument('--url', required=True, help='The URL to process')
    args = parser.parse_args()
    full_url = args.url

# Initialize the Chrome driver
def main2(full_url):
    max_retries = 10
    retry_delay = 5
    selenium_host="http://192.168.1.252:4444/wd/hub"
    driver = webdriver.Remote(
    command_executor=selenium_host,
    options=webdriver.ChromeOptions()
)

    
    for i in range(max_retries):
        try:
            response = requests.get(selenium_host)
            if response.status_code == 200:
                break
        except requests.ConnectionError:
            pass
        print(f"Waiting for Selenium container... ({i+1}/{max_retries})")
        time.sleep(retry_delay)
    else:
        raise Exception("Selenium container not ready after max retries")

    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    #options.add_argument('--ignore-certificate-errors')
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    #driver = webdriver.Chrome ()
    # Open the webpage
    driver.get(full_url)

    # Wait for the page to load
    sleep(5)

    # Scrape the property price
    price = driver.find_element(By.CSS_SELECTOR, ".statsValue").text

    # Scrape the address
    address = driver.find_element(By.CSS_SELECTOR, ".street-address").text + " "+ driver.find_element(By.CSS_SELECTOR, "#content > div.detailsContent > div.theRailSection > div.alongTheRail > div:nth-child(1) > section > div > div > div > div.flex-1 > div.AddressBannerV2.desktop > div > div > div > header > div > h1 > div.dp-subtext.bp-cityStateZip").text

    # Scrape the number of bedrooms
    bedrooms = driver.find_element(By.XPATH, "//div[@data-rf-test-id='abp-beds']/div[1]").text

    # Scrape the number of bathrooms
    bathrooms = driver.find_element(By.XPATH, "//div[@data-rf-test-id='abp-baths']/div[1]").text

    image= driver.find_element(By.CSS_SELECTOR, "#MBImage0 > img").get_attribute("src")

    description = driver.find_element(By.CSS_SELECTOR, "#marketing-remarks-scroll > p > span").text

    area = driver.find_element(By.CSS_SELECTOR, "#content > div.detailsContent > div.theRailSection > div.alongTheRail > div:nth-child(1) > section > div > div > div > div.flex-1 > div.AddressBannerV2.desktop > div > div > div > div > div.stat-block.sqft-section > span").text

    # Print the results
    print(f"Price: {price}")
    print(f"Address: {address}")
    print(f"Bedrooms: {bedrooms}")
    print(f"Bathrooms: {bathrooms}")
    print(f"Area: {area}")
    print(f"Description: {description}")
    print(f"Image: {image}")
    print(f"URL: {full_url}")

    # Close the driver
    driver.quit()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, "", "", "", "", price, bedrooms, bathrooms, area, description, address, "", image, full_url]
    return row