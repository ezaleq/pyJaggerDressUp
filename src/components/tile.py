from components.gameobject import GameObject
from PIL import Image
import pygame


class Tile(GameObject):
    def __init__(self, x : int, y : int, object_list : list[GameObject], width : int, height : int, outline = False, position = False, debug = False):
        blank_surface = pygame.Surface((width, height))
        blank_surface.fill((255, 255, 255))
        GameObject.__init__(self, x, y, blank_surface, 1, width, height, 1, outline, position, debug = debug)
        # Load image with Pillow
        self.image_slot = GameObject(
            x = x + 20,
            y = y + 20,
            image = blank_surface,
            scale = 1,
            width = width - 40,
            height = height - 40,
            layer = 2,
            debug = True,
            keep_aspect_ratio=True
        )
        object_list.append(self.image_slot)

    def change_slot_image(self, inventory_image):
        box = inventory_image.image.getbbox()
        cropped = inventory_image.image.crop(box)
        pygame_image = pygame.image.fromstring(cropped.tobytes(), cropped.size, cropped.mode)
        GameObject.change_image(self.image_slot, pygame_image, 1,
                                width = self.image_slot.rect.width,
                                height = self.image_slot.rect.height,
                                keep_aspect_ratio=True)
