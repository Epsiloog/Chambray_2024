"""def recherche(caractere,mot):
    list(mot)
    i=len(mot)
    while i!=0:
        if mot(i)==caractere:
            nb_occ+=1
        i-=1
    return(nb_occ)"""

pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
       return solution
    p = pieces[i]
    if p <= arendre-p:
        solution.append(pieces[i])
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1)
