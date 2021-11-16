"""
Classes fournies pour la mission 9; à compléter par les étudiants.
@author Kim Mens
@version 4 novembre 2021
"""

###############
### ARTICLE ###
###############

"""
Cette classe représente un Article de facture simple,
comprenant un descriptif et un prix.
   
@author Kim Mens
@version 4 novembre 2021
"""


class Article:

    def __init__(self, d, p):
        """
        @pre:  d un string décrivant l'article
               p un float représentant le prix HTVA en EURO d'un exemplaire de cet article 
        @post: Un article avec description d et prix p a été créé.
        Exemple: Article("carte graphique", 119.49)
        """
        self.__description = d
        self.__prix = p

    def description(self):
        """
        @post: retourne la description textuelle décrivant l'article.
        """
        return self.__description

    def prix(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, hors TVA.
        """
        return self.__prix

    def taux_tva(self):
        return 0.21

    def tva(self):
        """
        @post: retourne la TVA sur cet article
        """
        return self.prix() * self.taux_tva()

    def prix_tvac(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        @post: retourne un string decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f} EUR".format(self.description(), self.prix())


###############
### FACTURE ###
###############

"""
Cette classe représente une Facture, sous forme d'une liste d'articles.
   
@author Kim Mens
@version 4 novembre 2021
"""


class Facture:
    num_facture = 1

    def __init__(self, d, a_list):
        """
        @pre  d est un string court décrivant la facture;
              a_list est une liste d'objets de type Article.
        @post Une facture avec une description d et un liste d'articles a_list été crée.
        Exemple: Facture("PC Store - 22 novembre", [ Article("carte graphique", 119.49) ])
        """
        self.__description = d
        self.__articles = a_list
        self.num_facture = Facture.num_facture

        Facture.num_facture += 1

    def description(self):
        """
        @post: retourne la description de cette facture.
        """
        return self.__description

    def __str__(self):
        """
        @post: retourne la représentation string d'une facture, à imprimer avec la méthode print().
        (Consultez l'énoncé pour un exemple de la représentation string attendue.)
        """
        s = self.entete_str()
        total_prix = 0.0
        total_tva = 0.0
        for art in self.__articles:
            s += self.article_str(art)
            total_prix += art.prix()
            total_tva += art.tva()
        s += self.totaux_str(total_prix, total_tva)
        return s + "\n\n" + self.livraison_str()

    def entete_str(self):
        """
        @post: retourne une représentation string de l'entête de la facture, comprenant le descriptif
               et les entêtes des colonnes.
        """
        return f"Facture n° {self.num_facture} : " + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "prix HTVA", "TVA", "prix TVAC") \
               + self.barre_str()

    @staticmethod
    def barre_str():
        """
        @post: retourne un string représentant une barre horizontale sur la largeur de la facture
        """
        barre_longueur = 83
        return "=" * barre_longueur + "\n"

    @staticmethod
    def article_str(art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(),
                                                                         art.prix_tvac())

    def totaux_str(self, prix, tva):
        """
        @pre:  prix un float représentant le prix total de la facture en EURO
               tva un float représentant le TVA total de la facture en EURO
        @post: retourne un string représentant une ligne de facture avec les totaux prix et tva,
               à imprimer en bas de la facture
        """
        return self.barre_str() \
               + "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix + tva) \
               + self.barre_str()

    # Cette méthode doit être ajouté lors de l'étape 2.5 de la mission    
    def nombre(self, pce):
        """
        @pre:  pce une instance de la classe Piece
        @post: retourne le nombre d'articles de type ArticlePiece dans la facture,
               faisant référence à une pièce qui est égale à pce,
               en totalisant sur tous les articles qui contiennent une telle pièce.
        """
        for a in self.__articles:
            if isinstance(a, ArticlePiece) and pce == a.piece():
                return a.num()

    def entete_livraison(self):
        return f"Livraison - Facture n° {self.num_facture} : " + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "poids/pce", "nombre", "poids") \
               + self.barre_str()

    @staticmethod
    def article_livraison(art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(
            art.description() + int(art.piece().fragile()) * " (!)",
            art.piece().poids(),
            art.num(), art.piece().poids() * art.num())

    def totaux_livraison(self, a_list):
        """
        @pre:  prix un float représentant le prix total de la facture en EURO
               tva un float représentant le TVA total de la facture en EURO
        @post: retourne un string représentant une ligne de facture avec les totaux prix et tva,
               à imprimer en bas de la facture
        """
        return (
                       self.barre_str()
                       + f"| {str(len(a_list)) + ' articles':40} | {'':10} | {sum(a.num() for a in a_list):10.2f} |"
                         f"{sum(a.piece().poids() for a in a_list):10.2f} |\n"
               ) + self.barre_str()

    # Cette méthode doit être ajouté lors de l'étape 2.6 de la mission    
    def livraison_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode printLivraison
        """
        s = self.entete_livraison()
        a_list = [a for a in self.__articles if isinstance(a, ArticlePiece)]
        for art in a_list:
            s += self.article_livraison(art)
        s += self.totaux_livraison(a_list)
        s += int(any(a.piece().fragile() for a in a_list)) * "(!) *** livraison fragile ***\n"
        return s


#########################
### ARTICLEREPARATION ###
#########################


class ArticleReparation(Article):

    def __init__(self, time):
        self.__time = time
        super().__init__(self.description(), self.prix())

    def description(self):
        return f"Réparation ({self.__time} heures)"

    def prix(self):
        return 20 + 35 * self.__time


#############
### PIECE ###
#############


class Piece:

    def __init__(self, desc, prix, poids=0, is_fragile=False, tva_reduit=False):
        self.__description = desc
        self.__prix = prix
        self.__poids = poids
        self.__is_fragile = is_fragile
        self.__tva_reduit = tva_reduit

    def prix(self):
        return self.__prix

    def description(self):
        return self.__description

    def poids(self):
        return self.__poids

    def fragile(self):
        return self.__is_fragile

    def tva_reduit(self):
        return self.__tva_reduit

    def __eq__(self, other):
        return self.prix() == other.prix() and self.description() == other.description()


####################
### ARTICLEPIECE ###
####################


class ArticlePiece(Article):

    def __init__(self, num, piece):
        self.__num = num
        self.__piece = piece
        super().__init__(self.description(), self.prix())

    def description(self):
        return f"{self.__num} * {self.piece().description()} @ {self.__piece.prix()}"

    def prix(self):
        return self.__num * self.__piece.prix()

    def taux_tva(self):
        return 0.06 if self.__piece.tva_reduit() else 0.21

    def piece(self):
        return self.__piece

    def num(self):
        return self.__num

########################
### RUNNING THE CODE ###
########################

# Ajouter votre code ici pour imprimer une facture et un borderaux
# de livraison.
