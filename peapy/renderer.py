from .colors import Color, Black
from . import exceptions
import peapy
from .__pygame import pygame
from .textures import Circle, Rectangle, Image


class Renderer(peapy.Component):
    """
    PeaPy renderer component
    """

    def __init__(self, texture: Rectangle | Image | Circle, color: Color = Black()):
        """
        Construct a new Renderer object

        Args:
            texture (Rectangle | Image | Circle): The texture to render
            color (Color): The color of the texture
        """
        super().__init__()

        self.texture = texture
        self.color = color

    def init(self, game: peapy.PeaPy, obj_name: str) -> peapy.PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Init component

        return self.peapy

    def update(self, game, obj_name: str) -> peapy.PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Update component
        if type(self.texture) == Rectangle:
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

        elif type(self.texture) == Circle:
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

        elif type(self.texture) == Image:
            self.texture.render(self.peapy, self.obj_name)

        return self.peapy
