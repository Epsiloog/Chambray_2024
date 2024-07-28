from bluedot import BlueDot     #Importations du module Bluedot pour l'application mobile
from signal import pause        # Importation de la méthode pause du module signal (permet de gérer les évènement/signaux non réguliers dans le temps).

import time
import RPi.GPIO as GPIO     # Les broches GPIO (General Purpose Input/Output), toutes connectée au HAT...
import LED,sounds           # "personnalisations" de la voiture : sons, lumières
#import ultra

# Cette partie permet de créer les boutons affichés sur l'application mobile
bd = BlueDot(cols=3,rows=3) # crée un "tableau' composé de 9 boutons (3 lignes, 3 colonnes)
bd[0,1].square=True ; bd[1,0].square=True ; bd[2,1].square=True ; bd[1,2].square=True
bd[0,1].color, bd[1,0].color, bd[2,1].color, bd[1,2].color =(113,125,126),(113,125,126),(113,125,126),(113,125,126) # Boutons directionnels
bd[0,2].visible=False

bd[1,1].color=(166,29,29) ; bd[1,1].border=True ; bd[1,1].double_press_time=0.2 # Bouton du milieu pour stopper le robot ou le server BT & programme
bd[0,0].color='blue' # Couleur des boutons
bd[2,0].color='red'
bd[2,2].color=(0, 205, 205) ; bd[2,2].border=True
#bd[0,2].visible=False ; bd[0,2].border=True

LED.led.colorWipe(LED.Color(0,0,0)) # On initialise (à l'aide d'une méthode importée d'un autre fichier python) les LED éteintes

# Variables correspondant aux moteurs du robot.
Motor_A_EN    = 4
Motor_B_EN    = 17
Motor_A_Pin1  = 26
Motor_A_Pin2  = 21
Motor_B_Pin1  = 27
Motor_B_Pin2  = 18

# Intitialisation des différentes directions avec des booléens
Dir_forward   = 1 ; left_forward  = 1 ; right_forward = 1
Dir_backward  = 0 ; left_backward = 0 ; right_backward= 0

# Variables permettant de contrôler la puissance des moteurs de chaque côté
pwm_A,pwm_B = 0,0

def setup(): # Permet de mettre en place les moteurs (qui ne marchent pas au début)
	global pwm_A, pwm_B
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Motor_A_EN, GPIO.OUT)
	GPIO.setup(Motor_B_EN, GPIO.OUT)
	GPIO.setup(Motor_A_Pin1, GPIO.OUT)
	GPIO.setup(Motor_A_Pin2, GPIO.OUT)
	GPIO.setup(Motor_B_Pin1, GPIO.OUT)
	GPIO.setup(Motor_B_Pin2, GPIO.OUT)

	ms()
	try:
		pwm_A = GPIO.PWM(Motor_A_EN, 1000)
		pwm_B = GPIO.PWM(Motor_B_EN, 1000)
	except:
		pass

def ms():# Fonction permettant de stopper les moteurs (voiture sera immobile)
	GPIO.output(Motor_A_Pin1, GPIO.LOW)
	GPIO.output(Motor_A_Pin2, GPIO.LOW)
	GPIO.output(Motor_B_Pin1, GPIO.LOW)
	GPIO.output(Motor_B_Pin2, GPIO.LOW)
	GPIO.output(Motor_A_EN, GPIO.LOW)
	GPIO.output(Motor_B_EN, GPIO.LOW)

def motor_left(status, direction, speed): # Fonction permettant de faire tourner les roues de la partie gauche en fonction de la direction
	if status == 0:
		GPIO.output(Motor_B_Pin1, GPIO.LOW)
		GPIO.output(Motor_B_Pin2, GPIO.LOW)
		GPIO.output(Motor_B_EN, GPIO.LOW)
	else:
		if direction == Dir_backward:
			GPIO.output(Motor_B_Pin1, GPIO.HIGH)
			GPIO.output(Motor_B_Pin2, GPIO.LOW)
			pwm_B.start(100)
			pwm_B.ChangeDutyCycle(speed) # Change la fréquence de rotation des roues à une fréquence variable.
		elif direction == Dir_forward:
			GPIO.output(Motor_B_Pin1, GPIO.LOW)
			GPIO.output(Motor_B_Pin2, GPIO.HIGH)
			pwm_B.start(0)
			pwm_B.ChangeDutyCycle(speed)


