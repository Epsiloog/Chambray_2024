class Noeud:    #création de la classe noeud

    def __init__(self, g, v, d):    #le constructeur, méthode appelée à chaque instantiation
        self.gauche = g             #d'un nouvel objet de la classe Noeud
        self.valeur = v
        self.droit = d

    def __str__(self):              #méthode spéciale qui lorsqu'elle est appelée renvoie :
        return str(self.valeur)     #self.valeur sous la forme d'une chaine de caractère

    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None
        '''if self.gauche==None and self.droit==None:
            return True'''

def expression_infixe(e):
    s = ''
    if e.gauche is not None:
        s = s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit)
    if e.gauche is None and e.droit is None:
        return s

    return '('+ s +')'

arbre=Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))