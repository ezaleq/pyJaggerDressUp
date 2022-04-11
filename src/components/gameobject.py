from pygame.sprite import Sprite
from pygame import Surface
from PIL import Image
import pygame

class GameObject(Sprite):
    layer : int
    def __init__(self, x : int, y : int, image : Surface, scale : float, width = None, height = None, layer = 0, outline = False, position = False, debug = False, keep_aspect_ratio = False):
        # Debug options
        self._debug = debug
        self._draw_position = position
        self._draw_outline = outline
        self._drag = False

        Sprite.__init__(self)
        self.original_pos = (x, y)
        self.change_image(image, scale, width, height, keep_aspect_ratio)
        self.layer = layer

    def change_image(self, image : Surface, scale : float, width = None, height = None, keep_aspect_ratio = False):
        if width == None:
            width = image.get_width()
        if height == None:
            height = image.get_height()
        if image:
            if keep_aspect_ratio:
                self.image = GameObject.resize_to_aspect_ratio(image, (width, height))
            else:
                self.image = pygame.transform.scale(image, ((width * scale), (height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = self.original_pos
        else:
            self.image = None

    def resize_to_aspect_ratio(img, size):
        bx, by = size
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

    def change_position(self, x_y : tuple[int, int]):
        if self.image:
            self.rect.topleft = x_y

    def draw_position(self, screen : Surface):
        if self._draw_position:
            font = pygame.font.SysFont("monospace", 20)
            text = font.render(f"({self.rect.x}, {self.rect.y})" , False, (0, 0, 0))
            screen.blit(text, (self.rect.x, self.rect.y))

    def draw_outline(self, screen : Surface):
        if self._draw_outline:
            pygame.draw.rect(screen, (254, 235, 254), self.rect, 12)

    def get_wcenter(screen_size : tuple[int, int], width_image : int, scale = 1):
        return (screen_size[0] / 2) - (width_image * scale / 2)

    def get_hcenter(screen_size : tuple[int, int], height_image : int, scale = 1):
        return (screen_size[1] / 2) - (height_image * scale / 2)

    def update(self, screen : Surface):
        self.draw(screen)

    def draw(self, screen : Surface):
        if self.image:
            screen.blit(self.image, self.rect)
            self.draw_position(screen)
            self.draw_outline(screen)

    def listen_event(self, event: pygame.event):
        if self._debug:
            if event.type == pygame.KEYUP:
                pos = pygame.mouse.get_pos()
                if event.key == pygame.K_o and self.rect.collidepoint(pos):
                    self._draw_outline = not self._draw_outline
                if event.key == pygame.K_p and self.rect.collidepoint(pos):
                    self._draw_position = not self._draw_position
                if event.key == pygame.K_d and self.rect.collidepoint(pos):
                    self._drag = not self._drag

            if event.type == pygame.MOUSEMOTION and self._drag:
                pos = pygame.mouse.get_pos()
                self.rect.topleft = pos
