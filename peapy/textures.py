from .interfaces import PeaPy
from .__pygame import pygame


class Texture:
    """
    Class for loading and rendering images
    """

    pass


class Rectangle(Texture):
    """
    Class to represent a rectangle Texture

    For rendering, the object's height of the Transform will be used as the radius
    """


class Circle(Texture):
    """
    Class to represent a circle Texture
    """


class Image(Texture):
    def __init__(self, path: str, width: int = "no", height: int = "no"):
        """
        Image class

        Args:
            path (str): Path to the image
            width (int): Width of the image. When set to "no", the width of the image will be used. When set to "default", the width of the object's Transform will be used.
                        Else, the width will be set to the given value.
            height (int): Height of the image. When set to "no", the height of the image will be used. When set to "default", the height of the object's Transform will be used.
                        Else, the height will be set to the given value.
        """
        self.path = path
        self.width = width
        self.height = height

        self.image = pygame.image.load(self.path)

    def render(self, game: PeaPy, obj_name: str):
        """
        Render the image to the screen

        Args:
            game (PeaPy): The game object
            obj_name (str): The name of the object
        """
        if self.width is "default":
            width = game[obj_name]["Transform"].width
        elif self.width is "no":
            width = self.image.get_width()
        else:
            width = self.width

        if self.height is "default":
            height = game[obj_name]["Transform"].height
        elif self.height is "no":
            height = self.image.get_height()
        else:
            height = self.height

        image = pygame.transform.scale(self.image, (width, height))

        game.screen.blit(
            image, (game[obj_name]["Transform"].x, game[obj_name]["Transform"].y)
        )
