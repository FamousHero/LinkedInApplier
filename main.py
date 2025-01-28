from dotenv import load_dotenv

from selenium import webdriver

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

import time
import os
from pathlib import Path

debugging = True
load_dotenv()

USER_EMAIL=os.getenv("USER_EMAIL")
USER_PASSWORD=os.getenv("USER_PASSWORD")

def sign_in(driver):
    fill_input_by_id(driver, "username", USER_EMAIL)
    fill_input_by_id(driver, "password", USER_PASSWORD)
    time.sleep(2)
    sign_in_btn = driver.find_element(By.CSS_SELECTOR, "[aria-label=\"Sign in\"]")
    sign_in_btn.click()

def fill_input_by_id(driver, id, input_text):
    element = driver.find_element(By.ID, id)
    element.send_keys(input_text)


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get('https://www.linkedin.com/login')
sign_in(chrome_driver)
time.sleep(2)
