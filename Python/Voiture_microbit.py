# À ouvrir avec le site : python.microbit.org

from microbit import *

# Initialisation des valeurs d'impulsion pour les servos
impulsion1 = 1500
impulsion2 = 1500

# Fonction pour régler le servo 1 en fonction de l'impulsion
def set_servo1(impulsion1):
    alpha1 = (impulsion1 / 20000) * 100  # Conversion de l'impulsion en pourcentage de la période
    duty1 = (alpha1 / 100 ) * 1023  # Conversion du pourcentage en valeur de devoir analogique
    pin1.set_analog_period_microseconds(20000)  # Définir la période analogique à 20 ms
    pin1.write_analog(duty1)  # Écrire la valeur analogique sur la broche pin1
    print('impulsion1=',impulsion1, ' alpha1=', alpha1, ' duty1=', duty1)  # Afficher les valeurs pour le débogage

# Fonction pour régler le servo 2 en fonction de l'impulsion
def set_servo2(impulsion2):
    alpha2 = (impulsion2 / 20000) * 100  # Conversion de l'impulsion en pourcentage de la période
    duty2 = (alpha2 / 100 ) * 1023  # Conversion du pourcentage en valeur de devoir analogique
    pin2.set_analog_period_microseconds(20000)  # Définir la période analogique à 20 ms
    pin2.write_analog(duty2)  # Écrire la valeur analogique sur la broche pin2
    print('impulsion2=',impulsion2, ' alpha2=', alpha2, ' duty2=', duty2)  # Afficher les valeurs pour le débogage

# Fonction pour faire avancer le robot
def avancer():
    display.show(Image('01910:'  # Afficher une flèche pointant vers le haut
                       '19991:'
                       '93939:'
                       '30903:'
                       '00900'))
    global impulsion1
    global impulsion2
    if impulsion1 > 500 and impulsion1 < 2500:  # Vérifier que l'impulsion est dans la plage valide
        impulsion1 = impulsion1 - 200  # Diminuer l'impulsion pour le servo 1
    if impulsion2 > 500 and impulsion2 < 2500:  # Vérifier que l'impulsion est dans la plage valide
        impulsion2 = impulsion2 + 100  # Augmenter l'impulsion pour le servo 2
    sleep(250)  # Pause de 250 ms
    display.clear()  # Effacer l'affichage
    set_servo1(impulsion1)  # Régler le servo 1
    set_servo2(impulsion2)  # Régler le servo 2
    sleep(1000)  # Pause de 1 seconde

# Fonction pour faire tourner le robot à gauche
def tourner_gauche():
    display.show(Image('03910:'  # Afficher une flèche pointant à gauche
                       '00391:'
                       '99999:'
                       '00391:'
                       '03910'))
    global impulsion1
    global impulsion2
    if impulsion1 > 500 and impulsion1 < 2500:  # Vérifier que l'impulsion est dans la plage valide
        impulsion1 = impulsion1 - 100  # Diminuer l'impulsion pour le servo 1
    if impulsion2 > 500 and impulsion2 < 2500:  # Vérifier que l'impulsion est dans la plage valide
        impulsion2 = impulsion2 - 100  # Diminuer l'impulsion pour le servo 2
    sleep(250)  # Pause de 250 ms
    display.clear()  # Effacer l'affichage
    set_servo1(impulsion1)  # Régler le servo 1
    set_servo2(impulsion2)  # Régler le servo 2
    sleep(1000)  # Pause de 1 seconde

