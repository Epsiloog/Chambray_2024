#Importation des modules time et argparse
import time
#Importation de toutes les fonctions et méthodes de rpi_ws281x
from rpi_ws281x import *
import argparse     #argparse est un module permettant de "parser" du code, c'est à dire analyser et extraire des bouts de code et les enregistrer dans des fichiers grâce à des commandes
#il est notamment intéressant pour renvoyer des messages d'erreur qui n'apparaitraient pas en son absence

# configuration LEDs
LED_COUNT      = 6       # Nombre de pixels sur les LED
LED_PIN        = 12      # ports/broches GPIO connectées aux pixels
LED_FREQ_HZ    = 800000  # fréquence du signal des LEDS en Herz
LED_DMA        = 10      # canal Direct Memory Access utilisé pour générer le signal lumineux
LED_BRIGHTNESS = 255     # luminosité des LEDs (codé sur 255 bits)
LED_INVERT     = False   # Inversion du signal (couleurs opposées)
LED_CHANNEL    = 0       # Canal (GPIOs) utilisé pour ordonner l'allumage des LEDs

class LED:
    def __init__(self):
        self.LED_COUNT      = 6
        self.LED_PIN        = 12
        self.LED_FREQ_HZ    = 800000
        self.LED_DMA        = 10
        self.LED_BRIGHTNESS = 255
        self.LED_INVERT     = False
        self.LED_CHANNEL    = 0
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_true', help="efface l'affichage en sortie")
        args = parser.parse_args()

        # Création d'un objet NeoPixel avec les attributs de la méthode constructrice de la classe LED
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)
        # Initialise la bibliothèque (doit être appelé une fois avant les autres méthodes).
        self.strip.begin()

    # Définition d'une méthode qui allume les LEDs de différentes façons.
    def colorWipe(self, color, wait_ms=0):
        """Remplacer la couleur du nombre de pixels de LED_COUNT, un pixel à la fois.."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def colorWipe_bis(self, color1,color2,nb_pixels=6, wait_ms=0):
        """Cette méthode de la classe LED prend en argument 2 couleurs, le nb de pixel a allumer, et un temps d'attente.
           Elle affiche successivement la moitié du nb de pixels donnés puis l'autre moitié séparés par le temps d'attente."""
        for i in range(8):
            for j in range(nb_pixels//2):
                self.strip.setPixelColor(j, Color(color1[0],color1[1],color1[2]))
                self.strip.show()
            time.sleep(wait_ms/1000.0)
            for l in range(nb_pixels//2):
                self.strip.setPixelColor(l, Color(0,0,0))
                self.strip.show()
            for k in range(nb_pixels//2, nb_pixels):
                self.strip.setPixelColor(k, Color(color2[0],color2[1],color2[2]))
                self.strip.show()
            time.sleep(wait_ms/1000.0)
            for m in range(nb_pixels//2, nb_pixels):
                self.strip.setPixelColor(m, Color(0,0,0))
                self.strip.show()

    def colorWipe2(self,nb_pixel,p1,p2=None,p3=None,p4=None,p5=None,p6=None,nb_repetition=10, wait_time=0):
        """
        Cette méthode prend en argument le nb de pixels a allumer souhaités,
        des tuples pour les 6 pixels: (couleur, fréquence d'allumage),
        le nb de répétition de du cycle allumage/extinction
        et le temps mis pour allumer au départ le nb de pixels décidés.
        """
        LEDS=[p1,p2,p3,p4,p5,p6]
        for i in range(nb_pixel):
            self.strip.setPixelColor(i,Color(LEDS[i][0][0],LEDS[i][0][1],LEDS[i][0][2]))
            self.strip.show()
            time.sleep(wait_time)
        for j in range(nb_repetition):
            for i in range(nb_pixel):
                self.strip.setPixelColor(i,Color(LEDS[i][0][0],LEDS[i][0][1],(LEDS[i][0][2])))
                self.strip.show()
                time.sleep(LEDS[i][1])
                led.colorWipe(Color(0,0,0))
                time.sleep(LEDS[i][1])

led=LED()

def police():
    print('Gyrophares de police activés !')
    led.colorWipe_bis((255,0,0),(0,0,255),6,500)

def pompier():
    print('Pin Pon Pin Pon...')
    led.colorWipe_bis((255,0,0),(255,0,0),6,500)

def degrade():
    """ Fonction qui affiche les une à la suite des autres toutes les couleurs du cercle chromatique définis selon le code rgb (255^3 couleurs) """
    for i in range(2):
        for blue_to_cyan in range(255):
            led.colorWipe(Color(0,blue_to_cyan,255))
        for cyan_green in range(255):
            led.colorWipe(Color(0,255,255-cyan_green))
        for green_yellow in range(255):
            led.colorWipe(Color(green_yellow,255,0))
        for yellow_red in range(255):
            led.colorWipe(Color(255,255-yellow_red,0))
        for red_pink in range(255):
            led.colorWipe(Color(255,0,red_pink))
        for pink_blue in range(255):
            led.colorWipe(Color(255-pink_blue,0,255))

def spot_pastel():
    led.colorWipe2(6,((256,128,64),0.2),((64,256,128),0.2),((128,64,256),0.2),((256,128,64),0.2),((64,256,128),0.2),((128,64,256),0.2),8,0.3)


#boucle de test qui est réalisée uniquement si LED.py est exécutée (comme programme "main").
run=True
if __name__ == '__main__':
    while run==True:
        try:
            led.colorWipe(Color(255,0,0))
            time.sleep(1)
            led.colorWipe(Color(0,255,0))
            time.sleep(1)
            led.colorWipe(Color(0,0,255))
            time.sleep(1)
            led.colorWipe(Color(0,0,0))
            time.sleep(1)
            run=False
        except:
            led.colorWipe(Color(0,0,0))

