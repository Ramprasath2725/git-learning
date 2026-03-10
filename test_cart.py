from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
print("Google opened successfully")
print("abc")

time.sleep(3)
driver.quit()


