from .component import Component
from .interfaces import PeaPy
from .__pygame import pygame


class Transform(Component):
    """
    Transform class
    """

    NAME = "Transform"

    def __init__(
        self, x: float, y: float, width: float, height: float, rotation: float = 0.0
    ):
        """
        Construct a transform component

        Args:
            x (float): X position
            y (float): Y position
            width (float): Width
            height (float): Height
            rotation (float): Rotation
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation

    @property
    def top_left(self) -> tuple:
        """
        Get the top left position of the transform
        """
        return self.x, self.y

    @property
    def top_right(self) -> tuple:
        """
        Get the top right position of the transform
        """
        return self.x + self.width, self.y

    @property
    def bottom_left(self) -> tuple:
        """
        Get the bottom left position of the transform
        """
        return self.x, self.y + self.height

    @property
    def bottom_right(self) -> tuple:
        """
        Get the bottom right position of the transform
        """
        return self.x + self.width, self.y + self.height

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

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

        # Update component

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
        return f"peapy.components.{self.__class__.__name__}(x={self.x}, y={self.y}, width={self.width}, height={self.height}, rotation={self.rotation})"
