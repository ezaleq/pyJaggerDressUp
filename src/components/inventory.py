import json
import pygame
from PIL import Image
from components.button import Button
from components.gameobject import GameObject
from components.tile import Tile

class inventory_image:
    image : Image
    category : int
    type : int
    def __init__(self, image : Image, category : int, type : int):
        self.image = image
        self.category = category
        self.type = type
class Inventory(GameObject):

    tiles : Tile = []
    images : list[inventory_image] = []
    actual_cloths : list[inventory_image] = []
    def __init__(self, x : int, y : int, width : int, height : int, object_list : list[GameObject]):
        tile_blur_bg = pygame.image.load("resources/interface/dress/cuadro.png").convert_alpha()
        super().__init__(x, y, tile_blur_bg, 1, width, height, layer=0)

        self.load_tiles(x, y, object_list)
        self.load_button_pages(x, y, object_list)
        self.load_type_buttons(x, y, object_list)
        self.load_images()
        self.change_type(0)

    def change_type(self, type : int):
        self.actual_cloths = list(filter(lambda x: x.type == type, self.images))
        for index, tile in enumerate(self.tiles):
            tile.change_slot_image(self.actual_cloths[index])
    def load_button_pages(self, x : int, y : int, object_list : list[GameObject]):
        left_image = pygame.image.load("resources/interface/dress/flecha-1.png").convert_alpha()
        left_page = Button(
            x = x - 40,
            y = y + GameObject.get_hcenter(self.image.get_size(), left_image.get_height(), 0.3),
            image = left_image,
            scale = 0.3,
        )

        object_list.append(left_page)
    def load_images(self):
        with open("config/cloth_config.json", "r") as file:
            config = json.load(file)
        for image in config["images"]:
            img = Image.open(f"resources/cloth/{image['name']}")
            category = image["category"]
            type = image["type"]
            self.images.append(inventory_image(img, category, type))
    def load_type_buttons(self, x : int, y : int, object_list : list[GameObject]):
        head_image = pygame.image.load("resources/interface/dress/face.png").convert_alpha()
        top_image = pygame.image.load("resources/interface/dress/tops.png").convert_alpha()
        bottom_image = pygame.image.load("resources/interface/dress/bottoms.png").convert_alpha()
        shoe_image = pygame.image.load("resources/interface/dress/shoes.png").convert_alpha()
        accesory_image = pygame.image.load("resources/interface/dress/accesories.png").convert_alpha()
        image_list = [head_image, top_image, bottom_image, shoe_image, accesory_image]
        xbutton = x + 40
        ybutton = y - 50
        for image in image_list:
            btn = Button(
               x = xbutton,
               y = ybutton,
               image = image,
               scale = 0.3
            )
            object_list.append(btn)
            xbutton += 60
    def load_tiles(self, x : int, y : int, object_list : list[GameObject]):
        wtile = self.rect.width * 0.232
        htile = self.rect.height * 0.43
        xtile = x + 20
        ytile = y + 40
        for i in range(4):
            tile = Tile(x = xtile,
                        y = ytile,
                        width = wtile,
                        height = htile,
                        outline = True,
                        object_list = object_list)
            object_list.append(tile)
            self.tiles.append(tile)
            xtile += tile.image.get_width() + 10
        xtile = x + 20
        ytile = ytile + tile.image.get_height() + 10
        for i in range(4) :
            tile = Tile(x = xtile,
                        y = ytile,
                        width = wtile,
                        height = htile,
                        outline = True,
                        object_list = object_list)
            object_list.append(tile)
            self.tiles.append(tile)
            xtile += tile.image.get_width() + 10
