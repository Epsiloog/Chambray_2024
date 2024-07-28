# Créé par Thomas, le 16/09/2023 en Python 3.7

def hanoi(n, depart, par, fin):
    #assert(len(depart)==n)
    if n > 0:
        hanoi(n-1, depart, fin, par)
        fin.append(depart.pop())
        hanoi(n-1, par, depart, fin)
    return (depart,par,fin)