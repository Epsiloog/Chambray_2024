# Créé par Thomas, le 26/08/2022 en Python 3.7
from time import sleep
from random import randint,choice

rép=str(input("Voici un programme très intéréssant mais qui demande un long temps de chargement, voulez vous l'essayer ?"))
if rép.upper() != "OUI":
    # or "YES" or "BIEN SÛR" or "BIEN SUR" or "AVEC PLAISIR"
    print("Au revoir ＞﹏＜")
    sleep(3)
    exit()

for i in range(1,6):
    print("."*i)
    sleep(0.85)

values=[0,1,2,5,10]
barre="■"
print(barre)
while len(barre)<200:
    if len(barre+"■"+"■"*choice([0,1,2,5,10]))<205:
        barre+="■"+"■"*choice([0,1,2,5,10])
    print(barre)
    sleep(0.1*randint(2,30))

sleep(0.5)
print("Et voilà !  Le programme parle pour lui même ;)")
sleep(5)