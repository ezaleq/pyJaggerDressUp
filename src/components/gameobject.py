from pygame.sprite import Sprite
from pygame import Surface
import pygame

class GameObject(Sprite):
    def __init__(self, x : int, y : int, image : Surface, scale : float, screen : Surface, width = None, height = None, preserveAspectRatio = False):
        self.originalScreenSize = (1920, 1080)
        self.screen = screen
        Sprite.__init__(self)
        if width == None:
            width = image.get_width()
        if height == None:
            height = image.get_height()

        width = self.getRelativeByWidth(width)
        height = self.getRelativeByHeight(height)
        if preserveAspectRatio:
            self.image = self.aspect_scale(image, width, height)
        else:
            self.image = pygame.transform.scale(image, ((width * scale), (height * scale)))
        # self.image = pygame.transformt.scale(self.image, (screen.get_width() / 1920, screen.get_height() / max))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def aspect_scale(self, img : Surface, bx : int, by : int):
        ix,iy = img.get_size()
        if ix > iy:
            # fit to width
            scale_factor = bx/float(ix)
            sy = scale_factor * iy
            if sy > by:
                scale_factor = by/float(iy)
                sx = scale_factor * ix
                sy = by
            else:
                sx = bx
        else:
            # fit to height
            scale_factor = by/float(iy)
            sx = scale_factor * ix
            if sx > bx:
                scale_factor = bx/float(ix)
                sx = bx
                sy = scale_factor * iy
            else:
                sy = by

        return pygame.transform.scale(img, (sx,sy))

    def update(self):
        self.draw()

    def draw(self):
        xpos = self.getRelativeByWidth(self.rect.x)
        ypos = self.getRelativeByHeight(self.rect.y)
        self.screen.blit(self.image, (xpos, ypos))

    def getRelativeByWidth(self, size : int):
        return self.screen.get_width() * size / self.originalScreenSize[0]

    def getRelativeByHeight(self, size : int):
        return self.screen.get_height() * size / self.originalScreenSize[1]