def motor_right(status, direction, speed):# Fonction permettant de faire tourner les roues de la partie droite en fonction de la direction
	if status == 0: # stop
		GPIO.output(Motor_A_Pin1, GPIO.LOW)
		GPIO.output(Motor_A_Pin2, GPIO.LOW)
		GPIO.output(Motor_A_EN, GPIO.LOW)
	else:
		if direction == Dir_backward:
			GPIO.output(Motor_A_Pin1, GPIO.HIGH)
			GPIO.output(Motor_A_Pin2, GPIO.LOW)
			pwm_A.start(speed)
			pwm_A.ChangeDutyCycle(speed)
		elif direction == Dir_forward:
			GPIO.output(Motor_A_Pin1, GPIO.LOW)
			GPIO.output(Motor_A_Pin2, GPIO.HIGH)
			pwm_A.start(0)
			pwm_A.ChangeDutyCycle(speed)


def move(speed, direction, turn, radius=0.4):   # Fonction générale qui sera utilisée pour tourner, elle s'appuie sur les fonctions précédenets
	#speed = 100
	if direction == 'forward':
		if turn == 'right':
			motor_left(0, left_backward, int(speed*radius))
			motor_right(1, right_forward, speed)
		elif turn == 'left':
			motor_left(1, left_forward, speed)
			motor_right(0, right_backward, int(speed*radius))
		else:
			motor_left(1, left_forward, speed)
			motor_right(1, right_forward, speed)
	elif direction == 'backward':
		if turn == 'right':
			motor_left(0, left_forward, int(speed*radius))
			motor_right(1, right_backward, speed)
		elif turn == 'left':
			motor_left(1, left_backward, speed)
			motor_right(0, right_forward, int(speed*radius))
		else:
			motor_left(1, left_backward, speed)
			motor_right(1, right_backward, speed)
	elif direction == 'no':
		if turn == 'right':
			motor_left(1, left_backward, speed)
			motor_right(1, right_forward, speed)
		elif turn == 'left':
			motor_left(1, left_forward, speed)
			motor_right(1, right_backward, speed)
		else:
			ms()
	else:
		pass

def Avance(speed): # Fonction qui va permettre d'avancer
	motor_left(1, 1, speed)
	motor_right(1, 1, speed)

def Recule(speed): # Fonction qui va permettre de reculer
	motor_left(1, 0, speed)
	motor_right(1, 0, speed)

def destroy(): # Fonction qui permet d'arrêter complètement le fonctionnement de la voiture
	ms()
	GPIO.cleanup()

if __name__ == '__main__': # Au lancement du programme, la voiture va se "setup" toute seule, on pourra ensuite la contrôler
	try:
		speed_set = 100
		setup()
		motor_left(1, 1, speed_set)
		motor_right(1, 1, speed_set)
		time.sleep(0.1)
		motor_left(1, 0, speed_set)
		motor_right(1, 0, speed_set)
		time.sleep(0.1)
		motor_left(1, 1, speed_set)
		motor_right(1, 1, speed_set)
		time.sleep(0.1)
		motor_left(1, 0, speed_set)
		motor_right(1, 0, speed_set)
		time.sleep(0.1)
	except KeyboardInterrupt:
		destroy()

ms() # initalisation des variables permettant de contrôler la voiture comme on le souhaite
speed = 100
direc = 'no'

Couleurs=[[255,0,0],[0,255,0],[0,255,255],[255,165,0],[0,0,255],[255,0,255],\
[255,255,255],[0,0,0]] # Listes contenant les valeurs RGB de différentes couleurs pour les LED

