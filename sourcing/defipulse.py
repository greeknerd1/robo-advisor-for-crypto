from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import json

def func():
    driver = webdriver.Chrome(executable_path = 'C:/Users/User/chromedriver_win32\chromedriver.exe')
    driver.get('https://defipulse.com/')
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
    for tag in soup.find_all('div', class_ = "defi-market-data"):
        try:
            print(tag.text)
        except:
            continue
    driver.close()
    return None

func()