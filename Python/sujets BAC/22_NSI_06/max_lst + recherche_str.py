def maxi(tab):
    max=(tab[0],0)
    for i in range (len(tab)):
        if tab[i]>max[0]:
            max=(tab[i],i)
    return max

print(maxi([5,8,6,9,47]))

def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False :   #l'indice i avance dans seq_adn
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:    #l'indice j avance dans adn
            j+=1
        if j == g:
            trouve = True
        i+=1
    return trouve
