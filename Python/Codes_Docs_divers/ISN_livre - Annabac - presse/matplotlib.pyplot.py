# Créé par Thomas, le 16/06/2022 en Python 3.7
import matplotlib.pyplot as plt
from numpy import array, linspace

f=lambda x:x**2+x+2
#X=array(range(-20,21))
X=linspace(-20,20,40)
Y=f(X)
print(X,Y)

plt.xlabel("Abscisses X")
plt.ylabel("Ordonnées Y")
plt.title("Représentation graphique d'une fonction du 2nd degré")
plt.plot(X,Y,c="red",linewidth=2,linestyle="--")
plt.scatter(X,Y,c="black")
#plt.legend(loc="lower right")
plt.grid(True)
#plt.figure(1)
plt.show()


#f="x**2-2"
#X=[-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#Y=[398,359,322,287,254,223,194,167,142,119,98,79,62,47,34,23,14,7,2,-1,-2,-1,2,7, 14, 23, 34, 47, 62, 79, 98, 119, 142, 167, 194, 223, 254, 287, 322, 359, 398]