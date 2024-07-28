import pygame
from time import sleep

running = True
pygame.init()
screen = pygame.display.set_mode((800,800))

while running:
    screen.fill((255,128,0))
    pygame.display.flip()
    sleep(0.5)
    screen.fill((128,255,0))
    pygame.display.flip()
    sleep(0.5)
    screen.fill((0,255,128))
    pygame.display.flip()
    sleep(0.5)
    screen.fill((0,128,255))
    pygame.display.flip()
    sleep(0.5)
    screen.fill((128,0,255))
    pygame.display.flip()
    sleep(0.5)
    screen.fill((255,0,128))
    pygame.display.flip()
    sleep(0.5)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running=False
