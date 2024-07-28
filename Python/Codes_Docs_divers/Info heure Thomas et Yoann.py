# Créé par thomas.andre, le 12/11/2020 en Python 3.4
def info_heure(heure):
    heure=input("Quelle heure est t-il?")
    if 0<=heure<24:
        if 6<=heure<19:
            print("nous sommes le matin et il fait jour!")
        if 12<=heure<18:
            print("nous sommes l'après midi et il fait jour!")
        if 18<=heure<21:
            print("nous sommes en soirée!")
    else:
        print("Heure comprise entre 0h et 24h svp")