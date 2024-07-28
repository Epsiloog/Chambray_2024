# -*- coding: utf-8 -*-
"""

@author: hb (Created on Wed Mar 06 2019)
Simulation d'un quiz
"""

# Fonction donnant une permutation aléatoire d'une séquence donnée
from random import shuffle

# Mise en données sous forme d'un dictionnaire
# Clé       : Q (question )
# Attributs : Liste de réponses dont seulement une est correcte (RJ)
# Exemples :

quiz = {
     "Q01":["RJ","R1","R2","R3"]
    ,"Q02":["RJ","R1","R2","R3"]
    ,"Q03":["RJ","R1","R2","R3"]
    ,"Q04":["RJ","R1","R2","R3"]
    ,"Q05":["RJ","R1","R2","R3"]
    ,"Q06":["RJ","R1","R2","R3"]
    ,"Q07":["RJ","R1","R2","R3"]
    ,"Q08":["RJ","R1","R2","R3"]
    ,"Q09":["RJ","R1","R2","R3"]
    ,"Q10":["RJ","R1","R2","R3"]
}

# Nombre de questions du quiz
nQ = len(quiz)

# Liste d'une permutation aléatoire des questions
questions=quiz.keys() # Liste des questions du quiz
shuffle(questions) # Liste d'une permutation aléatoire des questions

# Nombre de questions proposées pour le test (inférieur ou égal à nQ)
nb_questions = 4
nb_questions = min(nb_questions,nQ) # limite le nombre de questions à nQ

# Score (s'incrémente de 1 à chaque bonne réponse)
score=0 # Initialisation du score à zéro avant le début du quiz

# Début du quiz
for q in range(nb_questions):
    question = questions[q]
    reponses = quiz[question][:] # Copie de laiste des réponses potentielles
    shuffle(reponses) # mélange des réponses potentielles

    print
    print (u'Choisissez une et une seule réponse à la question : '),question
    for i,reponse in enumerate(reponses):
        print (i),' : ',reponse
    print
    choix = int(raw_input('Saisir votre réponse : '))

    print
    if reponses[choix] == quiz[question][0]:
        score+=1
        print ('Bravo ! Votre score est de' 'score'),') / ',nb_questions
    else:
        print (u'Mauvaise réponse ! Votre score est de '),score,' / ',nb_questions

print
print ('Vous avez eu un score de '),score,' / ',nb_questions