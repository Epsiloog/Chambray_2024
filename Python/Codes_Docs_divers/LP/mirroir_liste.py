# Créé par Thomas, le 09/10/2021 en Python 3.7
L=[1,2,3]
Lmirroir=[]
Lmirroir+=L
index=len(L)-1
while index>=0:
    Lmirroir.append(L[index])
    index-=1

print(Lmirroir)

