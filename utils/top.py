import requests
from bs4 import BeautifulSoup
from csv import DictWriter
from types import SimpleNamespace
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from utils import write_to_csv


chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome(options=chrome_options)


def get_price_and_product_title_from_top(product_code: str):

    # Open the website
    driver.get("https://www.tops.co.th/en/search/" + product_code)

    # Wait for the results to load
    time.sleep(0.5)

    # Click on the first link in the search results
    first_result = driver.find_element(
        By.CLASS_NAME, 'product-item-inner-wrap')
    first_result.click()

    url = driver.current_url

    driver.quit

    rawHTML = requests.get(url).text

    soup = BeautifulSoup(rawHTML, 'html.parser')

    pulledData = soup.find('script', id='meta-schema').get_text()

    x = json.loads(pulledData, object_hook=lambda d: SimpleNamespace(**d))
    productName = x.name
    productPrice = x.offers.price

    print(x)

    write_to_csv({"Title": productName, "Value": productPrice})

    return f"{productName} : ฿{productPrice}"
