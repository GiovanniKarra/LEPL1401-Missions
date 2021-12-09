from OrderedLinkedList import OrderedLinkedList


class Classement(OrderedLinkedList):

    def __init__(self):
        """
        @pre: -
        @post: un classement vide de taille 0 a été créé
        """
        super().__init__([])
        self.__resultats = {}

    def size(self):
        """
        Méthode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de résultats actuellement stockés dans ce classement a été retourné.
        """
        super().size()

    def add(self, r):
        """
        Ajoute un résultat r dans ce classement.
        @pre:  r est une instance de la classe Resultat
        @post: Le résultat r a été inséré selon l'ordre du classement.
               En cas d'ex-aequo, r est inséré après les autres résultats de même ordre.
        """
        super().add(r)
        if self.__resultats[r.coureur().nom()].temps() > r.temps():
            self.__resultats[r.coureur().nom()] = r.temps()

    def get(self, c):
        """
        Retourne le résultat d'un coureur donné.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        try:
            return self.__resultats[c]
        except:
            return None

    def get_position(self, c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post retourne un entier représentant la position du coureur c dans ce classement,
              à partir de 1 pour la tête de ce classement. Si le coureur figure plusieurs fois
              dans le classement, la première (meilleure) position est retournée.
              Retourne -1 si le coureur ne figure pas dans le classement.
        """
        i = 1
        result = self.first()
        while c != result.value().coureur().nom() and i <= self.length():
            result = result.next()
            i += 1
        if i > self.length():
            return -1
        else:
            return i

    def remove(self, c):
        """
        Retire un résultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) résultat pour le coureur c du classement.
              c est comparé au sens de __eq__. Retourne c si un résultat a été retiré,
              of False si c n'est pas trouvé dans la liste.
        """
        if self.first().coureur() == c:
            self.set_first(self.first().next())
            self.dec_size()
        else:
            runner = self.first()
        while runner.next() is not None and c != runner.next().coureur():
            runner = runner.next()
        if runner.next() is None:
            return False

        result = runner.next()
        runner.set_next(result.next())
        self.dec_size()
        try:
            return self.__resultats.pop(c.nom())
        except:
            return False

    def __str__(self):
        """
        Méthode magique
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: Retourne une représentation de ce classement sous forme d'un string,
               avec une ligne par résultat.
        """
        s = "Classement : \n"
        result = self.first()
        while result is not None:
            s += str(result)
        return s
