from typing import Tuple
from pygame import BLEND_RGB_SUB, Surface
import pygame
import scenes.scene as scene
from scenes.title import TitleScene

class SceneManager:
    _actualScene : scene.Scene
    def __init__(self, build_size : Tuple[int, int], bg : Surface):
        self.build_size = build_size
        self.dummysurface = Surface(self.build_size)
        self._bg = bg
        self.load_scene(TitleScene(self))

    def load_scene(self, scene):
        self._actualScene = scene

    def update(self, screen : Surface):
        dummy = pygame.Surface(self.build_size)
        dummy.blit(self._bg, (0,0))
        self._actualScene.update(dummy)
        resized = pygame.transform.scale(dummy, screen.get_size(), screen)
        screen.blit(resized, (0,0))