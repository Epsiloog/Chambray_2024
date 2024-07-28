import pandas as pd

file=pd.read_csv("fichier.csv", sep=",", encoding='utf-8')

class Donnees:
    def __init__(self):
        self.file=file

    def get_image(self,n):
        i=self.file.loc[n, "image"]
        if i !="none":
            return "image/"+str(i)

        return 'image/not_define.jpg'

    def get_text(self,n):
        m=str(self.file.loc[n,"texte"])
        return m

    def get_org(self,n,i):
        choix ={0:"gauche", 1:"droit"}
        assert i in (0,1), "i compris dans [0,1]"
        v=choix[i]
        ind=self.file.loc[n, v]
        return ind

d=Donnees()

