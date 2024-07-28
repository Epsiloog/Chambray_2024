# Créé par Thomas, le 01/05/2022 en Python 3.7
from pygame import mixer

mixer.init()

mixer.music.load("../../../Users/Thomas/Music/course_voitures.mp3")

mixer.music.set_volume(0.7)

mixer.music.play()

while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input(" ")

    if query == 'p':
        mixer.music.pause()

    elif query == 'r':
        mixer.music.unpause()

    elif query == 'e':
        mixer.music.stop()
        break
