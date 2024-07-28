import RPi.GPIO as GPIO
import time

Tr=11
Ec=8

def checkdist(): # Fonction permettant de calculer la distance à un obstacle
    GPIO.setwarnings(False) #
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(Ec, GPIO.IN)
    GPIO.output(Tr, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Tr, GPIO.LOW)
    while not GPIO.input(Ec):  # Lorsque le signal n'est pas reçu (pas d'obstacle)
        pass
    t1 = time.time() #Calcule le temps passé dans la boucle
    while GPIO.input(Ec):
        pass
    t2 = time.time()
    print(round((t2-t1)*340/2,4)) # calcul de la distance à l'aide d'une formule à partir du temps et de la vitesse (arrondi à 4 chiffres après la virgule)


