from typing import List
import pygame

from components.gameobject import GameObject

class Jagger(GameObject):
    def __init__(self, x : int, y : int, scale : int, object_list : List[GameObject] , width = None, height = None):
        jagger_image = pygame.image.load('resources/interface/jagger/base.png').convert_alpha()
        GameObject.__init__(self, x, y, jagger_image, scale, width, height)
        self.load_layers(self, x, y, scale, object_list)

    def load_layers(self, x : int, y : int, scale : int, object_list : List[GameObject]):
        pass



