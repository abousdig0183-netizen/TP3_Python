
import json


class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def afficher(self):
        print(f"{self.titre} ({self.annee})")

    def est_recent(self):
        return self.annee >= 2020


class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self.auteur = auteur

    def afficher(self):
        print(f"Livre: {self.titre} par {self.auteur} ({self.annee})")


class Magazine(Document):
    def __init__(self, titre, annee, numero):
        super().__init__(titre, annee)
        self.numero = numero

    def afficher(self):
        print(f"Magazine: {self.titre} No. {self.numero} ({self.annee})")


class Bibliotheque:
    def __init__(self):
        self.documents = []

    def ajouter(self, document):
        self.documents.append(document)

    def rechercher(self, titre):
        resultats = []
        for document in self.documents:
            if titre.lower() in document.titre.lower():
                resultats.append(document)
        return resultats

    def sauvegarder_json(self, fichier):
        donnees = []

        for document in self.documents:
            if isinstance(document, Livre):
                donnees.append({
                    "type": "Livre",
                    "titre": document.titre,
                    "annee": document.annee,
                    "auteur": document.auteur
                })
            elif isinstance(document, Magazine):
                donnees.append({
                    "type": "Magazine",
                    "titre": document.titre,
                    "annee": document.annee,
                    "numero": document.numero
                })

        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":

    # Création des documents
    livre1 = Livre("1984", 1949, "George Orwell")
    magazine1 = Magazine("Science & Vie", 2023, 456)
    livre2 = Livre(
        "Le Petit Prince",
        1943,
        "Antoine de Saint-Exupéry"
    )

    # Affichage des documents
    docs = [livre1, magazine1, livre2]

    for d in docs:
        d.afficher()

    # Création de la bibliothèque
    biblio = Bibliotheque()

    for d in docs:
        biblio.ajouter(d)

    # Recherche
    print("\nRésultat de recherche :")
    resultats = biblio.rechercher("1984")

    for d in resultats:
        d.afficher()

    # Vérification des documents récents
    print("\nDocuments récents :")
    for d in biblio.documents:
        if d.est_recent():
            d.afficher()

    # Sauvegarde JSON
    biblio.sauvegarder_json("bibliotheque.json")
    print("\nSauvegarde JSON terminée.")
