# Créé par Thomas, le 15/07/2024 en Python 3.12.4

import pyaudio
import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt
import pygame

# Paramètres de l'audio
FORMAT = pyaudio.paInt16  # Format des échantillons audio
CHANNELS = 1  # Nombre de canaux
RATE = 44100  # Taux d'échantillonnage
CHUNK = 1024  # Taille des chunks

# Initialiser PyAudio
p = pyaudio.PyAudio()

# Ouvrir le flux audio
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Enregistrement...")

# Visualisation avec Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Boucle principale
try:
    while True:
        screen.fill((255, 255, 255))

        # Lire les données audio
        data = stream.read(CHUNK)
        # Convertir les données en tableau numpy
        audio_data = np.frombuffer(data, dtype=np.int16)

        # Analyser les données audio
        # Transformation de Fourier rapide
        fft_data = np.abs(scipy.fftpack.fft(audio_data))[:CHUNK//2]
        freq = np.fft.fftfreq(len(audio_data), 1.0/RATE)[:CHUNK//2]

        # Trouver la fréquence dominante
        freq_dominante = freq[np.argmax(fft_data)]
        intensite = np.max(fft_data)

        print(f"Fréquence dominante: {freq_dominante} Hz, Intensité: {intensite}")

        # Déterminer la couleur et la taille en fonction de la fréquence et de l'intensité
        couleur = (int(min(255, freq_dominante / 2)), 0, int(min(255, intensite / 1000)))
        taille = int(min(100, intensite / 1000)) + 200

        # Dessiner une forme (par exemple, un cercle)
        pygame.draw.circle(screen, couleur, (400, 300), taille)

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Traiter les événements Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise KeyboardInterrupt

except KeyboardInterrupt:
    print("Arrêt du programme.")

finally:
    # Arrêter le flux et fermer PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    pygame.quit()
