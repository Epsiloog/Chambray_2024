##### Exercice 2 #####

fruits={"pomme":54,"kiwi":91,"poire":45,"banane":72,"clementine":103}

def stock(dico):
    s=0
    for valeur in dico.values():
        s+=valeur
    return s

def plus_grand_stock(stock_fruits):
    stock_max=0
    fruit_max=""
    for i in stock_fruits.items():
        if i[1]>=stock_max:
            stock_max=i[1]
            fruit_max=i[0]
    return fruit_max

def plus_petit_stock(stock_fruits):
    stock_min=max(stock_fruits.values())
    fruit_min=""
    for i in stock_fruits.items():
        if i[1]<=stock_min:
            stock_min=i[1]
            fruit_min=i[0]
    return fruit_min

fruits2={"pomme":[54,65,23],"kiwi":[91,110,120],"poire":[45,10,32],"banane":[72,10,98],"clementine":[103,100,122]}

def stock_moyen(stock_fruits):
    stock_moyen=0
    fruit_moyen=""
    for i in stock_fruits.items():
        if (i[1][0]+i[1][1]+i[1][2])/3 >= stock_moyen:
            stock_moyen=(i[1][0]+i[1][1]+i[1][2])/3
            fruit_moyen=i[0]
    return fruit_moyen,stock_moyen

##### Exercice 3 #####

scores=[352100,325410,312785,220199,127853]
joueurs=["Batman","Robin","Batman","Joker","Batman"]
scores_max=5

def print_best_score(scores,joueurs):
    for i in range(len(scores)):
        print(str(i+1)+".",joueurs[i],scores[i])

def is_sorted_list(scores):
    for i in range(0,len(scores)-1):
        if scores[i]<scores[i+1]:
            return False
    return True

def best_score(scores,joueurs,nom):
    if is_sorted_list(scores):
        for i in range(len(scores)):
            if joueurs[i]==nom:
                return scores[i]
        return 0
    else:
        print("Rappelez cette fonction lorsque la liste scores sera triée par ordre décroissant")

def ask_best_score_by_name(scores,joueurs):
    nom=str(input("Pour quel joueur souhaitez vous des informations ?"))
    print("Ecrivez le n° du choix dans la fenêtre de dialogue suivante pour en obtenir le résultat")
    choix=int(input("1-obtenir le meilleur score du joueur | 2-Nb de fois où il apparait dans le classemnt | 3-Sa meilleur position dans le classement | 0-Les trois"))
    if choix==1:
        print(best_score(scores,joueurs,nom))
    elif choix==2:
        print(best_count_players(scores,joueurs,nom))
    elif choix==3:
        print(best_position_by_name(scores,joueurs,nom))
    elif choix==0:
        print("Son meilleur score est",best_score(scores,joueurs,nom),"et il apparait",best_count_players(scores,joueurs,nom),"fois dans le tableau des meilleurs scores avec comme meilleure position",best_position_by_name(scores,joueurs,nom))

def best_count_players(scores,joueurs,nom):
    s=0
    for i in joueurs:
        if i==nom:
            s+=1
    return s

def best_position_by_name(scores,joueurs,nom):
    if is_sorted_list(scores):
        for i in range(len(joueurs)):
            if nom==joueurs[i]:
                return i+1
        return -1
    else:
        print("Rappelez cette fonction lorsque la liste scores sera triée par ordre décroissant")

def new_score(score,scores):
    if score>scores[0]:
        return 0
    for i in range(len(scores)-1):
        if scores[i]>=score>=scores[i+1]:
            return i+1
    if score<scores[-1]:
        return len(scores)

def add_score(SCORE,NOM,scores,joueurs):
    indice=new_score(SCORE,scores)
    scores.insert(indice,SCORE)
    joueurs.insert(indice,NOM)
