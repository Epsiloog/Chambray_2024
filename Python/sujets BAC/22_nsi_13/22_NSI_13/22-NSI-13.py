def rendu(somme_a_rendre):
    assert(somme_a_rendre>=0)
    n1=0 ; n2=0 ; n3=0
    while somme_a_rendre>=5:
        somme_a_rendre-=5
        n1+=1
    while somme_a_rendre>=2:
        somme_a_rendre-=2
        n2+=1
    while somme_a_rendre>=1:
        somme_a_rendre-=1
        n3+=1
    return [n1,n2,n3]


def test():
    f=File()
    f.enfile(1)
    f.enfile(2)
    return(f.affiche())

class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element=None) :
        nouveau_maillon = Maillon(element)
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != None :
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file.suivant
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon
            maillon.suivant = None
            return resultat
        return None
