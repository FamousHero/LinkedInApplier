from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import Chrome
from pathlib import Path
import undetected_chromedriver as uc
import time
import os

debugging = True
load_dotenv()

USER_EMAIL=os.getenv("USER_EMAIL")
USER_PASSWORD=os.getenv("USER_PASSWORD")



driver = uc.Chrome()

driver.get('https://www.google.com/')

time.sleep(5)
