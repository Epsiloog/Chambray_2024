import time
import RPi.GPIO as GPIO
import keyboard
import ultra

Motor_A_EN    = 4 ;  Motor_A_Pin1  = 26 ; Motor_A_Pin2  = 21
Motor_B_EN    = 17 ;  Motor_B_Pin1  = 27 ; Motor_B_Pin2  = 18

#GPIO.setmode(GPIO.BCM)

Dir_forward   = 1
Dir_backward  = 0
left_forward  = 1
left_backward = 0
right_forward = 1
right_backward= 0

pwm_A = 0
pwm_B = 0

def ms():#Arrêt des moteurs (moteur stop)
	GPIO.output(Motor_A_Pin1, GPIO.LOW)
	GPIO.output(Motor_A_Pin2, GPIO.LOW)
	GPIO.output(Motor_B_Pin1, GPIO.LOW)
	GPIO.output(Motor_B_Pin2, GPIO.LOW)
	GPIO.output(Motor_A_EN, GPIO.LOW)
	GPIO.output(Motor_B_EN, GPIO.LOW)


def setup():#Initialisation des moteurs
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


def motor_left(status, direction, speed):       #Moteur gauche rotation positive ou négative
	if status == 0: # stop
		GPIO.output(Motor_B_Pin1, GPIO.LOW)
		GPIO.output(Motor_B_Pin2, GPIO.LOW)
		GPIO.output(Motor_B_EN, GPIO.LOW)
	else:
		if direction == Dir_backward:
			GPIO.output(Motor_B_Pin1, GPIO.HIGH)
			GPIO.output(Motor_B_Pin2, GPIO.LOW)
			pwm_B.start(100)
			pwm_B.ChangeDutyCycle(speed)
		elif direction == Dir_forward:
			GPIO.output(Motor_B_Pin1, GPIO.LOW)
			GPIO.output(Motor_B_Pin2, GPIO.HIGH)
			pwm_B.start(0)
			pwm_B.ChangeDutyCycle(speed)


def motor_right(status, direction, speed):      #Moteur gauche rotation positive ou négative
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


def move(speed, direction, turn, radius=0.6):   # 0 < radius <= 1
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

def Avance(speed):
	motor_left(1, 1, speed)
	motor_right(1, 1, speed)

def Recule(speed):
	motor_left(1, 0, speed)
	motor_right(1, 0, speed)

def destroy():
	ms()
	GPIO.cleanup()             # Libère des ressources systèmes

if __name__ == '__main__':
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

ms()
speed = 100
direc = ['no']      #variable de type list pour pouvoir y accéder dans une fonction locale (global "var" pas encore trouvé)

while True :

	def Avancer():
		Avance(speed)
		direc[0] = 'forward'
	keyboard.add_hotkey('up', Avancer)

	def Reculer():
		Recule(speed)
		direc[0] = 'backward'
	keyboard.add_hotkey('down', Reculer)

	def Pause():
		ms()
		direc[0] = 'no'
	keyboard.add_hotkey('space', Pause)

	def Gauche():
		move(speed,direc[0],'left',radius=0.3)
	keyboard.add_hotkey('left', Gauche)

	def Droite():
		move(speed,direc[0],'right',radius=0.3)
	keyboard.add_hotkey('right', Droite)

	def Arrêt():
		ms()
		exit()
	keyboard.add_hotkey('alt', Arrêt)

	def Affiche():
		print('Vitesse :', speed)
		print(direc)
		print('Distance à un obstacle :',ultra.checkdist())
	keyboard.add_hotkey('a', Affiche)

	keyboard.wait()


"""
while running:

	if bd[1,0].is_pressed==True:
			Avance(100)
			direc[0]='forward'
	elif bd[1,2].is_pressed==True:
			Recule(100)
			direc[0]='backward'

	elif bd[0,1].is_pressed==True:
			move(speed,direc[0],'left',radius=0.5)
	elif bd[2,1].is_pressed==True:
			move(speed,direc[0],'right',radius=0.5)

	elif bd[1,1].is_pressed==True:
            ms()
            direc[0]='no'

	elif bd[0,0].is_pressed:
		ms()
		running=False

	if bd[2,0].when_released:
            LED.led.colorWipe(LED.Color(Couleurs[indice][0],Couleurs[indice][1],Couleurs[indice][2]))
            if indice==5:
                indice=0
            else:
                indice+=1
"""
"""elif bd[1,1].is_double_press==True:
arret()"""
"""
bd.stop()
print("") ; print('The Bluetooth server has been stopped.') ; print('See you soon ;)')
exit()"""


