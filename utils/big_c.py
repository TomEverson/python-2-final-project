from requests.cookies import RequestsCookieJar
import requests
from bs4 import BeautifulSoup
from utils import write_to_csv
import re


class Big_C:
    def __init__(self):
        self.url = 'https://www.bigc.co.th/en/search?q='
        self.headers = {
            'Accept-Language': 'en-US,en;q=0.9'
        }
        pass

    def get_price_and_product_title_from_big_c(self, product_code: str):
        url = self.url + product_code
        headers = self.headers
        jar = RequestsCookieJar()
        jar.set('language', 'en', domain="www.bigc.co.th", path="/")

        rawHTML = requests.get(url, headers, cookies=jar)

        soup = BeautifulSoup(rawHTML.text, 'html.parser')

        title_element = soup.find("div", class_='productCard_title__f1ohZ')
        baht_element = soup.find('div', class_='productCard_price__9T3J8')

        # Extract the text (currency symbol in this case)
        price_text = baht_element.getText(strip=True)
        product_title = title_element.get_text()

        price_value = re.findall(r'\d+\.\d+', price_text)

        # Get the first match if available
        price_value = price_value[0] if price_value else None

        write_to_csv({"Title": product_title, "Value": price_value})

        return f"{product_title} : ฿{price_value}"
