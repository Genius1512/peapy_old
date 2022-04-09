from .__pygame import pygame


class Sound:
    """
    PeaPy sound component
    """

    def __init__(self, file_path: str):
        """
        Construct a new Sound object

        Args:
            file_path (str): The path to the sound file
        """
        self.file_path = file_path
        self.volume = 1.0

        self.is_playing = False

        pygame.mixer.init()
        pygame.mixer.music.load(file_path)

    def play(self):
        """
        Play the sound
        """
        self.is_playing = True
        pygame.mixer.music.play()

    def stop(self):
        """
        Stop the sound
        """
        self.is_playing = False
        pygame.mixer.music.stop()

    def pause(self):
        """
        Pause the sound
        """
        self.is_playing = False
        pygame.mixer.music.pause()

    def unpause(self):
        """
        Unpause the sound
        """
        self.is_playing = True
        pygame.mixer.music.unpause()

    def set_volume(self, volume: float):
        """
        Set the volume of the sound
        """
        self.volume = volume
        pygame.mixer.music.set_volume(volume)
