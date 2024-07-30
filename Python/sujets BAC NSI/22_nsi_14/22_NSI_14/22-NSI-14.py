def correspond(mot,mot_a_trous):
    assert(type(mot)==str and type(mot_a_trous)==str)
    if len(mot)!=len(mot_a_trous):
        return False
    mot_a_comparer=''
    for i in range(len(mot)):
        if mot_a_trous[i]=='*':
            mot_a_comparer+=mot[i]
        else:
            mot_a_comparer+=mot_a_trous[i]
    if mot==mot_a_comparer:
        return True
    else:
        return False


def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant
    à un plan d'envoi de messages entre `N` personnes A, B, C,
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon.
    '''
    personne = 'A'
    N = len(plan)
    assert(N<=26)
    for i in range(N-1):
        if plan[personne] == 'A':
            return False
        else:
            personne = plan[personne]
    return True
