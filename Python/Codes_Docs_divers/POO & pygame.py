# Créé par Thomas, le 18/10/2021 en Python 3.7
import pygame
class personne():
    def __init__(self,age,sport,photo):
        self.age=age
        self.sport=sport
        self.photo=photo

    def avoir_age(self):
        return self.age

    def affiche_photo(self,img):
        affichage(img)

image1=pygame.image.load('C:/Users\Thomas\Pictures\photos_de_profil\me_rectangle.jpg')

Thomas=personne(17,"athlétisme",image1)
print("âge :",Thomas.avoir_age(),", sport :",Thomas.sport, ", photo",Thomas.photo)

def affichage(image):
    screen=pygame.display.set_mode((363,525))
    run=True
    while run:
        pygame.display.flip()
        screen.blit(image,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()