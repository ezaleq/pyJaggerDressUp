import pygame, sys
from components.button import Button
from components.jagger import Jagger
from scenemanager import SceneManager
pygame.init()

size = width, height = 800, 600
icon = pygame.image.load("resources/interface/icon.png")
bg = pygame.image.load("resources/interface/fondo.png")

# Window configuration
pygame.display.set_caption("Jagger Dress Up")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(size, pygame.SHOWN)
sceneManager = SceneManager(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(bg, (0,0))
    sceneManager.update()
    pygame.display.flip()