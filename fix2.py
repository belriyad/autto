from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def main2(full_url):
    print("Processing", full_url)
    driver = webdriver.Remote(
    command_executor='http://192.168.1.252:4444/wd/hub',
    options=webdriver.ChromeOptions()
    )

    driver.get(full_url)
    price = driver.find_element(By.CSS_SELECTOR, ".statsValue").text
    print(price)
    driver.quit()
    return None