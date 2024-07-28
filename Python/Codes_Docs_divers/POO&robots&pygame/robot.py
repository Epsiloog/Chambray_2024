import pygame

screen = pygame.display.set_mode((800, 800))


class Robot(pygame.sprite.Sprite):

    """classe robot qui prend en paramètre dans le constructeur: la position
    [x, y] du robot, sa taille et une image le correspondant
    Dans cette classe on retrouve 7 méthodes :
    - une méthode up pour monter
    - une méthode down pour descendre
    - une méthode left pour tourner à gauche
    - une méthode right pour tourner à droite
    - une méthode slow pour ralentir et grandir
    - une méthode fast pour accélérer et rapetisser
    - une méthode update pour mettre à jour la postion du robot en temps réel"""

    def __init__(self, position, taille, image):
        """fonction constructeur qui crée le robot en fonction de sa taille,
        d'une image correspondante et de sa position"""
        # on initialise la classe parent sprite dont on hérite les attributs et fonctions
        super().__init__()
        # les attributs correspondant aux arguments passés dans le constructeur
        self.position, self.taille, self.image = position, taille, pygame.image.load(image)
        # surface du robot
        self.surf = pygame.Surface(taille)
        # orientation du robot
        self.gauche, self.droite, self.inactif = False, False, True
        # indices d'images pour afficherune image dynamique du robot
        self.indice_inactif, self.indice_image_droite, self.indice_image_gauche = 0, 0, 0
        # listes d'images pour l'affichage dynamique du robot
        self.animation_inactif = [
            pygame.image.load('PNG/Idle (1).png'),
            pygame.image.load('PNG/Idle (2).png'),
            pygame.image.load('PNG/Idle (3).png'),
            pygame.image.load('PNG/Idle (4).png'),
            pygame.image.load('PNG/Idle (5).png'),
            pygame.image.load('PNG/Idle (6).png'),
            pygame.image.load('PNG/Idle (7).png'),
            pygame.image.load('PNG/Idle (8).png'),
            pygame.image.load('PNG/Idle (9).png'),
            pygame.image.load('PNG/Idle (10).png'),

        ]
        self.animation_droite = [
            pygame.image.load('PNG/Run (1).png'),
            pygame.image.load('PNG/Run (2).png'),
            pygame.image.load('PNG/Run (3).png'),
            pygame.image.load('PNG/Run (4).png'),
            pygame.image.load('PNG/Run (5).png'),
            pygame.image.load('PNG/Run (6).png'),
            pygame.image.load('PNG/Run (7).png'),
            pygame.image.load('PNG/Run (8).png')
        ]
        self.animation_gauche = [
            pygame.transform.flip(pygame.image.load('PNG/Run (1).png'), True, False),
            pygame.transform.flip(pygame.image.load('PNG/Run (2).png'), True, False),
            pygame.transform.flip(pygame.image.load('PNG/Run (3).png'), True, False),
            pygame.transform.flip(pygame.image.load('PNG/Run (4).png'), True, False),
            pygame.transform.flip(pygame.image.load('PNG/Run (5).png'), True, False),
            pygame.transform.flip(pygame.image.load('PNG/Run (6).png'), True, False),
            pygame.transform.flip(pygame.image.load('PNG/Run (7).png'), True, False),
            pygame.transform.flip(pygame.image.load('PNG/Run (8).png'), True, False)
        ]
        # rectangle (utile pour les collisions car mis à jour continuellement)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.taille[0], self.taille[1])
        # vitesse de déplacement (variant avec les méthodes de déplacements)
        self.vitesse = 10

    def update(self):
        """fonction de mise à jour du rectangle responsable des collisions en fonction
        de la position du robot et son déplacement sur l'écran"""
        # mise à jour de la "hitbox" du joueur pour permettre la réalisation de collisions
        self.rect = pygame.Rect(self.position[0], self.position[1], 0.8 * self.taille[0], self.taille[1])
        # si l'utilisateur décide de se déplacer alors on affiche la frame correspondant à l'instant de déplacement
        if self.gauche:
            screen.blit(pygame.transform.scale(self.animation_gauche[self.indice_image_gauche], self.taille),
                        self.position)
        elif self.droite:
            screen.blit(pygame.transform.scale(self.animation_droite[self.indice_image_droite], self.taille),
                        self.position)
        # si le joueur ne se déplace pas
        elif self.inactif:
            screen.blit(pygame.transform.scale(self.animation_inactif[self.indice_inactif], self.taille), self.position)
            # gestion de l'affichage dynamique lorsque le joueur ne bouge pas
            self.indice_inactif += 1
            if self.indice_inactif == 10:
                self.indice_inactif = 0

    def left(self):
        """fonction de déplcement du joueur vers la gauche"""
        # si le joueur n'est pas sur le bord gauche
        if self.position[0] + 0.3 * self.taille[0] > 1 + self.vitesse:
            # l'utilisateur recule de sa vitesse
            self.position[0] -= self.vitesse
            # on change l'orientation du joueur
            self.droite, self.gauche, self.inactif = False, True, False
            # gestion de l'affichage dynamique vers la gauche
            self.inactif, self.indice_image_droite = 0, 0
            self.indice_image_gauche += 1
            if self.indice_image_gauche == 8:
                self.indice_image_gauche = 0
        else:
            # par opposition s'il ne se déplace pas vers la gauche
            self.gauche = False
            self.inactif = True

    def right(self):
        """fonction de déplcement du joueur vers la droite"""
        # si le joueur n'est pas sur le bord droit
        if self.position[0] + 0.7 * self.taille[0] < 799 - self.vitesse:
            # l'utilisateur recule de sa vitesse
            self.position[0] += self.vitesse
            # on change l'orientation du joueur
            self.droite, self.gauche, self.inactif = True, False, False
            # gestion de l'affichage dynamique vers la gauche
            self.indice_inactif, self.indice_image_gauche = 0, 0
            self.indice_image_droite += 1
            if self.indice_image_droite == 8:
                self.indice_image_droite = 0
        else:
            # par opposition s'il ne se déplace pas vers la gauche
            self.droite = False
            self.inactif = True

    def up(self):
        """fonction de déplcement du joueur vers le haut"""
        # si le joueur n'est pas en haut de l'écran
        if self.position[1] + 0.1 * self.taille[1] > 1 + self.vitesse:
            # le joueur se déplace de sa vitesse
            self.position[1] -= self.vitesse
            # aucun affichage dynamique pour monter

    def down(self):
        """fonction de déplcement du joueur vers le bas"""
        # si le joueur n'est pas en bas de l'écran
        if self.position[1] + 0.9 * self.taille[1] < 799 - self.vitesse:
            # le joueur se déplace de sa vitesse
            self.position[1] += self.vitesse
            # aucun affichage dynamique pour descendre

    def fast(self):
        """fonction pour faire accélérer le joueur mais le rapetisse"""
        # la réduction est limitée
        if self.taille[0] > 100:
            # augmentation de sa vitesse
            self.vitesse += 0.5
            # augmentation de la taille
            self.taille[0], self.taille[1] = self.taille[0] // 2, self.taille[1] // 2

    def slow(self):
        """fonction pour faire agrandir le joueur maias le ralenti"""
        # l'agrandissement est limité
        if self.taille[0] < 200:
            # réduction de la vitesse
            self.vitesse -= 0.5
            # augmentation de la taille
            self.taille[0], self.taille[1] = self.taille[0] * 2, self.taille[1] * 2
