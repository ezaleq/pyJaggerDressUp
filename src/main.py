from scenemanager import SceneManager
import pygame, sys
pygame.init()

build_size = width, height = 1920, 1080

# Window configuration
pygame.display.set_caption("Jagger Dress Up")
screen = pygame.display.set_mode(build_size, pygame.FULLSCREEN)
icon = pygame.image.load("resources/interface/icon.png").convert_alpha()
bg = pygame.image.load("resources/interface/fondo.png").convert()
pygame.display.set_icon(icon)
sceneManager = SceneManager(build_size, bg)
clock = pygame.time.Clock()

# Font initialization 
pygame.font.init()
font = pygame.font.Font("resources/fonts/Liminality-Regular.ttf", 20)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    clock.tick(0)
    sceneManager.update(screen)
    fps = "{:.2f}".format(clock.get_fps())
    fps_surface = font.render(f"FPS: {fps}", False, (255, 255, 255))
    screen.blit(fps_surface, (500, 0))