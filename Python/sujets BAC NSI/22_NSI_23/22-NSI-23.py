def max_dico(dico):
    if dico is not False:
        max_clée=''
        max=0
        for i in range (dico):
            if dico[i][1]>max:
                max=dico[i][1]
                max_clée=dico[i]
        return max_clée
    else:
        print("dico est vide")



class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


'''def eval_expression(tab):
    p = Pile()
    for ... in tab:
        if element != '+' ... element != '*':
            p.empiler(...)
        else:
            if element == ...:
                resultat = p.depiler() + ...
            else:
                resultat = ...
            p.empiler(...)
    return ...'''
