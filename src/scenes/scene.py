from pygame import Surface
import pygame

from components.gameobject import GameObject
from typing import List


class Scene:
    object_list : List[GameObject] = []
    def __init__(self, sceneManager):
        self._sceneManager = sceneManager
        soundButton = self.load_soundButton()

        self.object_list.append(soundButton)

    def load_soundButton(self):
        soundButton_image = pygame.image.load("resources/interface/sound/on.png").convert_alpha()
        soundButton = GameObject(
            x = 10,
            y = 10,
            image = soundButton_image,
            scale = 0.3
        )
        return soundButton

    def update(self, screen : Surface):
        for object in self.object_list:
            object.update(screen)