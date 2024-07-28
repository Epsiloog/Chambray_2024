def comptage(L, N):
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

txt=["De ondergang der Eerste Wareld","⚠ PORTUGAIS :Don quijote","Ecce homo","Fables","faust","The Tragedie of Hamlet","La Celestina","La comédie humaine","La divine comédie","⚠ PORTUGAIS : Os Lusiadas","Mobydick","⚠ PORTUGAIS : Os maias","Richard III"]
speciaux="/:;.,!?€${}()-_\"\' &[]\n\t"
alphabet="abcdefghijklmnopqrstuvwxyz"
ascii_alpha=[]
for i in alphabet:
    ascii_alpha.append(ord(i))

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

def lettres_dico(L_casier):
    dico={}
    for i in range(len(L_casier)):
        dico[chr(i+97)]=L_casier[i]
    return dico

nb_lettres_txts=[]
for i in textes:
    nb_lettres_txts.append(nb_lettres(i))

pourcentages_lettres=[]
for i in nb_lettres_txts:
    pourcentages_lettres.append(pourcentage_lettres(i))

nb_final=[]
for i in range(len(nb_lettres_txts)):
    nb_final.append(["  | ",txt[i],lettres_dico(nb_lettres_txts[i])])

freq_final=[]
for i in range(len(pourcentages_lettres)):
    freq_final.append(["  | ",txt[i],lettres_dico(pourcentages_lettres[i])])

print("Fréquence en % (arrondi au dixième) de chaque lettre dans les 13 textes des langues officielles :\n",freq_final)
print("\n\nNombre d'apparitions de chaque lettre dans les 13 textes des langues officielles :\n",nb_final)

nb_Cantares_Gallegos=nb_lettres(g1)
nb_Follas_Novas=nb_lettres(g2)

dico_Cantares_Gallegos=lettres_dico(nb_Cantares_Gallegos)
dico_Follas_Novas=lettres_dico(nb_Follas_Novas)

print("\nNombre d'apparitions de chaque lettre dans le texte 1 en galicien, Cantares Gallegos :",dico_Cantares_Gallegos)
print("\nNombre d'apparitions de chaque lettre dans le texte 2 en galicien, Follas Novas :",dico_Follas_Novas)

print("\n",tri_comptage(nb_Cantares_Gallegos,max(nb_Cantares_Gallegos)),"\n",tri_comptage(nb_Follas_Novas,max(nb_Follas_Novas)))
#print(nb_lettres_txts[])