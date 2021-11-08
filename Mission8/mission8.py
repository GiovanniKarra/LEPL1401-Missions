from typing import Type


class Duree:

    def __init__(self, h: int = 0, m: int = 0, s: int = 0):
        """
            @pre: h, m et s sont des entiers positifs (ou zéro)
                  m et s sont < 60
            @post: Crée une nouvelle durée en heures, minutes et secondes.
        """
        self.s = s
        self.m = m
        self.h = h

        if self.s >= 60:
            self.m += self.s // 60
            self.s = self.s % 60

        if self.m >= 60:
            self.h += self.m // 60
            self.m = self.m % 60

    def __str__(self):
        """
        @pre:  -
        @post: Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: la méthode "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le String désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def __gt__(self, other):
        return self.delta(other) > 0

    def to_secondes(self) -> int:
        """
        @pre:  -
        @post: Retourne le nombre total de secondes de cette instance de Duree (self).
        Par exemple, une durée de 8h 41m 25s compte 31285 secondes.
        """
        return self.s + self.m * 60 + self.h * 3600

    def delta(self, d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne la différence en secondes entre cette durée (self)
               et la durée d passée en paramètre.
               Cette valeur renvoyée est positif si cette durée (self)
               est plus grande que la durée d, négatif sinon.
        Par exemple, si cette durée (self) est 8h 41m 25s (donc 31285 secondes)
        et la durée d est 0h 1m 25s, la valeur retournée est 31200.
        Inversement, si cette durée (self) est 0h 1m 25s et la durée
        d est 8h 41m 25s, alors la valeur retournée est -31200.
        """
        return self.to_secondes() - d.to_secondes()

    def apres(self, d) -> bool:
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne True si cette durée (self) est plus grand que la durée
               d passée en paramètre; retourne False sinon.
        """
        return self > d

    def ajouter(self, d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Ajoute une autre durée d à cette durée (self),
               corrigée de manière à ce que les minutes et les secondes soient
               dans l'intervalle [0..60[, en reportant au besoin les valeurs
               hors limites sur les unités supérieures
               (60 secondes = 1 minute, 60 minutes = 1 heure).
               Ne retourne pas une nouvelle durée mais modifié la durée self.
        """
        self.__init__(s=self.to_secondes() + d.to_secondes())


class Chanson:
    def __init__(self, t: str, a: str, d: Duree):
        """
        @pre:  t et a sont des string, d est une instance de la classe Duree
        @post: Crée une nouvelle chanson, caractérisée par un titre t,
               un auteur a et une durée d.
        """
        self.t = t
        self.a = a
        self.d = d

    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
               "TITRE - AUTEUR - DUREE".
               Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return f"{self.t} - {self.a} - {str(self.d)}"


class Album:
    def __init__(self, numero: int):
        """
        @pre:  numero est un entier identifiant de facon unique cet album
        @post: Crée un nouvel album, avec comme identifiant le numero,
               et avec une liste de chansons vide.
        """
        self.id = numero
        self.songs = []

    @property
    def length(self) -> (int, int):
        return sum([s.d.to_secondes() for s in self.songs]), len(self.songs)

    def is_not_max(self, d: Duree = Duree()) -> bool:
        return all(x < y for x, y in zip((self.length[0] + d.to_secondes(), self.length[1] + 1), (75 * 60, 100)))

    def add(self, song: Chanson) -> bool:
        if not self.is_not_max(song.d):
            return False

        self.songs.append(song)
        return True

    def __str__(self):
        """
        format :
            Album 21 (12 chansons, 00:47:11)
            01: White_Wedding - Billy_Idol - 00:04:12
            02: Stand_And_Deliver - Adam_&_The_Ants - 00:03:33
            .
            .
            .
        """
        d = Duree(s=self.length[0])

        return f"Album {self.id} ({self.length[1]} chansons, {str(d)})" + "".join(
               [f"\n{i[0] + 1:02}: {str(i[1])}" for i in enumerate(self.songs)])


if __name__ == "__main__":
    # Grâce à la ligne ci-dessus, le code ci-dessous ne sera exécuté que si on n'exécute ce fichier directement.
    # Ceci nous permet d'éviter que le code ci-dessous sera exécuté lorsqu'on fait un import de ce fichier,
    # par exemple dans notre fichier test.py
    with open("music_db.txt", "r") as f:
        lines = f.readlines()

    albums = []
    parameters = [(line.split()[0], line.split()[1], [int(x) for x in line.split()[2:]]) for line in lines]
    songs = [Chanson(n, a, Duree(0, d[0], d[1])) for n, a, d in parameters]
    album_id = 1

    album = Album(album_id)

    for song in songs:
        if not album.add(song):
            album_id += 1
            albums.append(album)
            album = Album(album_id)
            album.add(song)

    albums.append(album)

    output = "\n\n".join([str(a) for a in albums])

    print(output)
