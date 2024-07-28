# Créé par Thomas, le 10/02/2023 en Python 3.7

"""
Algorithmique avancée - APP1 :
Planification d’une évacuation en urgence de déchets radioactifs

Objectifs de l'exercice :
    - Déplacer et inverser une pile de X conteneurs de déchets radioactifs croissante (sommet : déchet le - toxique, base : déchet le + toxique) d'un silo temp au silo final en passant par N silos de stockage
    - Contraintes : Les déchets sont empilés un par un. Ils ont des niveaux de toxicite r différents. Un déchet de toxicité r ne peut pas être empilé sur un déchet de toxicité < r.  2 déchets qui se suivent ne peuvent pas aller dans le même silo
    - Infos supplémentaires : La pile de déchets initiale du silo temporaire respecte respcte la règle d'empilement précédente. On considère que la taille des silos est supérieure ou égale aux X conteneurs de déchets empilés (particulièrement pr le silo temp et final)
"""

from time import sleep
#from random import randint

class silo():

    def __init__(self,capacite_max,contenu):
        self.capacite_max=capacite_max
        self.contenu=contenu
        print("Instanciation d'un objet \"silo\" avec pour capacite max :",capacite_max,"conteneurs de déchets")

    def est_vide(self):
        if not self.contenu:
            return True
        else:
            return False

    def sommet(self):
        #print(self.contenu[-1])
        if not self.est_vide():
            return self.contenu[-1]
        else:
            return 100

    def empiler(self,r):
        if not self.est_vide:
            if self.contenu[-1]>r:
                self.contenu.append(r)
        else:
            self.contenu.append(r)
        #print(self.contenu)

    def depiler(self):
        if not self.est_vide:
            #print(self.contenu[-1])
            return self.contenu.pop(-1)

    def capacite_max(self):
        return slef.capacite_max

    def remplissage(self):
        return len(self.contenu)

def deplacer(origine,cible):
    #print(origine.contenu,cible.contenu)
    if cible.est_vide() or cible.sommet() > origine.sommet():
        cible.empiler(origine.depiler())
    #print(origine.contenu,cible.contenu)

def evacuation(N,X):
    """
    N : nombre de silo de stockage
    X : nombre de conteneurs de déchets radioactifs
    """
    global tube_initial,L_silos,silo_final
    tube_initial=list(tube_initial) ; silo_temp=tube_initial.copy() ; silo_temp.reverse()

    assert(N>=3 and X==len(tube_initial))

    for i in range(N):
        L_silos.append(silo(X,[]))
    #print(L_silos)

    if N==X:
        for i in range(N-1,-1,-1):
            L_silos[i].empiler(int(silo_temp.pop()))
        return resoudre_XN(X,N,L_silos)

    elif N==3:
        """
        for i in range(0,3):
            L_silos[i].empiler(int(silo_temp.pop()))
        """
        return resoudre_3N(X,L_silos[0],L_silos[1],silo_final)

    else:
        return resoudre(X,N,L_silos)

    for i in range(N):
        print(L_silos[i].contenu)

def resoudre(X,N,L_silos):
    while not L_silos[0].remplissage()==1:
        for i in range(N,0,-1):
            L_silos[i].empiler(depiler(L_silos[0]))


def resoudre_XN(X,N,L_silos):
    assert(X==N)
    for i in L_silos:
        silo_final.empiler(i)
    print(silo_final.contenu)
    return silo_final.contenu

def resoudre_3N(n,origine,temp,cible):
    if n>0:
        resoudre_2N(n-1,origine,cible,temp)
        deplacer(origine,cible)
        resoudre_2N(n-1,temp,origine,cible)

        L_etats.append([origine.contenu,temp.contenu,temp.contenu])
        print("p",origine.contenu,temp.contenu,cible.contenu)
    #return origine.contenu,temp.contenu,cible.contenu

################################## Main ########################################

print("Bienvenue dans le protocole d'évacuation d'urgence des dechets radioactifs de la centrale ! \nPour commencer il est nécéssaire de connaitre les niveaux de toxicité des X conteneurs de déchets à évacuer du tube initial. \nCes derniers sont empilé du moins toxique en bas au plus toxique en haut.")
print("Dans cet algorithme le tube est modélisé par une liste strictement croissante.")
tube_initial=input("Inscrivez les niveaux de radioactivités r des X déchets (<=10) sortis du réacteur sous la forme : r1r2r3...")

X=len(tube_initial)
for i in range(0,X-1):
    assert(type(i)==type(1) and tube_initial[i]<tube_initial[i+1])

N=int(input("Pour combien de silos de stockage voulez vous faire la simulation ?"))
L_silos=[]
silo_final=silo(X,[])
L_etats=[]

evacuation(N,X)


if N==X:
    resoudre_XN(X,N,L_silos)
elif N==3:
    L_etats.append([L_silos[0].contenu,L_silos[1].contenu,[]])
    resoudre_2N(X,L_silos[0],L_silos[1],silo_final)
else:
    resoudre(X,N,L_silos)

################################################################################

########## Données / Exemples ##########

L_etats_3=[[[3,2,1],[],[]],
        [[3,2],[],[1]],
        [[3],[2],[1]],
        [[3],[2,1],[]],
        [[],[2,1],[3]],
        [[1],[2],[3]],
        [[1],[],[3,2]],
        [[],[],[3,2,1]]]

########## Affichage console / graphique ##########

def console(etats):
    colones,lignes,l_max_dechet=0
    colone_p,ligne_p=""

    for i in etats:
        colones=len(i)

        for silo in i:
            lignes=len(silo)
            if max(silo)>l_max_dechet:
                l_max_dechet=max(silo)
            silo.reverse()
            for dechet in silo:
                if dechet<4:
                    ligne_p+=dechet*"■"
                else:
                    ligne_p+=str(dechet)+(dechet-1)*"■"
    sleep(3)



"""
class dechet():
    def __init__(self,toxicite):
        self.toxicite=toxicite
        print("Instanciation d'un déchet radioactif de niveau :",toxicite)

    def get_toxicite(self):
        return self.toxicite
"""

"""
def evacuation(N,X):

    global tube_initial,L_silos,silo_final
    assert(N>=2 and X==len(tube_initial))
    for i in range(N):
        L_silos.append(silo(X,[]))
    #print(L_silos)
    for i in range(N,-1,-1):
        L_silos[i].empiler(int(tube_initial.pop()))

    while tube_initial != []:
        if i<N:
            L_silos[i].empiler(int(tube_initial.pop()))
            i+=1
        else:
            i=0
    return L_silos

    for i in range(N):
        print(L_silos[i].contenu)
"""

"""
for i in range(0,len(tube_initial)-1):
    if tube_initial[i]==",":
        tube_initial.pop(i)
print(tube_initial)
"""
