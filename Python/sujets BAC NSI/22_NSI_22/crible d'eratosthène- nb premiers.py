def renverse(mot):
    mot_inversé=''
    for i in mot:
        mot_inversé=i+mot_inversé
    return mot_inversé


def crible(N):
    """renvoie un tableau contenant tous les nombres premiers plus petit que N"""
    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False
    for i in range(2, N):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2*i, N, i):
                tab[multiple] = False
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def premiers():
    min = int(input("Entrez le min : "))
    max = int(input("Entrez le max : "))
    L=[]
    for n in range(min,max + 1):
       if n > 1:
           for i in range(2,n):
               if (n % i) == 0:
                   break
           else:
                L.append(n)
    print(L)