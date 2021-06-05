import requests
from bs4 import BeautifulSoup


def StockPrice(Symbol):
    URL = f"https://finance.yahoo.com/quote/{Symbol}?p={Symbol}&.tsrc=fin-srch"
    page = requests.get(URL)

    # Grabs the whole webpage's html
    soup = BeautifulSoup(page.content, 'html.parser')

    # Searches through whole webpage for the price <div>
    results = soup.find(id="quote-header-info")

    # Grabs price element and converts it into plane text
    price = results.find(
        'span', class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")

    price = price.text

    print(price)
