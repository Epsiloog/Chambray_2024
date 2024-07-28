def moyenne(tab):
    if len(tab)>0:
        m=0
        for i in tab:
            m+=i
        m/=len(tab)
        return m
    else:
        return 'erreur'


def tri(tab):
    ''' Cf EPREUVE PRATIQUE BLANCHE
    i est le premier indice de la zone non triee, j le dernier indice.
    Au debut, la zone non triee est le tableau entier.
    '''
    i= ...
    j= ...
    while i != j :
        if tab[i]== 0:
            i= ...
        else :
            valeur = tab[j]
            tab[j] = ...
            ...
            j= ...
    ...
