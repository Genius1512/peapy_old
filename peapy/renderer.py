from .colors import Color, Black
from .component import Component
from .interfaces import PeaPy
from .__pygame import pygame
from .textures import Circle, Rectangle, Texture, Image


class Renderer(Component):
    """
    Renderer class
    """

    NAME = "Component"

    def __init__(self, texture: Texture, color: Color = Black()):
        """
        Construct a renderer component
        """
        self.texture = texture
        self.color = color

    def _init(self, game: PeaPy, obj_name: str):
        """
        Called when creating a component
        Don't override this
        """
        self.peapy = game
        self.obj_name = obj_name

    def update(self, game: PeaPy, obj_name: str) -> PeaPy:
        """
        Called every frame
        """
        self.peapy = game
        self.obj_name = obj_name

        if type(self.texture) is Rectangle:
            pygame.draw.rect(
                self.peapy.screen,
                self.color.rgba,
                self.peapy[self.obj_name]["Transform"].rect,
            )

        elif type(self.texture) is Circle:
            pygame.draw.circle(
                self.peapy.screen,
                self.color.rgba,
                (
                    self.peapy[self.obj_name]["Transform"].x
                    + self.peapy[self.obj_name]["Transform"].height,
                    self.peapy[self.obj_name]["Transform"].y
                    + self.peapy[self.obj_name]["Transform"].height,
                ),
                self.peapy[self.obj_name]["Transform"].height,
            )

        elif type(self.texture) is Image:
            self.texture.render(self.peapy, self.obj_name)

        return self.peapy

    def quit(self, game: PeaPy, obj_name: str) -> PeaPy:
        """
        Called when deleting the component
        """
        self.peapy = game
        self.obj_name = obj_name

        # Quit component

        return self.peapy

    def __repr__(self):
        return f"peapy.components.{self.__class__.__name__}()"
