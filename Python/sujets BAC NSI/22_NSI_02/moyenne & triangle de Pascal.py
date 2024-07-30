def moyenne(notes):
    #notes=[(15,2),(9,1),(12,3)]

    Notes_pondérées=0
    for i in range (len(notes)):
        Notes_pondérées+=notes[i][0]*notes[i][1]

    Somme_coeffs=0
    for i in range (len(notes)):
        Somme_coeffs+=notes[i][1]

    Moyenne=Notes_pondérées/Somme_coeffs
    return(Moyenne)


def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C
