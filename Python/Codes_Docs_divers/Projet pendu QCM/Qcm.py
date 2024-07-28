# Créé par yoann.henry, le 04/02/2021 en Python 3.4
#les bibliothèques
import pandas
from random import shuffle
import tkinter
#premières variables
#qliste=pandas.read_csv("liste.csv")   #on importe la liste du quizz dans une variable python
'''prenom=input("Bonjour je suis un algorithme vous proposant une experience de qcm, je vais vous poser 10 questions et a la fin vous connaitrez votre score. Comment vous appelez vous ?")
print("Bien ",prenom,"Etes vous pret?")
print("Dans ce cas c'est parti!")
reponse_user=input(qliste)'''
reponse_user=input()
reponses=[B,D,C,B,D,C,D,C,D,B,A,C,A,C,A,C,D,A,D,C,B,C,A,B,B,D,A,A,A,D]
if reponse_user==reponses.loc[1]:
    print('bonne réponse')
    score=score+1
else:
     print('mauvaise réponse')
#for qliste in range(0,11):

