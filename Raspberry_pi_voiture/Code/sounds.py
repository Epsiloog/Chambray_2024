#Importation du module mixer (permet de gérer la lecture de musiques) de la bibliothèque pygame
from pygame import mixer

def police_song():
    """
    Cette fonction va initialiser les spécifications audio comme la fréquence, le nombre de cannaux...
    puis charger un fichier mp3 d'après son chemin donné en argument
    et enfin définir le volume et lire le fichier importé dans ce programme
    """
    mixer.init()
    mixer.music.load("/home/pi/Adeept_modifié/server/sounds/Sirène de la Police Nationale FR_f.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()

def pompier_song():
    """print(police_song.__doc__)"""
    mixer.init()
    mixer.music.load("/home/pi/Adeept_modifié/server/sounds/sirene-pompier.mp3")
    mixer.music.set_volume(0.8)
    mixer.music.play()

#définition des fonctions nécéssaires pour mettre en pause/lecture et arrêter la musique
def pause():
    mixer.music.pause()
def unpause():
    mixer.music.unpause()
def stop():
    mixer.music.stop()
