from pygame import Surface

from components.gameobject import GameObject
from typing import List, Tuple


class Scene:
    object_list : List[GameObject] = []
    def __init__(self, sceneManager):
        self._sceneManager = sceneManager

    def update(self, screen : Surface):
        for object in self.object_list:
            object.update(screen)