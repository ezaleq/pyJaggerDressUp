from scenes.dress import DressScene
from typing import List
import pygame
from components.gameobject import GameObject
from components.soundmanager import SoundManager
from scenes.scene import Scene
from components.button import Button

class TitleScene(Scene):
    def __init__(self, sceneManager):
        super().__init__(sceneManager)
        start_button, button_background = self.load_button(sceneManager)
        jagger_background = self.load_jaggerbg()
        logo = self.load_logo(sceneManager, button_background.rect.y)

        self.object_list.append(jagger_background)
        self.object_list.append(start_button)
        self.object_list.append(button_background)
        self.object_list.append(logo)

    def load_logo(self, sceneManager, ypos_start : int) -> GameObject:
        logo_image = pygame.image.load("resources/interface/title/title logo.png").convert_alpha()
        return GameObject(
            x = GameObject.get_wcenter(sceneManager.build_size, logo_image.get_width(), 0.3),
            y = ypos_start - (logo_image.get_height() * 0.3) - 30,
            image = logo_image,
            scale = 0.3)

    def load_jaggerbg(self) -> GameObject:
        titleDeco_image  = pygame.image.load("resources/interface/title/title deco.png").convert_alpha()
        return GameObject(0, 100, titleDeco_image, 0.3)

    def load_button(self, sceneManager) -> List[GameObject]:
        start_image = pygame.image.load("resources/interface/title/start.png").convert_alpha()
        button_background_image = pygame.image.load("resources/interface/cuadrito.png").convert_alpha()

        start_image_scale = 0.3
        himage_resized = (start_image.get_height() * start_image_scale)

        def onClick():
            self.sound_manager.play(SoundManager.CLICK)
            sceneManager.load_scene(DressScene(sceneManager))


        start_button = Button(
            x = GameObject.get_wcenter(sceneManager.build_size, start_image.get_width(), start_image_scale),
            y = sceneManager.build_size[1] - himage_resized - 150,
            image = start_image,
            scale = start_image_scale
        )
        start_button.onClick = onClick

        button_background = GameObject(
            x = start_button.rect.x - 20,
            y = start_button.rect.y - 20,
            image = button_background_image,
            scale = 1,
            width = start_button.rect.width + 40,
            height = start_button.rect.height + 40
        )

        return [start_button, button_background]

    def __del__(self):
        print("elminado")
