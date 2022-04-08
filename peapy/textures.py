from .__pygame import pygame
from . import exceptions


FROM_TRANSFORM = -2
FROM_IMAGE = -1


class Circle:
    pass


class Texture:
    pass


class Rectangle(Texture):
    pass


class Image(Texture):
    def __init__(self, path: str, width: int = -1, height: int = -1):
        self.path = path
        self.width = width
        self.height = height

        self.image = pygame.image.load(self.path)

    def render(self, game, obj_name: str):
        if self.width == FROM_TRANSFORM:
            try:
                width = game.get_object(obj_name)["Transform"].width
            except exceptions.ComponentNotFoundException:
                raise exceptions.RequiredComponentNotFoundException(
                    "Transform",
                    obj_name
                )
        elif self.width == FROM_IMAGE:
            width = self.image.get_width()
        else:
            width = self.width

        if self.height == FROM_TRANSFORM:
            try:
                height = game.get_object(obj_name)["Transform"].height
            except exceptions.ComponentNotFoundException:
                raise exceptions.RequiredComponentNotFoundException(
                    "Transform",
                    obj_name
                )
        elif self.height == FROM_IMAGE:
            height = self.image.get_height()
        else:
            height = self.height

        image = pygame.transform.scale(self.image, (width, height))
        game.screen.blit(
            image,
            (game[obj_name]["Transform"].x,
            game[obj_name]["Transform"].y)
        )
