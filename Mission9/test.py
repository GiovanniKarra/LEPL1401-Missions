"""
Tests fournis pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 4 novembre 2021
"""

from mission9 import Article, Facture, ArticleReparation, ArticlePiece, Piece

"""
Test initial pour la classe Article.
@author Kim Mens
@version 4 novembre 2021
"""
articles = [Article("laptop 15\" 8GB RAM", 743.79),
            Article("installation windows", 66.11),
            Article("installation wifi", 45.22),
            Article("carte graphique", 119.49),
            ArticleReparation(1.5),
            ArticlePiece(3, Piece("Livre d'Eric Zemmour", 39.99, 420, True, True)),
            ArticlePiece(10, Piece("PC Gaming Low Budget", 420.69, 42))
            ]


def test_articles(a_list):
    for art in a_list:
        print(art)


"""
Test initial pour la classe Facture.
@author Kim Mens
@version 4 novembre 2020
"""
facture = Facture("PC Store - 22 novembre", articles)
facture2 = Facture("PC Store - 23 novembre", [Article("Bluetooth USB", 6.99)])


def test_facture(f):
    print(f)


art_reparation = ArticleReparation(4)

def test_reparation():
    print(art_reparation)

"""
Faire exécuter les différents tests.
"""

if __name__ == "__main__":
    print("\n*** TEST DE LA CLASSE Article ***\n")
    test_articles(articles)

    print("\n*** TEST DE LA CLASSE Facture ***\n")
    test_facture(facture)
    test_facture(facture2)

    print("\n*** TEST DE LA CLASSE ArticleReparation ***\n")
    test_reparation()
