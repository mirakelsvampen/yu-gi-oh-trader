from collections import defaultdict
from bs4 import BeautifulSoup as bs4
import requests

class Card(object):
    # Not in use yet
    def __init__(self):
        self.name = ""
        self.rarity = ""
        self.number = 0
        self.available = 0
        self.from_price = 0.0
        self.max_price = 0.0

    @property
    def inspect(self):
        return {
            "name": self.name,
            "rarity": self.rarity,
            "number": self.number,
            "available": self.available,
            "from_price": self.from_price,
            "max_price": self.max_price
        }

class CardMarket(object):
    def __init__(self, base_url: str, lang:str, market:str):
        self.base_url = f"{base_url}/{lang}/{market}"
        self.headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.paths = {
            "Products": [
                "Singles",
                # "Boosters",
                # "Booster-Boxes",
                # "Lots-Collections",
                # "Sealed-Products"
            ]
        }

    @property
    def products(self):
        products = defaultdict(list)
        for product in self.paths["Products"]:
            url = f"{self.base_url}/Products/{product}"
            response = requests.get(url=url, headers = self.headers)
            products[product].append(
                {
                    "status": response.status_code,
                    "content": bs4(response.content, 'html.parser')
                }
            )
        return products

    def pagination(self):
        for page in self.products:
            pagination_div = [''].find_all("div", {"id": "pagination"})
            print(pagination_div)
    
    
site = CardMarket(
    base_url="https://www.cardmarket.com",
    lang="en",
    market="YuGiOh",
)

print(site.pagination())