# Créé par Thomas, le 12/05/2021 en Python 3.7
# encodé en utf-8
import numpy as np

tableau = np.array([[1,2,3],[4,5,6],[7,8,9]]) #on a importé une liste pour faire un tableau, et numéroté les cases pour que le joueur indique ses positions
print(tableau)
#combinaisons_gagnantes= ([1,5,9],[3,5,7],[1,2,3],[1,4,7],[7,8,9],[3,6,9],[2,5,8],[4,5,6]) #si un joueur fait ces combinaisons, alors il a gagné
continuer=True
compteur=0

def choisir_nombre(): #fonction permettant de choisir un nombre et ne pas "planter" le programme si ce n'est pas un nombre entre 1 et 9 (ou des lettres ?)
    n=input("Entrer un nombre entre 1 et 9")
    try:
        n=int(n)
        if n>0 and n<10:
            if tableau[(n-1)//3][(n-1)%3]==10 or tableau[(n-1)//3][(n-1)%3]==20: #raccourcissement de la position dans le tableau
                print("Déjà pris, choisis une autre case")
                return choose_number()
            else :
                return n
        else:
            print("Pas entre 1 et 9")
            return choose_number()
    except:
        print("Ce n'est pas un entier")
        return choose_number()

"""
def placer1(n):
    global tableau  #global pour pouvoir utiliser tableau dans la fonction
    tableau[(n-1)//3][(n-1)%3]=10 #division pour déterminer les positions

def placer2(n):
    global tableau
    tableau[(n-1)//3][(n-1)%3]=20
"""

def placer(n,j):
    global tableau
    global compteur
    if compteur<9:
        tableau[(n-1)//3][(n-1)%3]=j
        compteur=compteur+1
        print("Le nombre de coups est de ",compteur)

def test_gagnant(j):
    global tableau
    global continuer
    #combinaisons gagnantes
    if tableau[0][0]==tableau[0][1]==tableau[0][2] or tableau[0][1]==tableau[1][1]==tableau[1][2] or tableau[0][2]==tableau[1][1]==tableau[2][0]  or tableau[0][0]==tableau[1][0]==tableau[2][0]\
    or tableau[1][0]==tableau[1][1]==tableau[1][2] or tableau[2][0]==tableau[2][1]==tableau[2][2] or tableau[0][1]==tableau[1][1]==tableau[2][1] or tableau[0][0]==tableau[1][1]==tableau[2][2]:
        return True
    else:
        return False

while continuer:
    placer(choisir_nombre(),10)
    print(tableau)
    if test_gagnant(10):
        print("Le joueur 1 a gagné")
        continuer=False

    else:
            placer(choisir_nombre(),20)
            print(tableau)
            if test_gagnant(20):
                print("Le joueur 2 a gagné")
                continuer=False

    if compteur==9:
        continuer=False

"""
while continuer==1:  #faire tourner les fonctions tant qu'une combinaison gagnante n'est pas atteinte
    placer1(choisir_nombre())
    test_gagnant() #fonction pour arreter le jeu si une combibnaison est atteinte
    print(tableau)
    placer2(choisir_nombre())
    test_gagnant()
    print(tableau)
"""