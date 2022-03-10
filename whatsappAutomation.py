import os
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:\Users\saura\Desktop"
driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")

driver.implicitly_wait(5)
try:
    destination = driver.find_element(By.XPATH, "//span[.='Contact Name']") #replace it with your contact name
    destination.click()
except:
    destination = driver.find_element(By.XPATH, "//span[.='Contact Name']") #replace it with your contact name
    destination.click()


msg_area = driver.find_element(By.CSS_SELECTOR, "[title*='Type a message']")
for i in range(20):
    msg_area.send_keys("Hi")
    msg_area.send_keys(Keys.RETURN)


