from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep, time

# Initialize the Chrome driver
def main2(full_url):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the webpage
    driver.get(full_url)

    # Wait for the page to load
    time.sleep(5)

    # Scrape the property price
    price = driver.find_element(By.CSS_SELECTOR, ".statsValue").text

    # Scrape the address
    address = driver.find_element(By.CSS_SELECTOR, ".street-address").text

    # Scrape the number of bedrooms
    bedrooms = driver.find_element(By.XPATH, "//div[@data-rf-test-id='abp-beds']/div[1]").text

    # Scrape the number of bathrooms
    bathrooms = driver.find_element(By.XPATH, "//div[@data-rf-test-id='abp-baths']/div[1]").text

    # Print the results
    print(f"Price: {price}")
    print(f"Address: {address}")
    print(f"Bedrooms: {bedrooms}")
    print(f"Bathrooms: {bathrooms}")

    # Close the driver
    driver.quit()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, "", "", "", "", price, bedrooms, bathrooms, "area", "description", address, "other_info", "image", full_url]
    return row