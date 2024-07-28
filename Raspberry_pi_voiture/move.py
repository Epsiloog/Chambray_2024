import RPi.GPIO as GPIO
from time import sleep

from bluedot import BlueDot     # Importations du module Bluedot pour l'application mobile
from signal import pause        # Importation de la méthode pause du module signal (permet de gérer les évènement/signaux non réguliers dans le temps).

# Cette partie permet de créer les boutons affichés sur l'application mobile
bd = BlueDot(cols=3,rows=3) # crée un "tableau' composé de 9 boutons (3 lignes, 3 colonnes)
bd.wait_for_connection()    # attend une connection avant d'executer la suite des instructions.
bd[0,1].square,bd[1,0].square,bd[2,1].square,bd[1,2].square=True,True,True,True
bd[0,1].color, bd[1,0].color, bd[2,1].color, bd[1,2].color =(113,125,126),(113,125,126),(113,125,126),(113,125,126) # Boutons directionnels
bd[0,0].visible,bd[0,2].visible,bd[2,0].visible,bd[2,2].visible=False,False,False,False

bd[1,1].color=(166,29,29) ; bd[1,1].border=True ; bd[1,1].double_press_time=0.2 # Bouton du milieu (rouge/bordure) pour stopper le robot, le server BT & le programme (double tap dans un intervalle de temps de 0.2s)

# Definition des pins
M1_En = 21
M1_In1 = 20
M1_In2 = 16
M2_En = 18
M2_In1 = 23
M2_In2 = 24

# Creation d'une liste des pins pour chaque moteur pour compacter la suite du code
Pins = [[M1_En, M1_In1, M1_In2], [M2_En, M2_In1, M2_In2]]

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(M1_En, GPIO.OUT)
GPIO.setup(M1_In1, GPIO.OUT)
GPIO.setup(M1_In2, GPIO.OUT)
GPIO.setup(M2_En, GPIO.OUT)
GPIO.setup(M2_In1, GPIO.OUT)
GPIO.setup(M2_In2, GPIO.OUT)

M1_Vitesse = GPIO.PWM(M1_En, 100)
M2_Vitesse = GPIO.PWM(M2_En, 100)
M1_Vitesse.start(100)
M2_Vitesse.start(100)

def sens1(moteurNum) :
	GPIO.output(Pins[moteurNum - 1][1], GPIO.HIGH)
	GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
	print("Moteur", moteurNum, "tourne dans le sens 1.")

def sens2(moteurNum) :
	GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
	GPIO.output(Pins[moteurNum - 1][2], GPIO.HIGH)
	print("Moteur", moteurNum, "tourne dans le sens 2.")

def arret(moteurNum) :
	GPIO.output(Pins[moteurNum - 1][1], GPIO.LOW)
	GPIO.output(Pins[moteurNum - 1][2], GPIO.LOW)
	print("Moteur", moteurNum, "arret.")

def ms():
    """
    ms comme Motor Stop
    """
    GPIO.output(Pins[0][1], GPIO.LOW)
    GPIO.output(Pins[0][2], GPIO.LOW)
    GPIO.output(Pins[1][1], GPIO.LOW)
    GPIO.output(Pins[1][2], GPIO.LOW)
    print("Moteurs arretes.")
bd[1,1].when_pressed=ms       #Appel de la fonction ms() lorsque le bouton du milieu est appuyé
ms()

def avance():
    sens2(1)
    sens2(2)
bd[1,0].when_pressed=avance

def recule():
    sens1(1)
    sens1(2)
bd[1,2].when_pressed=recule

def gauche():
    sens2(2)
    sens1(1)
bd[0,1].when_pressed=gauche

def droit():
    sens1(2)
    sens2(1)
bd[2,1].when_pressed=droit

def fin():
    ms()
    print(" \nLe server Bluetooth va être stoppé.\nA bientôt ;)")
    bd.stop()
    exit()
bd[1,1].when_double_pressed=fin

def test():

    avance()
    sleep(0.15)
    recule()
    sleep(0.15)
    avance()
    sleep(0.15)
    recule()
    sleep(0.15)
    ms()

if __name__=="__main__":
    test()