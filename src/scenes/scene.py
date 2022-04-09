from pygame import Surface

from components.gameobject import GameObject
from typing import List


class Scene:
    screen : Surface
    object_list : List[GameObject] = []

    def __init__(self, sceneManager):
        self._sceneManager = sceneManager
        self.screen = sceneManager._screen

    def update(self):
        for object in self.object_list:
            object.update()