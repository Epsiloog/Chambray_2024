# Créé par Thomas, le 26/04/2021 en Python 3.7
from math import*
def racines(a,b,c):
    delta=b**2-4*a*c
    if delta > 0:
        print ("deux racines :", "x1 = ",(-b-sqrt(delta)/(2*a)), " et x2 = ",(-b+sqrt(delta))/(2*a))
    elif delta <0:
            print("pas de racine")
    else:
        print("une racine",-b/(2*a))
