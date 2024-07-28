import pygame
#from time import sleep

print(" ")
print("-----------------------------------------------------------------------")
print(" ")
print("Bonjour !  Bienvenue dans un jeu sur le cercle des 17 !")
print("Pour pouvoir y jouer il va falloir que tu répondes à un QUIZ 😀")
pygame.time.wait(5000)
nom_joueur=str(input("Mais au fait comment t'appelle tu ?"))
print("Très bien",nom_joueur,'commençons')

q1="Comment s'appelle la société qui souhaite recruter des enfants ayant des pouvoirs liés à l'électricité ?"
r1="elgen"
q2="Qui est le dirigeant de l'académie de Pasadena ?"
r2="hatch"
q3="Quelle est le prénom de la mère du héros principal ?"
r3=""
q4="Qui sont devenus les CH des Elgen ?  .... et ...."
r4="jack et wade"
q5="Quelle est le pouvoir de Abigail ?\
    a) Elle accentue la douleur d'une personne lorsqu'elle est en contact\
    b) Elle rend une personne insensible à toute stimulation sensorielle (1 à 5 sens)\
    c) Elle supprime la douleur en stimulant, par l'électricité, les terminaisons nerveuses"
r5="c"

Questions_réponses=[[q1,r1],[q2,r2],[q3,r3],[q4,r4],[q5,r5]]

screen=pygame.display.set_mode((800,800))
background=pygame.Surface((800,800))

running=True
r2=True

titre=pygame.image.load("lecercledes17.jpg")
tome1=pygame.transform.scale(pygame.image.load("tome1.png"),(800,800))
#vey2=pygame.transform.scale(pygame.image.load("Vey.jpg",(144,360)))
#tome1=pygame.Surface.convert(tome1)

while running:
    pygame.display.flip()
    screen.blit(background,(0,0))
    screen.blit(titre,(0,0))
    while r2:
        pygame.display.flip()
        screen.blit(background,(0,0))
        screen.blit(tome1,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                r2=False
                running=False
                pygame.quit()

score=0
No_Q=['1ère','2nde','3ème','4ème','5ème']

for i in range (len(Questions_réponses)):
    print("")
    #print(i)
    print('Voici la',No_Q[i],'question')
    print(Questions_réponses[i][0])
    réponse=str(input("Entrez la réponse dans cette fenêtre"))
    print(réponse)
    #réponse=réponse.lower
    #Questions_réponses[i][1]=str(Questions_réponses[i][1].lower)
    #print(Questions_réponses[)
    if réponse==Questions_réponses[i][1]:
        print('✔ Bonne réponse')
        score+=1
    else:
        print("❌ Mauvaise réponse")
    print('Votre score est de :',score,'!')
#.lower()