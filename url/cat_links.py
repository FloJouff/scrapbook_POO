import requests
from bs4 import BeautifulSoup


def get_categories_links():
    main_url = "https://books.toscrape.com/index.html"
    main_page = requests.get(main_url)

    if main_page.status_code == 200:
        soup = BeautifulSoup(main_page.content, "html.parser")

    cats = soup.find("ul", class_="nav nav-list")

    links = cats.find_all("a")
    categories_url = []

    for link in links[1:]:
        categories_url.append(("https://books.toscrape.com/" + link["href"]))

    return categories_url
