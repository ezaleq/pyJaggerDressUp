from scenemanager import SceneManager
import pygame, sys
pygame.init()

build_size = width, height = 1920, 1080
icon = pygame.image.load("resources/interface/icon.png")
bg = pygame.image.load("resources/interface/fondo.png")

# Window configuration
pygame.display.set_caption("Jagger Dress Up")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(build_size, pygame.FULLSCREEN)
sceneManager = SceneManager(build_size, bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                screen = pygame.display.set_mode(build_size, pygame.RESIZABLE)
            if event.key == pygame.K_s:
                screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

    sceneManager.update(screen)
    pygame.display.update()