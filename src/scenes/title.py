from turtle import title
import pygame
from components.gameobject import GameObject
from scenes.scene import Scene
from components.button import Button

class TitleScene(Scene):
    def __init__(self, sceneManager):
        super().__init__(sceneManager)
        start_image = pygame.image.load("resources/interface/title/start.png")
        titleDeco_image  = pygame.image.load("resources/interface/title/title deco.png")

        titleDeco_object = GameObject(0, 100, titleDeco_image, 0.2,)
        startButton_object = Button(0, 0, start_image , 0.2)

        self.object_list.append(titleDeco_object)
        self.object_list.append(startButton_object)


