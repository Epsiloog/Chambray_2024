# Créé par Thomas, le 12/10/2021 en Python 3.7
def termes_suite(n):
    T=80
    liste_termes_T=[80]
    for i in range(n-1):
        T=0.8*T+2
        liste_termes_T.append(T)
    print(liste_termes_T)
