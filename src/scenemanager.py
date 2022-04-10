from typing import Tuple
from pygame import Surface
import pygame
from soundmanager import SoundManager
import scenes.scene as scene
from scenes.title import TitleScene

class SceneManager:
    _actualScene : scene.Scene = None
    def __init__(self, build_size : Tuple[int, int], bg : Surface):
        self.sound_manager = SoundManager()
        self.build_size = build_size
        self._bg = bg
        self.load_scene(TitleScene(self))
        self.load_fonts()
        self.dummy = pygame.Surface(self.build_size)

    def load_fonts(self):
        pygame.font.init()
        self.font = pygame.font.Font("resources/fonts/Liminality-Regular.ttf", 20)


    def load_scene(self, scene):
        if self._actualScene:
            del self._actualScene
        self._actualScene = scene

    def update(self, screen : Surface):
        self.dummy.blit(self._bg, (0,0))
        self._actualScene.update(self.dummy)
        resized = pygame.transform.scale(self.dummy, screen.get_size(), screen)
        screen.blit(resized, (0,0))

    def event(self, event : pygame.event):
        self._actualScene.event(event)