# Fonction pour faire tourner le robot à droite
def tourner_droite():
    display.show(Image('01930:'  # Afficher une flèche pointant à droite
                       '19300:'
                       '99999:'
                       '19300:'
                       '01930'))
    global impulsion1
    global impulsion2
    if impulsion1 > 500 and impulsion1 < 2500:  # Vérifier que l'impulsion est dans la plage valide
        impulsion1 = impulsion1 + 100  # Augmenter l'impulsion pour le servo 1
    if impulsion2 > 500 and impulsion2 < 2500:  # Vérifier que l'impulsion est dans la plage valide
        impulsion2 = impulsion2 + 100  # Augmenter l'impulsion pour le servo 2
    sleep(250)  # Pause de 250 ms
    display.clear()  # Effacer l'affichage
    set_servo1(impulsion1)  # Régler le servo 1
    set_servo2(impulsion2)  # Régler le servo 2
    sleep(1000)  # Pause de 1 seconde

# Fonction pour faire reculer le robot
def reculer():
    display.show(Image('00900:'  # Afficher une flèche pointant vers le bas
                       '30903:'
                       '93939:'
                       '19991:'
                       '01910'))
    global impulsion1
    global impulsion2
    if impulsion1 > 500 and impulsion1 < 2500:  # Vérifier que l'impulsion est dans la plage valide
        impulsion1 = impulsion1 + 200  # Augmenter l'impulsion pour le servo 1
    if impulsion2 > 500 and impulsion2 < 2500:  # Vérifier que l'impulsion est dans la plage valide
        impulsion2 = impulsion2 - 100  # Diminuer l'impulsion pour le servo 2
    sleep(250)  # Pause de 250 ms
    display.clear()  # Effacer l'affichage
    set_servo1(impulsion1)  # Régler le servo 1
    set_servo2(impulsion2)  # Régler le servo 2
    sleep(1000)  # Pause de 1 seconde

# Fonction pour arrêter le robot
def arret():
    global impulsion1
    global impulsion2
    display.show(Image.SAD)  # Afficher une image triste
    impulsion1 = 1500  # Réinitialiser l'impulsion pour le servo 1
    impulsion2 = 1500  # Réinitialiser l'impulsion pour le servo 2
    set_servo1(impulsion1)  # Régler le servo 1
    set_servo2(impulsion2)  # Régler le servo 2
    sleep(250)  # Pause de 250 ms
    display.clear()  # Effacer l'affichage

# Fonction pour faire un "dash" (accélération rapide) du robot
def dash():
    global impulsion1
    global impulsion2
    if impulsion1 > 500 and impulsion1 < 2500:  # Vérifier que l'impulsion est dans la plage valide
        impulsion1 = impulsion1 - 700  # Diminuer significativement l'impulsion pour le servo 1
    if impulsion2 > 500 and impulsion2 < 2500:  # Vérifier que l'impulsion est dans la plage valide
        impulsion2 = impulsion2 + 400  # Augmenter significativement l'impulsion pour le servo 2
    sleep(250)  # Pause de 250 ms
    display.clear()  # Effacer l'affichage
    set_servo1(impulsion1)  # Régler le servo 1
    set_servo2(impulsion2)  # Régler le servo 2
    sleep(1000)  # Pause de 1 seconde

# Boucle principale pour gérer les actions en fonction des entrées utilisateur
while 1 == 1:
    if button_a.was_pressed():  # Si le bouton A est pressé
        tourner_droite()  # Tourner à droite
    if button_b.was_pressed():  # Si le bouton B est pressé
        tourner_gauche()  # Tourner à gauche
    if pin_logo.is_touched():  # Si le logo est touché
        avancer()  # Avancer
    if accelerometer.was_gesture('shake'):  # Si le micro:bit détecte un mouvement de secousse
        reculer()  # Reculer
    if microphone.current_event() == SoundEvent.LOUD and impulsion1 != 1500 and impulsion2 != 1500:  # Si un son fort est détecté et les impulsions ne sont pas à leur valeur par défaut
        arret()  # Arrêter le robot
    if microphone.current_event() == SoundEvent.LOUD and impulsion1 == 1500 and impulsion2 == 1500:  # Si un son fort est détecté et les impulsions sont à leur valeur par défaut
        dash()  # Faire