from . import exceptions
from .__pygame import pygame

FROM_TRANSFORM = -2
FROM_IMAGE = -1


class Texture:
    """
    PeaPy class to represent a texture
    """

    pass


class Circle:
    """
    PeaPy class to represent a circle
    """

    pass


class Rectangle(Texture):
    """
    PeaPy class to represent a rectangle
    """

    pass


class Image(Texture):
    """
    PeaPy class to represent an image
    """

    def __init__(self, path: str, width: int = -1, height: int = -1):
        """
        Construct a new Image object

        Args:
            path (str): The path to the image file
            width (int): The width of the image. When set to -2, the width of the parent object's Transform will be set
                            to the width of the image. When set to -1, the width of the image will be used.
            height (int): The height of the image. When set to -2, the height of the parent object's Transform will be
                            set to the height of the image. When set to -1, the height of the image will be used.
        """
        self.path = path
        self.width = width
        self.height = height

        self.image = pygame.image.load(self.path)

    def render(self, game, obj_name: str):
        """
        Render the image
        """
        if self.width == FROM_TRANSFORM:
            try:
                width = game.get_object(obj_name)["Transform"].width
            except exceptions.ComponentNotFoundException:
                raise exceptions.RequiredComponentNotPresent(
                    "Image requires Transform component"
                )
        elif self.width == FROM_IMAGE:
            width = self.image.get_width()
        else:
            width = self.width

        if self.height == FROM_TRANSFORM:
            try:
                height = game.get_object(obj_name)["Transform"].height
            except exceptions.ComponentNotFoundException:
                raise exceptions.RequiredComponentNotPresent(
                    "Image requires Transform component"
                )
        elif self.height == FROM_IMAGE:
            height = self.image.get_height()
        else:
            height = self.height

        image = pygame.transform.scale(self.image, (width, height))
        image = pygame.transform.rotate(image, game.get_object(obj_name)["Transform"].rotation)
        try:
            game.screen.blit(
                image, (game[obj_name]["Transform"].x, game[obj_name]["Transform"].y)
            )
        except exceptions.ComponentNotFoundException:
            raise exceptions.RequiredComponentNotPresent(
                "Image requires Transform component"
            )
