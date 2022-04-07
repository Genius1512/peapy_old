from .__pygame import pygame


class Sound:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.volume = 1.0

        pygame.mixer.init()
        pygame.mixer.music.load(file_path)

    def play(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()
