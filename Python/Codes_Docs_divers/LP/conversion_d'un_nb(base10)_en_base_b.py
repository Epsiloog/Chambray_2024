# Créé par Thomas, le 09/10/2021 en Python 3.7
D=[]
D_inversé=[]
n=int(input("Entrez votre nombre à convertir (en base 10)."))
b=13
while n>0:
    D.append(n%b)
    n=n//b
index=len(D)-1
while index>=0:
    D_inversé.append(D[index])
    index-=1

print(D,D_inversé)
