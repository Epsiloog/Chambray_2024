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
    f.affiche_tete()
    maillon = f.maillon_tete()
    return maillon.valeur()

class Maillon :
    def __init__(self,v) :
        self._valeur = v
        self.suivant = None

    def valeur():
        return self._valeur

class File :
    def __init__(self) :
        self.dernier_file = None

    def maillon_tete():
        return self.dernier_file

    def enfile(self,element=0) :
        nouveau_maillon = Maillon(element)
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != self.dernier_file :
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.affiche
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon
            maillon.suivant = None
            return resultat
        return None
