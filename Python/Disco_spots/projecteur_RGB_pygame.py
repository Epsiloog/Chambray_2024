# Importation des bibliothèques
import pygame
from time import sleep

# variable de boucle du jeu
running = True
pygame.init()   # Initialisation de pygame
screen = pygame.display.set_mode((800,800))     # Initialisation de la fenêtre de pygame de taille 800 par 800.

# Boucle principale de l'application
while running:
    screen.fill((255,128,0))    # Remplissage de l'écran par une couleur
    pygame.display.flip()       # mise à jour de l'affichage
    sleep(0.5)
    screen.fill((128,255,0))
    pygame.display.flip()
    sleep(0.5)
    screen.fill((0,255,128))
    pygame.display.flip()
    sleep(0.5)
    screen.fill((0,128,255))
    pygame.display.flip()
    sleep(0.5)
    screen.fill((128,0,255))
    pygame.display.flip()
    sleep(0.5)
    screen.fill((255,0,128))
    pygame.display.flip()
    sleep(0.5)

    for event in pygame.event.get():        # parcours des évènements utilisateurs
            if event.type == pygame.QUIT:   # si le type de l'évènement est égale à pygame.QUIT alors :
                pygame.quit()               # quiter pygame
                running=False               # mise à False de la variable running
