def xor(tab1,tab2):
    assert(len(tab1)==len(tab2))
    tab_xor=[]
    for i in range (len(tab1)):
        if tab1[i]==tab2[i]:
            tab_xor.append(0)
        else:
            tab_xor.append(tab1[i] or tab2[i])
    return tab_xor

a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]

assert(xor(a, b) == [1, 1, 0, 1, 1, 0, 0, 1])
assert(xor(c, d) == [1, 1, 1, 0])

################################ EXERCICE_2 ####################################

class Carre:
    def __init__(self, tableau = [[]]):
        self.ordre = len(tableau)
        self.valeurs = tableau

    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.valeurs[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        return sum(self.valeurs[i])

    def somme_col(self, j):
        '''calcule la somme des valeurs de la colonne j'''
        return sum([self.valeurs[i][j] for i in range(self.ordre)])

def est_magique(carre):
    n = carre.ordre
    s = carre.somme_ligne(0)

    #test de la somme de chaque ligne
    '''for i in range(0, n):
        if carre.somme_ligne(i) != s:
            return False'''

    #test de la somme de chaque colonne
    for j in range(n):
        if carre.somme_col != s:
            return False

    #test de la somme de chaque diagonale
    '''if sum([carre.valeurs[k][k] for k in range(n)]) != s:
            return False
    if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:
            return False'''

    return s


carre1=[[2, 7, 6], [9, 5, 1], [4, 3, 8]]
def test():
    c3=Carre(carre1)
    return est_magique(c3)

print(test())