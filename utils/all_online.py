from requests.cookies import RequestsCookieJar
import requests
from bs4 import BeautifulSoup
from utils import write_to_csv
import re
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='th', target='en')


class All_Online:

    def __init__(self):
        self.url = 'https://www.allonline.7eleven.co.th/search/?q='
        self.headers = {
            'Accept-Language': 'en-US,en;q=0.9'
        }

    def get_price_and_product_title_from_7_11(self, product_code: str):
        url = self.url + product_code
        headers = self.headers
        # jar = RequestsCookieJar()
        # jar.set('language', 'en', domain="www.bigc.co.th", path="/")

        rawHTML = requests.get(url, headers)

        soup = BeautifulSoup(rawHTML.text, 'html.parser')

        price_element = soup.find("div", class_='price price-cls-mobile')
        baht_element = price_element.find('s').getText(strip=True)

        # Extract the text (currency symbol in this case)
        title_element = soup.find(
            "div", class_="item description item-description-cls-mobile").getText(strip=True)
        product_title = translator.translate(title_element)

        price_value = re.search(r'\d+', '฿ 170').group()

        # Get the first match if available
        price_value = price_value if price_value else None

        write_to_csv({"Title": product_title, "Value": price_value})

        return product_title, price_value
