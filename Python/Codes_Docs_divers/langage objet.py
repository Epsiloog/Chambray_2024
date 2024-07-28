# Créé par Thomas, le 15/01/2023 en Python 3.7

# 4 immeubles, 2 supermarchés et une banque

class Batiment():

    def __init__(self,adresse,nb_etages):
        self.adresse=adresse
        self.nb_etages=nb_etages
        print("Tu as initialisé une instance de la classe Batiment grâce à sa méthode constructrice __init__(self,paramètres) avec pour adresse :",adresse,"et un nb détages égale à",nb_etages)

    def get_adresse(self):
        return self.adresse

    def get_etages(self):
        return self.nb_etages


class Immeuble(Batiment):
    def __init__(self,nb_balcons):
        super().__init__(adresse,nb_etages)
        self.nb_balcons=nb_balcons

    def get_balcons(self):
        return self.balcons


class Supermarché(Batiment):
    def __init__(self,nb_rayons):
        super.__init__(adresse,nb_etages)
        self.nb_rayons=nb_rayons

    def get_rayons(self):
        return self.nb_rayons

class Banque(Batiment):
    def __init__(self,nb_coffres,nom):
        super().__init__(adresse,nb_etages)
        self.nb_coffres=nb_coffres
        self.nom=nom

    def get_coffres(self):
        return self.nb_coffres

    def get_nom(self):
        return self.nom


immeuble1=Immeuble(2)
