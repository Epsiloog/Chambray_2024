#################### Importation des bibiothèques/modules ######################

from random import randint
from time import perf_counter
import matplotlib.pyplot as plt
#from numpy import array, linspace

################################## Fonctions ###################################

def tri_insertion(t,j=1,i=0,k=0):
    while j<len(t):
        i=j-1
        k=t[j]
        while i>=0 and t[i]>k:
            t[i+1]=t[i]
            i=i-1
        t[i+1]=k
        j=j+1
    return t

def tri_selection(t,i=0,min=0,j=0):
    while i<len(t):
        j=j+1
        min=i
        while j<len(t):
            if t[j]<t[min]:
                min=j
            j=j+1
        if min!=i:
            t[i],t[min]=t[min],t[i]
        i+=1
    return t

def interclassement(L1,L2):
    L_fin=[]
    i1,i2=0,0
    while i1<len(L1) and i2<len(L2):
        if L1[i1]<L2[i2]:
            L_fin.append(L1[i1])
            i1+=1
        else:
            L_fin.append(L2[i2])
            i2+=1
    return L_fin + L1[i1:] + L2[i2:]

def tri_fusion(L):
    if len(L)<=1:
        return L
    else:
        m=len(L)//2
        return interclassement(tri_fusion(L[:m]),tri_fusion(L[m:]))

def score_m(num):
    return sum(tab_j[num],0)/10

def nb_scores_min_max(num):
    nb=0
    mini=min(tab_j[num]) ; maxi=max(tab_j[num])

    for i in range(len(tab_j)):
        if i!=num:
            for j in tab_j[i]:
                if mini < j < maxi:
                    nb+=1
    return nb

def score_global(num):
    return score_m(num)-nb_scores_min_max(num)/((max_j-1)*10)

#################################### Main ######################################

max_j=int(input("Pour combien de joueurs maximum voulez vous effectuer la simulation ?"))
intervalle=int(input("Avec quelle intervalle de joueurs souhaitez vous tracer la courbe du temps"))

debut=perf_counter()
tab_j=[[] for i in range(max_j)]

for I in range(max_j):
    for j in range(10):
        tab_j[I].append(randint(0,10)+randint(0,10)/10)

scores_locaux=[]
for i in range(len(tab_j)):
    scores_locaux.append(score_m(i))

scores_globaux=[]
for i in range(max_j):
    scores_globaux.append(score_global(i))

temps_inser,temps_selec,temps_f=[],[],[]

for j in range(max_j+1):

    if j%intervalle==0:

        tps1=perf_counter()
        local_insertion=tri_insertion(scores_locaux[0:j])
        global_insertion=tri_insertion(scores_globaux[0:j])
        tps2=perf_counter()
        tps_insertion=tps2-tps1
        del(local_insertion,global_insertion)

        tps1=perf_counter()
        local_selection=tri_selection(scores_locaux[0:j])
        global_selection=tri_selection(scores_globaux[0:j])
        tps2=perf_counter()
        tps_selection=tps2-tps1
        del(local_selection,global_selection)

        tps1=perf_counter()
        local_fusion=tri_fusion(scores_locaux[0:j])
        global_fusion=tri_fusion(scores_globaux[0:j])
        tps2=perf_counter()
        tps_fusion=tps2-tps1

        temps_inser.append(tps_insertion) ; temps_selec.append(tps_selection) ; temps_f.append(tps_fusion)

fin=perf_counter()
print(len(local_fusion),len(global_fusion),"\nTri des scores locaux :",local_fusion,"\nTri des scores globaux :",global_fusion)
print("\nCalculs terminés en :",round(fin-debut,2),"secondes.")

############################## Affichage graphique #############################

X=[i for i in range(0,max_j+1,intervalle)]

plt.xlabel("Nombre de joueurs (intervalle = "+str(intervalle)+")")
plt.ylabel("Temps en s")
plt.title("Graphique du temps de calcul en fonction du nb de joueurs")

plt.plot(X,temps_inser,c="red",label="tri insertion")
plt.plot(X,temps_selec,c="blue",label="tri sélection")
plt.plot(X,temps_f,c="black",label="tri fusion")

plt.legend()
plt.grid(True)
plt.show()