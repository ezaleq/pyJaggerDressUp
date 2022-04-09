from pygame import Surface
from pygame.sprite import Sprite
from components.gameobject import GameObject

class Button(GameObject):
    def __init__(self, x : int, y : int, image : Surface, scale : float, screen : Surface, width = None, height = None, preserveAspectRatio = False):
        GameObject.__init__(self, x, y, image, scale, screen, width, height, preserveAspectRatio)