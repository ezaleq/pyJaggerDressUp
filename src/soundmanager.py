import pygame

class SoundManager:
    CLICK = "click"
    DONE = "done"
    GRAB = "grab"
    MUSIC = "bgmusic"
    RESET = "reset"
    def __init__(self):
        path = "resources/sfx/{sound}"
        self.muted = False
        self.sounds = {
            "click" : pygame.mixer.Sound(path.format(sound="click.wav")),
            "done" : pygame.mixer.Sound(path.format(sound="done.wav")),
            "grab" : pygame.mixer.Sound(path.format(sound="grab.wav")),
            "bgmusic" : pygame.mixer.Sound(path.format(sound="bgmusic.wav")),
            "reset" : pygame.mixer.Sound(path.format(sound="reset.wav")),
        }
        self.sounds[SoundManager.MUSIC].play(-1)

    def play(self, sound : str):
        if self.muted or (sound not in self.sounds):
            return
        self.sounds[sound].play()

    def toggle(self):
        self.muted = not self.muted
        if self.muted:
            for sound in self.sounds.values():
                sound.stop()
            return

        self.sounds[SoundManager.MUSIC].play(-1)
