from pygame import Surface
import scenes.scene as scene
from scenes.title import TitleScene

class SceneManager:
    _actualScene : scene.Scene
    _screen : Surface

    def __init__(self, screen : Surface):
        self._screen = screen
        self.load_scene(TitleScene(self))

    def load_scene(self, scene):
        self._actualScene = scene

    def update(self):
        self._actualScene.update()