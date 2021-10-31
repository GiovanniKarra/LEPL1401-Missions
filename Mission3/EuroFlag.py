# On importe le module turtle pour y avoir accès
import turtle

# On crée un objet de type Turtle, et on désigne une vitesse de dessin
t = turtle.Turtle()
t.speed("fastest")


# On définit la fonction rectangle
def rectangle(width, height, color1):
    # Boucle pour éviter de répéter les mêmes lignes
    for i in range(2):
        t.color(color1)
        t.pendown()
        t.begin_fill()
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
        t.end_fill()
        t.penup()


def star(line, color2):
    t.color(color2)
    t.pendown()
    t.begin_fill()
    t.left(72)
    t.forward(line)
    for i in range(4):
        t.right(144)
        t.forward(line)

    t.end_fill()
    t.penup()

# Tracer les étoiles en cercle
def cercle_etoile():
    for i in range(24):
        if i % 2 == 0:
            t.left(24)
            t.forward(6)
            t.right(93)
            t.forward(14)
        else:
            t.right(24)
            t.forward(6)
            t.right(93)
            t.forward(14)

            star(5, "yellow")


def aller():
    t.forward(85)
    t.right(90)
    t.forward(25)


def retour():
    t.right(180)
    t.forward(25)
    t.left(90)
    t.forward(85)
    t.pu


def parlement():
    t.right(90)
    t.forward(166)
    t.left(90)
    t.forward(99)
    t.left(180)


def drapeau(a, b, c):
    rectangle(99, 66, a)
    t.forward(33)
    for i in range(2):
        rectangle(33, 66, b)
        t.forward(33)
        b = c


def onyva():
    t.pu
    t.forward(20)
    t.pd


def ontourne():
    t.pu
    t.right(90)
    t.forward(80)
    t.pd


def drapeau_europe():
    rectangle(150, 100, "blue")
    aller()
    cercle_etoile()
    retour()


drapeau_europe()
parlement()
drapeau("blue", "white", "red")
onyva()
drapeau("black", "yellow", "red")
onyva()
drapeau("green", "white", "red")
ontourne()
drapeau("blue", "yellow", "red")
onyva()
drapeau("green", "white", "orange")
ontourne() 