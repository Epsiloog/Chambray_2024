# Créé par Thomas, le 12/05/2021 en Python 3.7
# encodé en utf-8
import numpy as np

#combinaisons_gagnantes= ([1,5,9],[3,5,7],[1,2,3],[1,4,7],[7,8,9],[3,6,9],[2,5,8],[4,5,6]), si un joueur fait ces combinaisons, alors il a gagné

# Création d'un tableau 3x3 pour représenter le plateau de jeu
tableau = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(tableau)

# Variable pour contrôler la continuation du jeu et pour compter les coups joués
continuer = True
compteur = 0

# Fonction pour demander au joueur de choisir une case entre 1 et 9
def choisir_nombre():
    n = input("Entrer un nombre entre 1 et 9")
    try:
        n = int(n)
        if 1 <= n <= 9:
            # Vérifie si la case est déjà prise
            if tableau[(n-1)//3][(n-1)%3] == 10 or tableau[(n-1)//3][(n-1)%3] == 20:
                print("Déjà pris, choisis une autre case")
                return choisir_nombre()
            else:
                return n
        else:
            print("Pas entre 1 et 9")
            return choisir_nombre()
    except ValueError:
        print("Ce n'est pas un entier")
        return choisir_nombre()

# Fonction pour placer le coup du joueur dans le tableau
def placer(n, j):
    global tableau
    global compteur
    if compteur < 9:
        tableau[(n-1)//3][(n-1)%3] = j  # Place le coup du joueur dans la case correspondante
        compteur += 1
        print("Le nombre de coups est de", compteur)

# Fonction pour vérifier si le joueur j a gagné
def test_gagnant(j):
    global tableau
    # Vérifie toutes les combinaisons gagnantes possibles
    if (tableau[0][0] == tableau[0][1] == tableau[0][2] or
        tableau[1][0] == tableau[1][1] == tableau[1][2] or
        tableau[2][0] == tableau[2][1] == tableau[2][2] or
        tableau[0][0] == tableau[1][0] == tableau[2][0] or
        tableau[0][1] == tableau[1][1] == tableau[2][1] or
        tableau[0][2] == tableau[1][2] == tableau[2][2] or
        tableau[0][0] == tableau[1][1] == tableau[2][2] or
        tableau[2][0] == tableau[1][1] == tableau[0][2]):
        return True
    else:
        return False

# Boucle principale du jeu
while continuer:
    # Tour du joueur 1 (10)
    placer(choisir_nombre(), 10)
    print(tableau)
    if test_gagnant(10):
        print("Le joueur 1 a gagné")
        continuer = False
    else:
        # Tour du joueur 2 (20)
        placer(choisir_nombre(), 20)
        print(tableau)
        if test_gagnant(20):
            print("Le joueur 2 a gagné")
            continuer = False

    # Si le tableau est plein et qu'il n'y a pas de gagnant, le jeu s'arrête
    if compteur == 9:
        continuer = False

"""
Explications détaillées :

1. **Initialisation du plateau de jeu** : Le tableau est initialisé avec des valeurs de 1 à 9 pour que les joueurs puissent facilement choisir des cases.
2. **Variables globales** : `continuer` pour contrôler la boucle de jeu et `compteur` pour suivre le nombre de coups joués.
3. **Fonction `choisir_nombre`** : Demande à l'utilisateur de choisir un nombre entre 1 et 9 et vérifie la validité de l'entrée.
4. **Fonction `placer`** : Place le coup du joueur dans le tableau en utilisant une conversion pour les coordonnées du tableau.
5. **Fonction `test_gagnant`** : Vérifie si un joueur a gagné en testant toutes les combinaisons gagnantes possibles.
6. **Boucle principale du jeu** : Alterne entre les tours des deux joueurs, place leurs coups, vérifie s'il y a un gagnant et arrête le jeu si le tableau est plein ou si un joueur a gagné.
"""