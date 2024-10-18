from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome ()
browser.get('http://www.google.com/')
