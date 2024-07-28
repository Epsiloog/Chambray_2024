# Créé par Thomas, le 07/10/2021 en Python 3.7
class calculatrice:
    def __init__(self,type_de_calculatrice):
        self.type=type_de_calculatrice
    def additione(self,terme1,terme2):
        return(terme1+terme2)

ma_calculatrice=calculatrice(1)
print(ma_calculatrice.additione(2,3.45))



