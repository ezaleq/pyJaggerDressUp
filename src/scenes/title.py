import pygame
from components.gameobject import GameObject
from scenes.scene import Scene
from components.button import Button

class TitleScene(Scene):
    def __init__(self, sceneManager):
        super().__init__(sceneManager)
        start_image = pygame.image.load("resources/interface/title/start.png")
        titleDeco_image  = pygame.image.load("resources/interface/title/title deco.png")

        titleDeco_object = GameObject(0, 100, titleDeco_image, 1, self.screen, 772.8, 1005.6, True)
        startButton_object = Button(255, 255, start_image , 1, self.screen, 400, 400, True)

        self.object_list.append(titleDeco_object)
        self.object_list.append(startButton_object)