indice=0 # initilisation des indices dans les listes permettant de changer la couleur des LED et des boutons.
indice_pp=0
indice_cf=0

# Utilisations de fonctions associés à chaque bouton qui seront effectuées en fonction des actions de l'utilisateur
def forward():
    global direc
    Avance(100)
    direc='forward'
bd[1,0].when_pressed=forward # ce qui permet de lancer les fonctions lorsque l'utilisateur fait une action sur un bouton

def backward():
    global direc
    Recule(100)
    direc='backward'
bd[1,2].when_pressed=backward

def left():
    global direc
    move(speed,direc,'left',radius=0.6)
bd[0,1].when_pressed=left

def right():
    global direc
    move(speed,direc,'right',radius=0.6)
bd[2,1].when_pressed=right

def arret():
    global direc
    ms()
    direc='no'
bd[1,1].when_pressed=arret

def fin():
    ms()
    LED.led.colorWipe(LED.Color(0,0,0))
    print(" \nLe server Bluetooth a été stoppé.\nA bientôt ;)")
    bd.stop()
    exit()
bd[1,1].when_double_pressed=fin

def colors():
    global indice # Permet dans ce cas de changer la valeur d'une variable dans une fonction : rend cette variable globale donc aussi locale à la fonction
    print("Les LED se sont allumés pour red=",Couleurs[indice][0],"green=",Couleurs[indice][1],"blue=",Couleurs[indice][2])
    LED.led.colorWipe(LED.Color(Couleurs[indice][0],Couleurs[indice][1],Couleurs[indice][2])) # On change la couelr des LED
    if indice !=7: # Change la couleur du bouton qui affiche la prochaine couleur des LED sur le robot
        indice+=1
        bd[2,0].color=(Couleurs[indice][0],Couleurs[indice][1],Couleurs[indice][2])
    else:
        indice=0
        bd[2,0].color=(Couleurs[indice][0],Couleurs[indice][1],Couleurs[indice][2])
bd[2,0].when_pressed=colors

def police_pompier():
    global indice_pp
    if indice_pp==0:    # En fonction de la valeur de l'indice, on lance le mode pompier ou police
        #sounds.police_song()
        LED.police()
        indice_pp=1
        bd[0,0].color='red'
    else:
        #sounds.pompier_song()
        LED.pompier()
        indice_pp=0
        bd[0,0].color='blue'
bd[0,0].when_pressed=police_pompier

def color_fun(): # Permet le changement des couleurs des LED avec plus de possibilités à l'aide de fonctions importées
    global indice_cf
    if indice_cf==0:
        bd[2,2].color='yellow'
        LED.degrade()
        indice_cf=1
    else:
        bd[2,2].color=(0, 205, 205)
        LED.spot_pastel()
        indice_cf=0
bd[2,2].when_pressed=color_fun

pause() # pause attend qu'un nouveau signal arrive pour relancer l'aquisition d'un signal et donc de l'execution des fonctions ci dessus.


"""
def degrade():
    try:
        for i in range(2):
            for blue_to_cyan in range(255):
                if bd[1,1].is_pressed:
                    raise StopIteration
                LED.led.colorWipe(LED.Color(0,blue_to_cyan,255))
            for cyan_green in range(255):
                if bd[1,1].on_pressed:
                    raise StopIteration
                LED.led.colorWipe(LED.Color(0,255,255-cyan_green))
            for green_yellow in range(255):
                LED.led.colorWipe(LED.Color(green_yellow,255,0))
            for yellow_red in range(255):
                LED.led.colorWipe(LED.Color(255,255-yellow_red,0))
            for red_pink in range(255):
                LED.led.colorWipe(LED.Color(255,0,red_pink))
            for pink_blue in range(255):
                LED.led.colorWipe(LED.Color(255-pink_blue,0,255))
    except StopIteration:
        print("Sortie de la boucle")
        pass
"""
