def recherche(tab,n):
    if not not tab:
        trouvé=False
        début=0
        fin=len(tab)-1
        while début <= fin and trouvé==False:
            milieu=(début+fin)//2
            if n==tab[milieu]:
                trouvé=True
            elif n>tab[milieu]:
                début=milieu+1
            else:
                fin=milieu-1
        print(n,'est dans le tableau :',tab,'car trouvé =',trouvé,".  Il est situé à l'indice",milieu)
    else:
        return -1


ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for lettre in message :
        if lettre in ALPHABET:
            indice = (position_alphabet(lettre)+decalage)%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat+=lettre
    return resultat
