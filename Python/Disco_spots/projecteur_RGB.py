# Créé par Thomas, le 15/07/2024 en Python 3.7

from tkinter import Tk,Canvas,PhotoImage

import time

images = [
"img\carre_rouge.gif",
"img\carre_green.gif",
"img\carre_blue.gif",]
images=images*100

fenetre  = Tk()

largeur,hauteur=800,800

canvas = Canvas(fenetre,width=largeur,height=hauteur)
canvas.pack()

canvas.create_image(0, 0, anchor='nw', tag='image')

for path in images:
    image = PhotoImage(file=path)
    canvas.itemconfigure('image', image=image)
    canvas.update()
    time.sleep(0.5)

