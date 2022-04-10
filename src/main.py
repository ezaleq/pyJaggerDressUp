from scenemanager import SceneManager
import pygame, sys
pygame.init()

build_size = width, height = 1920, 1080

# Window configuration
pygame.display.set_caption("Jagger Dress Up")
screen = pygame.display.set_mode(build_size, pygame.WINDOWMINIMIZED)
icon = pygame.image.load("resources/interface/icon.png").convert_alpha()
bg = pygame.image.load("resources/interface/fondo.png").convert()
pygame.display.set_icon(icon)
sceneManager = SceneManager(build_size, bg)
clock = pygame.time.Clock()

while True:
    pygame.display.update()
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        sceneManager.event(event)
    sceneManager.update(screen)