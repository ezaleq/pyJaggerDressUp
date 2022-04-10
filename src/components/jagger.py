import json
from typing import List
import pygame

from components.gameobject import GameObject


class ClothLayer(GameObject):
    category_name : str = ""
    def __init__(self, x : int, y : int, width : int, height : int, category : str, layer : int):
        super().__init__(x, y, None, 1, width, height, layer)
        self.category_name = category

class Jagger(GameObject):
    cloth_layers : List[ClothLayer] = []
    def __init__(self, x : int, y : int, scale : int, object_list : List[GameObject] , width = None, height = None):
        jagger_image = pygame.image.load('resources/interface/jagger/base.png').convert_alpha()
        GameObject.__init__(self, x, y, jagger_image, scale, width, height, 1)
        self.load_layers(x, y, object_list)

    def load_layers(self, x : int, y : int, object_list : List[GameObject]):
        with open("config/cloth_config.json", "r") as file:
            configuration = json.load(file)
        layer = 2
        for category in configuration["categories"]:
            self.cloth_layers.append(ClothLayer(x, y, self.rect.width, self.rect.height, category, layer))
            layer += 1
        object_list.extend(self.cloth_layers)

