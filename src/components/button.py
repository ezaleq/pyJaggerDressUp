import pygame
from components.gameobject import GameObject

class Button(GameObject):
    pass

    def listen_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                self.onClick()

    def onClick(self):
        pass
