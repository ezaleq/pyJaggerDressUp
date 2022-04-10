from pygame.sprite import Sprite
from pygame import Surface
from PIL import Image
import pygame

class GameObject(Sprite):
    layer : int
    def __init__(self, x : int, y : int, image : Surface, scale : float, width = None, height = None, layer = 0):
        Sprite.__init__(self)
        self.original_pos = (x, y)
        self.change_image(image, scale, width, height)
        self.layer = layer

    def change_image(self, image : Surface, scale : float, width = None, height = None):
        if width == None:
            width = image.get_width()
        if height == None:
            height = image.get_height()
        if image:
            self.image = pygame.transform.scale(image, ((width * scale), (height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = self.original_pos
        else:
            self.image = None

    def get_wcenter(screen_size, width_image, scale = 1):
        return (screen_size[0] / 2) - (width_image * scale / 2)

    def get_hcenter():
        pass

    def update(self, screen : Surface):
        self.draw(screen)

    def draw(self, screen : Surface):
        if self.image:
            screen.blit(self.image, self.rect)

    def listen_event(self, event: pygame.event):
        pass