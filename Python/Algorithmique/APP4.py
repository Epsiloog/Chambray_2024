from random import randint
##################################################### Variables ########################################################

trouve=False
tentatives_max=0
tentatives=1
mot_propose=""
long=len(mot_propose)
mots,mots_hash=[],[]
nb_mots=len(mots)
mots_tentes=[]
grille=[]

##################################################### Fonctions #########################################################

def str_to_int(mot):
    n=len(mot)
    v=0
    for i in mot:
        v+=ord(i)*256**(n-1)
        n-=1
    return v

def hachage(mot):
    return str_to_int(mot)%(nb_mots//5)

def create_table(n):
    return [[] for i in range(n)]

#########################################################################################################################

long=int(input("De combien de lettres doit être composé le mot à trouver (entre 4 et 9) ?"))
while 4>long or long>9:
    print("Le mot doit être composé de 9 lettes au maximum et de 4 lettres au minimum.")
    long=str(input("De combien de lettres doit être composé le mot à trouver (entre 4 et 9) ?"))

tentatives_max=int(input("En combien de tentatives souhaitez-vous devinez le mot ? (entre 4 et 9)"))
while 4>tentatives_max or tentatives_max>9:
    print("Le nombre de tentatives doit être de 9 maximum et de 4 minimum.")
    tentatives_max=int(input("Combien de tentatives souhaitez-vous avoir pour devinez le mot ? (entre 4 et 9)"))

with open("liste.de.mots.francais.frgut.txt","r",encoding="utf-8") as f:
    lignes=f.readlines()

for i in lignes:
    if len(i)==long+1:
        mots.append((i.strip()))

nb_mots=len(mots)
mot_propose=mots[randint(0,nb_mots)]

mots_hash=create_table(nb_mots//5)
for i in mots:
    mots_hash[hachage(i)].append(i)

del(mots)
mots_hash=tuple(mots_hash)
print("\nLe dictionnaire contient",nb_mots,"mots possibles de",long,"lettres.")
#print(mots_hash)

print(" - 2 signifie : bonne lettre et à la bonne place\n - 1 : lettre dans le mot mais pas à la bonne place\n - 0 : mauvaise lettre")

grille=[0]*long
while not trouve and tentatives<=tentatives_max:
    print("\nTentative n°",tentatives)
    mot_tente=str(input("Quelle mot pensez-vous être le bon ?"))
    while len(mot_tente)!=long or (mot_tente not in  mots_hash[hachage(mot_tente)]) or mot_tente in mots_tentes:
        if mot_tente in mots_tentes:
            mot_tente=str(input("Ce mot a déjà été essayé."))
        else:
            mot_tente=str(input("Invalide, votre mot doit avoir le même nombre de lettres que le mot sélectionné et doit être inscrit dans le dictionnaire."))
    mots_tentes.append(mot_tente)
    for i in range(long):
        if mot_tente[i] not in mot_propose:
            grille[i]=0
        else:
            if mot_tente[i]==mot_propose[i]:
                grille[i]=2
            else:
                grille[i]=1
    print(grille)
    if grille==[2]*long:
        trouve=True
    tentatives+=1

if trouve:
    print("Félicitaion, vous avez trouvé le mot au bout de la",tentatives,"tentative !")
else:
    print("Dommage, vous ferez mieux la prochaine fois !\nLe mot était :",mot_propose)
