import requests
from bs4 import BeautifulSoup


class Category:
    def __init__(self, cat_url):
        self.cat_url = cat_url
        self.books_url = []

    def get_books_url(self):
        # adresse de la catégorie à scraper:
        self.book_urls = []

        page = requests.get(self.cat_url)

        cat_soup = BeautifulSoup(page.content, "html.parser")

        articles = cat_soup.find_all("article", class_="product_pod")
        for article in articles:
            lien = article.find("a")["href"]
            chemin = lien.replace("../", "")

            book_url = "https://books.toscrape.com/catalogue/" + chemin

            self.book_urls.append(book_url)

        # nexts pages

        base_url = str(self.cat_url).split("index.html")
        next_element = cat_soup.find("li", class_="next")

        while next_element is not None:
            next_index_page = next_element.find("a", href=True)["href"]
            link = requests.get(str(base_url[0]) + next_index_page)

            soup = BeautifulSoup(link.text, "html.parser")

            articles = soup.find_all("article", class_="product_pod")

            for article in articles:
                lien = article.find("a")["href"]
                chemin = lien.replace("../", "")
                book_url = "https://books.toscrape.com/catalogue/" + chemin
                self.book_urls.append(book_url)
            next_element = soup.find("li", class_="next")

        return self.book_urls
