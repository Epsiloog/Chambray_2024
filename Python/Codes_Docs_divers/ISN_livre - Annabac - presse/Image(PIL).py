# Créé par Thomas, le 07/07/2022 en Python 3.7

from PIL import Image
from time import sleep

def rotation():
    (largeur,hauteur)=img.size
    img_rot=Image.new("RGB",(largeur,hauteur),(0,0,0))
    nb_rot=1
    for i in range(nb_rot):
        for x in range(largeur):
            for y in range(hauteur):
                c=img.getpixel((y,hauteur-1-x))
                img_rot.putpixel((x,y),(c))
    img_rot.show()

def echange_pix(img,x0,x1,y0,y1):
    p1 = img.getpixel((x0,y0))
    p2 = img.getpixel((x1,y1))
    img.putpixel((x0,y0),p2)
    img.putpixel((x1,y1),p1)

def echange_quadrant(img,x0,x1,y0,y1,n):
    for i in range(n):
        for j in range(n):
            echange_pix(img,x0+i,y0+j,x1+i,y1+j)

def tourne_quadrants(image, x0,y0,n):
    if n>=2:
        m=n//2
        tourne_quadrants(image,x0,y0,m)
        tourne_quadrants(image, x0, y0+m,m)
        tourne_quadrants(image, x0+m,y0,m)
        tourne_quadrants(image, x0+m,y0+m,m)
        echange_quadrant(image,x0,y0,x0+m,y0,m)
        echange_quadrant(image,x0,y0,x0+m,y0+m,m)
        echange_quadrant(image,x0,y0,x0,y0+m,m)

def quart_tour(img):
    largeur,hauteur=img.size
    assert largeur==hauteur
    tourne_quadrants(img,0,0,largeur)
    img.show()
#quart_tour(Image.open("joconde2.jpg"))


img = Image.open("carre_orange.gif")
img.show()