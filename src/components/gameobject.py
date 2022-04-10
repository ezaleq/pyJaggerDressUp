from pygame.sprite import Sprite
from pygame import Surface
from PIL import Image
import pygame

class GameObject(Sprite):
    def __init__(self, x : int, y : int, image : Surface, scale : float, width = None, height = None):
        Sprite.__init__(self)
        if width == None:
            width = image.get_width()
        if height == None:
            height = image.get_height()
        self.image = pygame.transform.scale(image, ((width * scale), (height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, screen : Surface):
        self.draw(screen)

    def draw(self, screen : Surface):
        screen.blit(self.image, self.rect)