# Créé par Thomas, le 27/05/2022 en Python 3.7
#from pygame import mixer
import time
from random import randint,choice
"""
mixer.init()
mixer.music.load("C:/Users/Thomas/Music/Charlie Chaplin   Opening Music  Box Theme  Charlie’s Theme.mp3")
mixer.music.set_volume(1)
mixer.music.play()

def spp(value=0):  #stop/play/pause
    if value==0:
        mixer.music.stop()
    elif value==1:
        mixer.music.pause()
    else:
        mixer.music.unpause()

def stop():
    mixer.music.stop()
"""
def addition(nb1,nb2):
    global score
    res=nb1+nb2
    if int(input("Quelle est le résultat ?"))==res:
        print("Bonne réponse ✔")
        score+=1
    else:
        print("Mauvaise réponse ❌\nLa bonne réponse était :",res)
        score-=0.5

def soustraction(nb1,nb2):
    global score
    res=nb1-nb2
    if int(input("Quelle est le résultat ?"))==res:
        print("Bonne réponse ✔")
        score+=1
    else:
        print("Mauvaise réponse ❌\nLa bonne réponse était :",res)
        score-=0.5

def multiplication(nb1,nb2):
    global score
    res=nb1*nb2
    if int(input("Quelle est le résultat ?"))==res:
        print("Bonne réponse ✔")
        score+=1
    else:
        print("Mauvaise réponse ❌\nLa bonne réponse était :",res)
        score-=0.5

def division(nb1,nb2):
    global score
    res=round(nb1/nb2,2)
    if float(input("Quelle est le résultat (arrondi à 2 décimales) ?"))==res:
        print("Bonne réponse ✔")
        score+=1
    else:
        print("Mauvaise réponse ❌\nLa bonne réponse était :",res)
        score-=0.5

score=0
quotients_simples=[1,2,4,6,8]

starttime=time.time()
for i in range(10):
    opérateur=randint(1,4)
    print("");print("-"*55);print("")
    print("Question n°",i,"\n ")
    if opérateur==1:
        nb1,nb2=randint(0,9),randint(0,9)
        print(nb1,"+",nb2,"= ...")
        addition(nb1,nb2)
    elif opérateur==2:
        nb1,nb2=randint(0,9),randint(0,9)
        print(nb1,"-",nb2,"= ...")
        soustraction(nb1,nb2)
    elif opérateur==3:
        nb1,nb2=randint(0,9),randint(0,9)
        print(nb1,"x",nb2,"= ...")
        multiplication(nb1,nb2)
    else:
        nb1,nb2=randint(0,9),choice(quotients_simples)
        print(nb1,":",nb2,"= ...")
        division(nb1,nb2)
    print(" \nVotre score est de ",score)

print("_"*55);print("")
print("Votre score final est de", score,"/10  😀")
print("Vous l'avez réalisé en :",round((time.time()-starttime),1),"secondes...")
#mixer.music.stop()