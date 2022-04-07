from . import exceptions
from .__pygame import pygame
from .config import Config, get_default_config
from .logger import Logger
from .object import Object


class PeaPy:
    """
    Main PeaPy class
    """

    fps: int
    delta: float
    screen: pygame.Surface

    def __init__(self, config: Config = get_default_config()):
        """
        Construct a PeaPy object

        Args:
            config (dict): The config
        """

    def add_object(self, obj: Object):
        """
        Add an object to the game

        Args:
            obj (Object): The object to add
        """

    def get_object(self, name: str) -> Object:
        """
        Get an object by name

        Args:
            name (str): The name of the object

        Returns:
            Object: The object
        """

    def get_objects(self) -> dict[str, Object]:
        """
        Get all objects

        Returns:
            dict[str, Object]: The objects
        """

    def remove_object(self, name: str):
        """
        Remove an object from the game

        Args:
            name (str): The name of the object
        """

    def update(self) -> bool:
        """
        Update the game

        Returns:
            bool: True if the game should continue, False if it should quit
        """

    def __getitem__(self, key: str) -> Object:
        return self.get_object(key)

    def __repr__(self):
        return "peapy.PeaPy()"


def print_peapy_tree(game: PeaPy):
    """
    Print the tree of objects and their components

    Args:
        game (PeaPy): The game
    """
