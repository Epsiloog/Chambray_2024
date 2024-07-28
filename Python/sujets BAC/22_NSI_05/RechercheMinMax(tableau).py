def RechercheMinMax(tableau):
    max=tableau[(len(tableau))-1]
    min=tableau[(len(tableau))-1]
    for i in range (0,len(tableau)-2):
        if tableau[i]<min:
            min=tableau[i]
        if tableau[i]>max:
            max=tableau[i]
    return {'min':min,'max':max}


class Carte:
    """Initialise Couleur (entre 1 a 4), et Valeur (entre 1 a 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v
        assert(self.Couleur in [1,2,3,4])
        assert(self.Valeur in [1,2,3,4,5,6,7,8,9,10,11,12,13])

    """Renvoie le nom de la Carte As, 2, ... 10,
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []


    """Remplit le paquet de cartes"""
    def remplir(self):
        self.contenu = [ Carte(couleur,valeur) for couleur in range(1, 4) for valeur in range( 1, 13)]

    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        if 0 <= pos < 52 :
            return self.contenu[pos]

def test():
    unPaquet = PaquetDeCarte()
    unPaquet.remplir()
    uneCarte = unPaquet.getCarteAt(20)
    print(uneCarte.getNom() + " de " + uneCarte.getCouleur())

test()
