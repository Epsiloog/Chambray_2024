import pygame
from robot import Robot
from obstacle import Obstacle


# banque d'images et de ressources d'affichage
acide = pygame.image.load("png2/Tiles/Acid (2).png")
acide1 = pygame.image.load("png2/Tiles/Acid (1).png")
barril = pygame.image.load("png2/Objects/Barrel (1).png")
switch = pygame.image.load("png2/Objects/Switch (2).png")
help = pygame.transform.scale(pygame.image.load("png2/Settings.png"), (100, 100))
victoire = pygame.transform.scale(pygame.image.load("png2/victoire.png"), (801, 800))
close = pygame.transform.scale(pygame.image.load("png2/Close.png"), (100, 100))
ecran_aide = pygame.Surface((700, 700))
caisse = pygame.transform.scale(pygame.image.load("png2/Tiles/Tile (10).png"), (150, 100))
obstacles = [
    Obstacle([300,100], [200,100], caisse),
    Obstacle([450,100], [200,100], caisse),
    Obstacle([200,275], [200,100], caisse),
    Obstacle([350,275], [200,100], caisse),
    Obstacle([650,450], [200,100], caisse),
    Obstacle([500,450], [200,100], caisse),
    Obstacle([400,625], [200,100], caisse),
    Obstacle([0,625], [150,100], caisse),
    Obstacle([100,450], [200,100], caisse)
]

# création du joueur et de l'arrivée (créé avec la classe robot mais pas dynamique pour autant)
joueur = Robot([0, 0], [200, 200], "PNG/Idle (2).png")
arrive = Robot([660, 568], [140, 232], "png2/Objects/DoorOpen.png")

# variable contenant l'écran de jeu et la condition de la boucle générale du jeu
screen, running = pygame.display.set_mode((800, 800)), True

# dictionnaire recensant les inputs
pressed = {}
# fond noir à afficher en 1er à chaque frames
background = pygame.Surface((800, 800))
# variable utile pour faire une marée avec le fond d'écran
montante, maree = True, 0
# variaible contenant la position de la souris et si un bouton sur la souris est pressé
mouse = [[0, 0], False]
# variable pour le bouton d'aide
besoin_aide = False

# affichage du texte dans la bulle d'aide
pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 50)
texte = "Bienvenue dans le fameux jeu de robot. Le but est de rejoindre la porte située en bas à droite de l'écran pour cela utilisez les flèches directionnelles pour vous déplacer ainsi que la barre d'espace pour grandir et le bouton supprimer pour rapetisser. Bonne Chance !!!"
# boucle générale du jeu
while running:
    # on rend le jeu fluide en controlant le rythme d'éxécution
    pygame.time.wait(50)
    # on affiche le fond noir
    screen.blit(background, (0, 0))
    # gestion du fond d'écran dynamique
    if montante:
        maree += 1
    if not montante:
        maree -= 1
    if maree > 100:
        montante = False
    if maree == 0:
        montante = True
    # affichage du fond d'écran dynamique
    for i in range(4):
        for j in range(3):
            # bain d'acide
            screen.blit(acide, (256 * i, 256 * (j+1)))
    for k in range(4):
        # surface du bain d'acide
        screen.blit(acide1, (256 * k - maree, maree))

    # affichage des détails
    screen.blit(barril, (600, 250))
    screen.blit(switch, (15, 400))

    # gestion des collisions
    for i in obstacles:
        if pygame.sprite.collide_rect(joueur, i):
            # en cas de collisions relancer le jeu
            joueur.position = [0, 0]
        # affichage des images
        screen.blit(i.image, i.position)

    # gestions des touches (flèches haut, droites bas et gauche)
    if pressed.get(pygame.K_RIGHT):
        joueur.right()
    else:
        # modification de l'orientation du joueur
        joueur.droite, joueur.inactif = False, True
    if pressed.get(pygame.K_LEFT):
        joueur.left()
        # modification de l'orientation du joueur
        joueur.inactif = True
    else:
        # modification de l'orientation du joueur
        joueur.gauche, joueur.inactif = False, True
    if pressed.get(pygame.K_UP):
        joueur.up()
    elif pressed.get(pygame.K_DOWN):
        joueur.down()

    # on règle la taille de notre robot et on met à jour sa position
    joueur.update()

    # on affiche notre robot et on met à jour l'écran
    screen.blit(pygame.transform.scale(arrive.image, arrive.taille), arrive.position)

    # gestion du bouton
    screen.blit(help, (700, 0))
    if 800 > mouse[0][0] > 700 and 100 > mouse[0][1] > 0 and mouse[1]:
        besoin_aide = True
    elif 50 < mouse[0][1] < 100 and 50 < mouse[0][1] < 100 and mouse[1]:
        besoin_aide = False
    if besoin_aide:
        # affichage du message d'aide dans la fenêtre d'aide
        screen.blit(ecran_aide, (50, 50))
        ecran_aide.fill((50, 50, 50))
        ecran_aide.blit(close, (0, 0))
        ecran_aide.blit(font.render(texte[0:31], True, (255, 255, 255)), (30, 110))
        ecran_aide.blit(font.render(texte[31:65], True, (255, 255, 255)), (30, 160))
        ecran_aide.blit(font.render(texte[65:97], True, (255, 255, 255)), (30, 220))
        ecran_aide.blit(font.render(texte[97:128], True, (255, 255, 255)), (30, 280))
        ecran_aide.blit(font.render(texte[128:162], True, (255, 255, 255)), (30, 340))
        ecran_aide.blit(font.render(texte[162:184], True, (255, 255, 255)), (30, 400))
        ecran_aide.blit(font.render(texte[184:215], True, (255, 255, 255)), (30, 460))
        ecran_aide.blit(font.render(texte[215:240], True, (255, 255, 255)), (30, 520))
        ecran_aide.blit(font.render(texte[240:252], True, (255, 255, 255)), (30, 580))
        ecran_aide.blit(font.render(texte[253:270], True, (255, 255, 255)), (200, 640))
    # par défaut l'utilisateur n'appuie sur aucun bouton de la souris
    mouse[1] = False

    if pygame.sprite.collide_rect(joueur, arrive):
        screen.blit(victoire, (0, 0))

    # on met à jour l'écran
    pygame.display.flip()

    # on parcours les évennements de pygame (= les inputs du clavier, souris, ...)
    for event in pygame.event.get():
        # inputs de la souris
        mouse[0] = pygame.mouse.get_pos()
        mouse[1] = pygame.mouse.get_pressed()[0]
        # si l'utilisateur veut fermer la fenêtre
        if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        # si l'utilisateur appuie sur une touche
        elif event.type == pygame.KEYDOWN:
            # on modifie la clé de la touche correspondante à True
            pressed[event.key] = True
            # si l'utilisateur veut grandir ou rapetisser
            if event.key == pygame.K_SPACE:
                joueur.fast()
            elif event.key == pygame.K_BACKSPACE:
                joueur.slow()
        # si l'utilisateur n'appuie plus sur cette touche
        elif event.type == pygame.KEYUP:
            # on modifie la clé de la touche correspondante à False
            pressed[event.key] = False
