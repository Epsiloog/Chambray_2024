# Créé par Thomas, le 08/05/2022 en Python 3.7
def seuil(p):
    n=1
    while 1-(5/6)**n <=p:
        n=n+1
    return n
