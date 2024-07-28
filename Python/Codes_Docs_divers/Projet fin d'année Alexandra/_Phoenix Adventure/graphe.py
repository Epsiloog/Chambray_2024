import Donnees as donnees
d=donnees.Donnees()

class Noeud:
    def __init__(self, noeud):
        self.noeud=noeud
        self.text=d.get_text(noeud)
        self.gauche=d.get_org(noeud,0)
        self.droit=d.get_org(noeud,1)
        self.image=d.get_image(self.noeud)


class Graphe:
    def __init__(self, valeur = 0):
        self.n=Noeud(valeur)
    def reinit(self, fils):
        self.n=Noeud(fils)

    #etats des noeuds
    def a_gauche(self):
        return self.get_gauche()!=0
    def a_droit(self):
        return self.get_droit()!=0
    def est_choix(self):
        return self.a_gauche() and self.a_droit()
    def est_texte(self):
        return not self.a_gauche() or not self.a_droit()
    def est_fin(self):
        return not self.a_gauche() and not self.a_droit()

    #get des attributs
    def get_noeud(self):
        return self.n.noeud
    def get_text(self):
        return self.n.text
    def get_gauche(self):
        return self.n.gauche
    def get_droit(self):
        return self.n.droit
    def get_image(self):
        return self.n.image

    def avancer(self, n):
        if n=="texte":
            indice_suivant=self.get_gauche()
        if n=="gauche":
            indice_suivant=self.get_gauche()
        if n=="droit":
            indice_suivant=self.get_droit()

        self.reinit(indice_suivant)

g=Graphe()