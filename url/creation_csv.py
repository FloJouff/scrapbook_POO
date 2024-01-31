import csv
import os.path


def add_data_to_csv(categorie_name, book_data):
    os.makedirs("fichiers_csv", exist_ok=True)
    fieldnames = [
        "title",
        "url",
        "UPC",
        "PRIX HT",
        "PRIX TTC",
        "disponibilité",
        "Description du produit",
        "Categorie",
        "URL de l'image de couverture",
        "Note",
    ]
    with open(
        "fichiers_csv" + "//" + f"{categorie_name}.csv",
        "a",
        newline="",
        encoding="UTF-8-sig",
    ) as fichier_csv:
        writer = csv.DictWriter(
            fichier_csv, fieldnames=fieldnames, delimiter=",",
            lineterminator="\n"
        )
        writer.writeheader()
        writer.writerow(book_data)
