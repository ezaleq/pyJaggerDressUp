import pygame
from components.inventory import Inventory
from scenes.scene import Scene
from components.jagger import Jagger

class DressScene(Scene):
    def __init__(self, sceneManager):
        super().__init__(sceneManager)

        self.load_background()
        self.load_inventory()
        self.load_jagger()

    def load_jagger(self):
        jagger_obj = Jagger(40, 0, 0.31, self.object_list)
        self.object_list.append(jagger_obj)

    def load_background(self):
        pass

    def load_inventory(self):
        inventory = Inventory(x = 782, y = 181, width = 900, height = 700, object_list = self.object_list)
        self.object_list.append(inventory)
