from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the webpage
driver.get("https://www.redfin.com/WA/Redmond/2345-W-Lake-Sammamish-Pkwy-NE-98052/home/22224726")

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