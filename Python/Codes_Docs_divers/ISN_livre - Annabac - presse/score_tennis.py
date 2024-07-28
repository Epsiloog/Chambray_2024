# Créé par Thomas, le 29/05/2022 en Python 3.7
#15=1 30=2 40=3
'''
#récursif
def jeu(j,s1=0,s2=0):
    if j==1 and s1<4:
        print("j1 a marqué ce point")
        return jeu((int(input("Quelle joueur a marqué le point ?"))),s1+1,s2)
    elif j==2 and s2<4:
        print("j2 a marqué ce point")
        return jeu((int(input("Quelle joueur a marqué le point ?"))),s1+1,s2)
    return(s1,s2)
'''
def jeu_sans_avantages(j=None,s1=0,s2=0):
    while s1<4 and s2<4:
        j=int(input("Quel joueur a marqué le point ?"))
        if j==1:
            s1+=1
        elif j==2:
            s2+=1
    print("Jeu ! J1=" + str(s1) + "  J2=" + str(s2))
    if s1>s2:
        return "Le joueur 1 a donc gagné"
    else:
        return "Le joueur 2 a donc gagné"


"""if s1>s2:
        return ("Le joueur 1 a gagné, le score est de : J1=", s1,"et J2=", s2)
    else:
        return ("Le joueur 2 a gagné, le score est de : J1=", s1,"et J2=", s2)"""

###########################################################################################
jeux1,jeux2,set1,set2=0,0,0,0

def jeu2(resultats):
    resultats=str(resultats)
    if 4<=len(resultats)<=7:
        s1,s2=0,0
        for i in resultats:
            if i==1:
                s1+=1
            elif i==2:
                s2+=1
        return s1>s2

def set():
    global jeux1,jeux2
    while jeux1!=6 and jeux2!=6:
        #resultats=input("Entrez les points du jeu, 1: le joueur 1 gagne un point, 2: le joueur 2 gagne un point (Ex:211222 --> joueur 2 gagne jeu")
        resultats="1111"
        if jeu2(resultats):
            jeux1+=1
        else:
            jeux2+=1
    print("Set ! J1=",jeux1,"| Sets J2=",jeux2)
    return jeux1>jeux2

def match():
    nb_sets=int(input("En combien de sets gagnants ce match est joué ?"))
    global set1,set2
    while set1!=nb_sets and set2!=nb_sets:
        if set():
            set1+=1
        else:
            set2+=1
    if set1>set2:
        print("Le joueur 1 a gagné le match !")
    else:
        print("Le joueur 2 a gagné le match !")

match()