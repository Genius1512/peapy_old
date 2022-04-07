from . import exceptions
from .objects import Object
from .__pygame import pygame


class PeaPy:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("PeaPy")
        self.clock = pygame.time.Clock()

        self.__objects: dict[str, Object] = {}

    def add_object(self, obj: Object):
        if obj.name in self.__objects:
            raise exceptions.DuplicateObjectException(obj.name)

        self.__objects[obj.name] = obj
        self.__objects[obj.name]._init(self)

    def get_object(self, name: str) -> Object:
        if name not in self.__objects:
            raise exceptions.ObjectNotFoundException(name)

        return self.__objects[name]

    def get_objects(self) -> dict[str, Object]:
        return self.__objects

    def remove_object(self, name: str):
        if name not in self.__objects:
            raise exceptions.ObjectNotFoundException(name)

        self = self.__objects[name].quit(self, name)
        del self.__objects[name]

    def update(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        self.delta = self.clock.tick(60) / 1000
        self.screen.fill((255, 255, 255))

        for obj in self.__objects.values():
            self = obj.update(self)

        pygame.display.update()
        return True

    def __repr__(self):
        return "peapy.PeaPy()"


def print_peapy_tree(game: PeaPy):
    print("PeaPy:")
    for obj in game.get_objects().values():
        print("\t" + obj.name + ":")
        for comp in obj.get_components().values():
            print("\t\t" + comp.NAME)
