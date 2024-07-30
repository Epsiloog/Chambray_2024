def nb_repetitions(elt,tab):
    assert(type(tab)==list)
    nb=0
    for i in tab:
        if i==elt:
            nb+=1
    return nb


def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a >=1 :
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a