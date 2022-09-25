from bs4 import BeautifulSoup
from lxml import etree
import requests

URL = "https://www.x-rates.com/table/?from=USD&amount=1"
HEADERS = {"User-Agent": "Mozilla/5.0"}
XPATHS = [
    'EUR://*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[1]/td[2]/a',
    'GBP://*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[2]/td[2]/a',
    'INR://*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[3]/td[2]/a',
    'AUD://*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[4]/td[2]/a',
    'CAD://*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[5]/td[2]/a',
    'SGD://*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[6]/td[2]/a',
    'CHF://*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[7]/td[2]/a',
    'MYR://*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[8]/td[2]/a',
    'JPY://*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[9]/td[2]/a',
    'CNY://*[@id="content"]/div[1]/div/div[1]/div[1]/table[1]/tbody/tr[10]/td[2]/a',
    'DKK://*[@id="content"]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr[14]/td[2]/a',
]

def fetch():
    currency_rates = []
    fetch_webpage = requests.get(URL, headers=HEADERS)
    bsoup = BeautifulSoup(fetch_webpage.content, "html.parser")
    elec_tree = etree.HTML(str(bsoup))
    xpaths_len = len(XPATHS)
    for i in range(xpaths_len):
        currency_name = XPATHS[i].split(":")[0]
        currency_xpath = XPATHS[i].split(":")[1]
        currency_rate = elec_tree.xpath(currency_xpath)[0].text
        currency_rates.append(f"{currency_name}:{currency_rate}")
    return currency_rates
