# Créé par Thomas, le 12/09/2021 en Python 3.7
import turtle

def Cote(n,cote):
    if n==0:
        turtle.forward(cote)
    else:
        Cote(n-1,cote/3)
        turtle.left(60)
        Cote(n-1,cote/3)
        turtle.right(120)
        Cote(n-1,cote/3)
        turtle.left(60)
        Cote(n-1,cote/3)

turtle.penup()
turtle.goto(-350,-250)
turtle.pendown()

def flocon(n,cote):
    turtle.left(60)
    Cote(n,cote)
    turtle.right(120)
    Cote(n,cote)
    turtle.right(120)
    Cote(n,cote)

flocon(2,200)