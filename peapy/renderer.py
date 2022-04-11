from . import textures
from . import colors
from . import exceptions
from .peapy import PeaPy
from .__pygame import pygame
from .component import Component


class Renderer(Component):
    """
    PeaPy renderer component
    """

    def __init__(self, texture: textures.Rectangle | textures.Image | textures.Circle,
                 color: colors.Color = colors.Black()):
        """
        Construct a new Renderer object

        Args:
            texture (Rectangle | Image | Circle): The texture to render
            color (Color): The color of the texture
        """
        super().__init__()

        self.peapy = None
        self.obj_name = None
        self.texture = texture
        self.color = color

    def init(self, game: PeaPy, obj_name: str) -> PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Init component

        return self.peapy

    def update(self, game, obj_name: str) -> PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Update component
        if type(self.texture) == textures.Rectangle:
            try:
                pygame.draw.rect(
                    self.peapy.screen,
                    self.color.rgba,
                    self.peapy[self.obj_name]["Transform"].rect,
                )
            except exceptions.ComponentNotFoundException:
                raise exceptions.RequiredComponentNotPresent(
                    "Renderer requires Transform component"
                )

        elif type(self.texture) == textures.Circle:
            try:
                pygame.draw.circle(
                    self.peapy.screen,
                    self.color.rgba,
                    self.peapy[self.obj_name]["Transform"].top_left,
                    self.peapy[self.obj_name]["Transform"].height,
                )
            except exceptions.ComponentNotFoundException:
                raise exceptions.RequiredComponentNotPresent(
                    "Renderer requires Transform component"
                )

        elif type(self.texture) == textures.Image:
            self.texture.render(self.peapy, self.obj_name)

        return self.peapy
