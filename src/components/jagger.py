import pygame
from pygame.sprite import Sprite
from PIL import Image

class Jagger(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load('resources/interface/dress/base.png').convert_alpha()


