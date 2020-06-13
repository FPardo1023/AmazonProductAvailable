import bs4
from bs4 import BeautifulSoup
import requests

def check_availability(URL_py, user_agent_py):
    URL = URL_py

    headers = {"User-Agent": user_agent_py}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    product = soup.find(id="productTitle").get_text()
    availability = soup.find(id="availability").get_text()

    print(product.strip())
    if "Currently unavailable." in availability:
        print("Currently Unavailable!")
    else:
        print(availability.strip())

check_availability('https://www.amazon.ca/dp/B07YGZL8XF/?coliid=I18V4B7R8TULPQ&colid=3CBNXXUKOYLM5&ref_=lv_ov_lig_dp_it&th=1', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')

