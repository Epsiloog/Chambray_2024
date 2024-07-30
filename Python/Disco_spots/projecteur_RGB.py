# Créé par Thomas, le 15/07/2024 en Python 3.7

from tkinter import Tk,Canvas,PhotoImage    # Importation des bibliothèques utiles
import time

# Liste des images qui vont être difusées
images = [
"img\carre_rouge.gif",
"img\carre_green.gif",
"img\carre_blue.gif",]
images=images*100

# Création de la fenêtre tkinter
fenetre  = Tk()

largeur,hauteur=800,800

# Création d'un canvas dans la fenêtre avec les dimensions spécifiées
canvas = Canvas(fenetre, width=largeur, height=hauteur)
canvas.pack()  # Affichage du canvas dans la fenêtre

# Création d'un élément image sur le canvas, positionné en haut à gauche (nw: north-west)
canvas.create_image(0, 0, anchor='nw', tag='image')

# Boucle pour afficher les images séquentiellement
for path in images:
    image = PhotoImage(file=path)  # Chargement de l'image à partir du chemin de fichier
    canvas.itemconfigure('image', image=image)  # Configuration de l'élément image sur le canvas avec la nouvelle image
    canvas.update()  # Mise à jour du canvas pour refléter les changements
    time.sleep(0.5)  # Pause de 0.5 seconde entre chaque image pour créer un effet de diaporama


