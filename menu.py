from url.categories import Category
from url.books import Book
from url.creation_csv import add_data_to_csv
from url.cat_links import get_categories_links


def main():

    while True:
        print("1. pour scrapper tout le site https://books.toscrape.com/ ")
        print("2. pour scrapper une categorie ")
        print("3. pour scrapper un livre ")
        print("0. pour quitter  ")
        menu_choix = input("faites votre choix: ")
        if menu_choix == "1":
            cat_url = get_categories_links()
            for url in cat_url:
                cat = Category(url)
                print(cat.get_books_url())
                for book_url in cat.get_books_url():
                    book = Book(book_url)
                    book.scrap_book()
                    add_data_to_csv(book.book_data["Categorie"], book.book_data)
        elif menu_choix == "2":
            cat_url = input("lien de la categorie: ")
            cat = Category(cat_url)
            print(cat.get_books_url())
            for book_url in cat.get_books_url():
                book = Book(book_url)
                book.scrap_book()
                add_data_to_csv(book.book_data["Categorie"], book.book_data)
        elif menu_choix == "3":
            book_url = input("lien du livre: ")
            book = Book(book_url)
            book.scrap_book()
            add_data_to_csv(book.book_data["Categorie"], book.book_data)
        elif menu_choix == "0":
            break
        else:
            print("Réponse non valide")
# cat_url = get_categories_links()
# print(cat_url)
# for url in cat_url:
#     cat = Category(url)
#     print(cat.get_books_url())
#     for book_url in cat.get_books_url():
#         book = Book(book_url)
#         book.scrap_book()
#         print(book.book_data)
#         add_data_to_csv(book.book_data["Categorie"], book.book_data)


if __name__ == "__main__":
    main()
