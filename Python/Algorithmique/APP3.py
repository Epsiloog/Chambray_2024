# Créé par Thomas, le 25/04/2023 en Python 3.7

def comptage(L,N):
    P=[0]*(N+1)
    for i in L:
        P[i]+=1
    return P

def tri_comptage(L,N):
    M=[]
    H=comptage(L,N)
    for i in range(N):
        for j in range(H[i]):
            M.append(i)
    return M

speciaux="/:;.,!?€${}()-_\"\' &[]\n\t"
alphabet="abcdefghijklmnopqrstuvwxyz"
txt=["De ondergang der Eerste Wareld","Don quijote","Ecce homo","Fables","faust","The Tragedie of Hamlet","LA CELESTINA","La comédie humaine","La divine comédie","Lusiadas","Mobydick","Osmaias","Richard III"]
ascii_alpha=[]
for i in alphabet:
    ascii_alpha.append(ord(i))
d=97

assert(len(alphabet)==len(ascii_alpha)==26)

textes=[]

with open("textes\\cantaresgallegos_.txt","r",encoding="utf-8") as f:
    g1=f.read()
with open("textes\\deondergangdereerstewareld_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\donquijote_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\eccehomo_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\fables_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\faust_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\follasnovas_.txt","r",encoding="utf-8") as f:
    g2=f.read()
with open("textes\\hamlet_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\lacelestine_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\lacomediehumaine_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\ladivinecomedie_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\lusiadas_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\mobydick_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\osmaias_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())
with open("textes\\richardIII_.txt","r",encoding="utf-8") as f:
    textes.append(f.read())

def nb_lettres(txt):
    L_freq=[0]*26
    for i in txt.lower():
        if ord(i) in ascii_alpha:
            L_freq[ord(i)-97]+=1
    return L_freq

def pourcentage_lettres(nb_lettres_txt):
    pourcentages_lettres_txt=[]
    total=sum(nb_lettres_txt,0)
    for i in nb_lettres_txt:
        pourcentages_lettres_txt.append(round(i/total*100,1))
    return pourcentages_lettres_txt

def nb_lettres_dico(L_casier):
    dico={}
    for i in range(len(L_casier)):
        dico[chr(i+97)]=L_casier[i]
    return dico

nb_lettres_txts=[]
for i in textes:
    nb_lettres_txts.append(nb_lettres(i))

dico_lettres=[]
for i in range(len(nb_lettres_txts)):
    dico_lettres.append(nb_lettres_dico(nb_lettres_txts[i]))

pourcentages_lettres=[]
for i in nb_lettres_txts:
    pourcentages_lettres.append(pourcentage_lettres(i))

dico_lettres_percent=[]
for i in range(len(pourcentages_lettres)):
    dico_lettres_percent.append(nb_lettres_dico(pourcentages_lettres[i]))

valeurs_lettres=[]
for i in dico_lettres:
    valeurs_lettres.append(i.values())

valeurs_lettres_tries=[]
for i in valeurs_lettres:
    valeurs_lettres_tries.append(tri_comptage(i,max(i)))

dico_final=[]
for i in valeurs_lettres_tries:
    tpm={}
    for j in i:
        tpm[dico_lettres[0]]

print(dico_lettres,dico_lettres_percent)

FREQ_Cantares_Gallegos=nb_lettres(g1)
FREQ_Follas_Novas=nb_lettres(g2)

"""
tab_final=[]
for i in range(len(pourcentages_lettres)):
    tab_final.append(["  |  ",txt[i],nb_lettres_dico(pourcentages_lettres[i])])
"""