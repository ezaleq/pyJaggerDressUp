from turtle import screensize
from typing import Tuple
from pygame import Surface
import pygame
from components.gameobject import GameObject
from soundmanager import SoundManager
import scenes.scene as scene
from scenes.title import TitleScene
from scenes.dress import DressScene


class SceneManager:
    _actualScene : scene.Scene = None
    def __init__(self, build_size : Tuple[int, int], bg : Surface, show_fps = False, show_mouse = False):
        self.show_fps = show_fps
        self.show_mouse = show_mouse
        self.clock = pygame.time.Clock()

        self.sound_manager = SoundManager()
        self.build_size = build_size
        self._bg = bg
        self.load_scene(DressScene(self))
        self.load_fonts()
        self.dummy = pygame.Surface(self.build_size)

    def load_fonts(self):
        pygame.font.init()
        self.font = pygame.font.Font("resources/fonts/Liminality-Regular.ttf", 20)


    def load_scene(self, scene):
        if self._actualScene:
            del self._actualScene
        self._actualScene = scene

    def draw_fps(self):
        if self.show_fps:
            formatted = "{:.2f}".format(self.clock.get_fps())
            text = self.font.render(f"FPS: {formatted}", False, (255, 255, 255), (0, 0, 0))
            wpos = GameObject.get_wcenter(self.dummy.get_size(), text.get_width(), 1)
            self.dummy.blit(text, (wpos, 0))

    def draw_mouse(self):
        if self.show_mouse:
            pos = pygame.mouse.get_pos()
            text = self.font.render(f"({pos[0]}, {pos[1]})", False, (255, 255, 255), (0, 0, 0))
            self.dummy.blit(text, pos)
    def update(self, screen : Surface):
        self.clock.tick(100)
        self.dummy.blit(self._bg, (0,0))
        self._actualScene.update(self.dummy)
        self.draw_fps()
        self.draw_mouse()
        resized = pygame.transform.scale(self.dummy, screen.get_size(), screen)
        screen.blit(resized, (0,0))

    def event(self, event : pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F2:
                self.show_fps = not self.show_fps
            if event.key == pygame.K_F3:
                self.show_mouse = not self.show_mouse

        self._actualScene.event(event)