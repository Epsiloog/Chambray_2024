# Créé par Thomas, le 23/05/2022 en Python 3.7
from pygame import mixer
import time
mixer.init()
mixer.music.load("/home/pi/Adeept_modifié/server/sounds/bruit-de-demarrage-voiture-2s.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
print('Moteur démarré.')
time.sleep(2)
#exit()
