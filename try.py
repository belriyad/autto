from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Remote(
    command_executor='http://192.168.1.252:4444/wd/hub',
    options=webdriver.ChromeOptions()
)

driver.get('https://www.redfin.com/WA/Bellevue/14650-NE-50th-Pl-98007/unit-H3/home/10576')
price = driver.find_element(By.CSS_SELECTOR, ".statsValue").text
print(price)