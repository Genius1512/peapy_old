from .config import Config, get_default_config
from . import exceptions
from .logger import Logger
from .objects import Object
from .__pygame import pygame


class PeaPy:
    """
    Main PeaPy class
    """

    def __init__(self, config: Config = get_default_config()):
        """
        Construct a PeaPy object

        Args:
            config (dict): The config
        """
        self.config = config
        self.logger = Logger(self.config.logger.name, self.config.logger.default_path)

        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.config.window.width, self.config.window.height)
        )
        pygame.display.set_caption(self.config.window.caption)
        self.clock = pygame.time.Clock()

        self.__objects: dict[str, Object] = {}

    def add_object(self, obj: Object):
        """
        Add an object to the game

        Args:
            obj (Object): The object to add
        """
        if obj.name in self.__objects:
            raise exceptions.DuplicateObjectException(obj.name)

        self.__objects[obj.name] = obj
        self.__objects[obj.name]._init(self)

    def get_object(self, name: str) -> Object:
        """
        Get an object by name

        Args:
            name (str): The name of the object

        Returns:
            Object: The object
        """
        if name not in self.__objects:
            raise exceptions.ObjectNotFoundException(name)

        return self.__objects[name]

    def get_objects(self) -> dict[str, Object]:
        """
        Get all objects

        Returns:
            dict[str, Object]: The objects
        """
        return self.__objects

    def remove_object(self, name: str):
        """
        Remove an object from the game

        Args:
            name (str): The name of the object
        """
        if name not in self.__objects:
            raise exceptions.ObjectNotFoundException(name)

        self = self.__objects[name].quit(self, name)
        del self.__objects[name]

    def update(self) -> bool:
        """
        Update the game

        Returns:
            bool: True if the game should continue, False if it should quit
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        self.delta = self.clock.tick(self.config.stats.max_fps) / 1000
        self.screen.fill(self.config.window.background)

        for obj in self.__objects.values():
            self = obj.update(self)

        pygame.display.update()
        return True

    def __getitem__(self, key: str) -> Object:
        return self.get_object(key)

    def __repr__(self):
        return "peapy.PeaPy()"


def print_peapy_tree(game: PeaPy):
    """
    Print the tree of objects and their components
    """
    print("PeaPy:")
    for obj in game.get_objects().values():
        print("\t" + obj.name + ":")
        for comp in obj.get_components().values():
            print("\t\t" + comp.NAME)
