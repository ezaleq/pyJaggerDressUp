from pygame import Surface
from components.button import Button
import pygame

from components.gameobject import GameObject
from typing import List

from components.soundmanager import SoundManager

class Scene:
    object_list : List[GameObject] = []
    sound_manager : SoundManager
    def __init__(self, sceneManager):
        self.object_list = []
        self._sceneManager = sceneManager
        self.sound_manager = sceneManager.sound_manager
        sound_button = self.load_soundButton()
        self.object_list.append(sound_button)

    def event(self, event : pygame.event):
        for obj in self.object_list:
            obj.listen_event(event)

    def load_soundButton(self):
        bOn_image = pygame.image.load("resources/interface/sound/on.png").convert_alpha()
        bOff_image = pygame.image.load("resources/interface/sound/off.png").convert_alpha()
        soundButton = Button(
            x = 10,
            y = 10,
            image = bOn_image,
            scale = 0.3
        )
        def onClick():
            self.sound_manager.play(SoundManager.CLICK)
            self.sound_manager.toggle()
            if self.sound_manager.muted:
                soundButton.change_image(bOff_image, 0.3)
            else:
                soundButton.change_image(bOn_image, 0.3)

        soundButton.onClick = onClick
        return soundButton

    def update(self, screen : Surface):
        for object in self.object_list:
            object.update(screen)