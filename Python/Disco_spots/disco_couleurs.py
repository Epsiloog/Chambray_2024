import pyaudio
import numpy as np
import scipy.fftpack
import pygame
import sys

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

# Initialiser Pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Visualisation Audio")
clock = pygame.time.Clock()

try:
    while True:
        # Lire les données audio
        data = stream.read(CHUNK, exception_on_overflow=False)
        # Convertir les données en tableau numpy
        audio_data = np.frombuffer(data, dtype=np.int16)
        
        # Analyser les données audio
        # Transformation de Fourier rapide
        fft_data = np.abs(scipy.fftpack.fft(audio_data))[:CHUNK//2]
        freq = np.fft.fftfreq(len(audio_data), 1.0/RATE)[:CHUNK//2]
        
        # Trouver la fréquence dominante
        freq_dominante = freq[np.argmax(fft_data)]
        intensite = np.max(fft_data)

        # Déterminer la couleur en fonction de la fréquence et de l'intensité
        rouge = int(min(255, freq_dominante / 2))
        vert = int(min(255, intensite / 1000))
        bleu = 255 - rouge

        # Afficher la couleur
        screen.fill((rouge, vert, bleu))

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Limiter le taux de rafraîchissement à 30 FPS
        clock.tick(30)

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
    sys.exit()
