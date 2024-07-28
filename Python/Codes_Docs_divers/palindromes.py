# Créé par thomas.andre, le 13/09/2021 en Python 3.4
def est_palindrome(mot,i):
    if i>len(mot)//2:
        return True
    elif mot[i]!=mot[-i-1]:
        return False
    else:
        return est_palindrome(mot,i+1)

