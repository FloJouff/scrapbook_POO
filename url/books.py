import requests
from bs4 import BeautifulSoup
import os.path
import urllib.request


class Book:
    def __init__(self, url):
        self.url = url
        self.book_data = {}

    def scrap_book(self):
        book_page = requests.get(self.url)

        soup = BeautifulSoup(book_page.content, "html.parser")
        titre = soup.find("h1")
        title = titre.string
        title = title.replace(":", "")
        title = title.replace("/", "")
        title = title.replace("\\", "")
        title = title.replace("'", "")
        title = title.replace('"', "")
        title = title.replace("*", "")
        title = title.replace("~", "")
        title = title.replace("`", "")
        title = title.replace("?", "")

        note = soup.find("p", class_="star-rating")["class"][1]
        score_value = {"One": "1", "Two": "2", "Three": "3", "Four": "4",
                       "Five": "5"}

        note_finale = score_value[note]

        tds = soup.find_all("td")

        datas = []
        for td in tds:
            datas.append(td.string)

        # Identification des données extraites

        upc = datas[0]
        price_excluding_tax = datas[2]
        price_including_tax = datas[3]
        number_available = datas[5]

        # Nettoyage du nombre d'exemplaire disponible

        available_clean = number_available.strip("In stock ( available)")

        # Extraction de la description du produit

        list_p = soup.find_all("p")

        list_ps = []

        for p in list_p:
            list_ps.append(p.string)

        product_description = str(list_p[3])

        # Gestion des cas particuliers:

        exclu = "star-rating"
        if exclu in product_description:
            product_description_clean = "Pas de description disponible"
        else:
            product_description_clean = product_description.strip("</p>")

        # Extraction de la categorie

        category = soup.find_all("a")

        list_as = []

        for a in category:
            list_as.append(a.string)

        categorie = list_as[3]

        # Extraction de l'adresse de l'image de couverture

        images = []
        for img in soup.find_all("img"):
            images.append(img.get("src"))

        url_image = images[0].replace("../..", "https://books.toscrape.com/")

        self.book_data = {
            "title": title,
            "url": self.url,
            "UPC": upc,
            "PRIX HT": price_excluding_tax,
            "PRIX TTC": price_including_tax,
            "disponibilité": available_clean,
            "Description du produit": product_description_clean,
            "Categorie": categorie,
            "URL de l'image de couverture": url_image,
            "Note": note_finale,
        }

        # print(self.book_data.keys())

        os.makedirs("images" + "//" + f"{categorie}", exist_ok=True)
        f = open("images" + "//" + f"{categorie}" + "//" + f"{title}.jpg",
                 "wb")
        f.write(urllib.request.urlopen(url_image).read())
        f.close()
