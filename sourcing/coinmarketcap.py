from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import json

def btc():
    # data = requests.get("https://coinmarketcap.com/currencies/bitcoin/historical-data/")
    driver = webdriver.Chrome()
    driver.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/')
    data = driver.page_source
    soup = BeautifulSoup(data, "html.parser")
    #prices = soup.find_all('table', class_ = "h7vnx2-2 hLKazY cmc-table  ")
    #print(prices)
    for tag in soup.find_all("div"):
        try:
            if "sc-16r8icm-0" in tag["class"][0] or "jKrmxw" in tag["class"][1] or "container" in tag["class"][2]:
                print(tag.text)
        except:
            continue
    driver.close()
    return None

btc()

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/