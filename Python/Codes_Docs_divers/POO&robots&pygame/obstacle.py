import pygame


class Obstacle(pygame.sprite.Sprite):
    """classe obstacle qui prend en paramètre dans le constructeur : la position
    [x, y] de l'obstacle, sa taille et une image le correspondant
    Dans cette classe on retrouve uniquement une méthode constructeur pour créer un obstacle"""
    def __init__(self, position, taille, image):
        """fonction constructeur qui crée un obstacle en fonction de sa taille,
        d'une image correspondante et de sa position"""
        # on initialise la classe parent sprite dont on hérite les attributs et fonctions
        super().__init__()
        # les attributs correspondant aux arguments passés dans le constructeur
        self.position, self.taille, self.image = position, taille, image
        # surface de l'obstacle
        self.surf = pygame.Surface(taille)
        self.rect = pygame.Rect(self.position, (0.8*self.taille[0], 0.5*self.taille[1]))
