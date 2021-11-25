# un module pour dessiner des figures simples sur un plan XY
from graphics import GraphWin, Line, Point
# nous avons aussi besoin des fonctions cos et sin ainsi que 
# la valeur pi pour notre calcul de la position d'un point
from math import pi, cos, sin
import turtle


class TurtleBot:
    win = turtle.Screen()

    def __init__(self, nom, x=0, y=0):
        # nom du robot
        self.__nom = nom
        # position du robot
        self.__x = x  # position x du robot
        self.__y = y  # position y du robot
        # angle en degres radius représentant la direction du robot
        self.__angle = 0
        # fenêtre graphique sur laquelle le chemin du robot sera tracé;
        # le point à la position (0,0) se trouve dans le coin supérieur gauche

        self.historique = []
        self.tess = turtle.Turtle()

    def __str__(self):
        """
        Imprime un string du type "R2-D2@(100,100) angle: 0.0" représentant le nom,
        les coordonnées et l'orientation du robot.
        """
        return str(self.nom()) + "@(" + str(self.position()) + ") angle: " + str(self.angle())

    def nom(self):
        return self.__nom

    def angle(self):
        "retourne l'angle en degres représentant la direction du robot"
        return self.tess.heading()

    def position(self):
        return self.tess.position()

    def move_forward(self, distance):
        """ fait avancer le robot de distances pixels
            et trace une ligne lors de ce mouvement """

        self.tess.forward(distance)
        self.historique.append(('forward', distance))

    def move_backward(self, distance):
        """ fait reculer le robot de distances pixels
            et trace une ligne lors de ce mouvement """

        self.tess.backward(distance)
        self.historique.append(('backward', distance))

    def turn_right(self):
        """ fait tourner le robot de 90 degrés vers la droite
            (dans le sens des aiguilles d'une montre)
        """
        self.tess.right(90)
        self.historique.append(('right', 90))

    def turn_left(self):
        """ fait tourner le robot de 90 degrés vers la gauche
            (dans le sens contraire des aiguilles d'une montre)
        """
        self.tess.left(90)
        self.historique.append(('left', 90))

    def history(self):
        return self.historique

    def unplay(self):
        for _ in range(len(self.historique)):
            self.tess.undo()


# Exemple d'utilisation de cette classe (il suffit d'exécuter ce fichier)
if __name__ == '__main__':
    # create robot called R2-D2 at position (100,100) and facing East,
    # to be more or less in the center of the window
    r2d2 = TurtleBot("R2-D2", 100, 100)

    print(r2d2)
    # R2-D2@(100, 100) angle: 0.0
    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    # R2-D2@(150, 100) angle: 270.0
    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    # R2-D2@(150.0, 50.0) angle: 180.0
    r2d2.move_forward(50)
    r2d2.turn_left()
    print(r2d2)
    # R2-D2@(100.0, 50.0) angle: 90.0
    r2d2.move_forward(50)
    print(r2d2)
    # R2-D2@(100, 100) angle: 90.0
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)
    r2d2.move_forward(50)
    r2d2.turn_right()
    print(r2d2)

    print(r2d2.history())
    r2d2.unplay()
