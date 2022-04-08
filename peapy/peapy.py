from . import config
from . import exceptions
from .object import Object
from .__pygame import pygame


class PeaPy:
    def __init__(self, config: config.Config = config.get_default_config()):
        self.config = config

        self.__objects: dict[str, Object] = {}

        # Values
        self.frame_count = 0
        self.fps = 0
        self.delta_time = 0

        # Init pygame
        pygame.init()
        self.screen = pygame.display.set_mode((
            self.config.window.width,
            self.config.window.height
        ))
        pygame.display.set_caption(self.config.window.caption)
        self.clock = pygame.time.Clock()

        self.should_delete: list[str] = []

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

        self.should_delete.append(name)

    def update(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        self.screen.fill(self.config.window.background)

        self.delta_time = self.clock.tick(self.config.stats.max_fps) / 1000
        self.fps = self.clock.get_fps()
        self.frame_count += 1
        self.should_delete = []

        for obj in self.__objects.values():
            self = obj._update(self)

        # Remove objects marked for deletion
        for name in self.should_delete:
            del self.__objects[name]

        pygame.display.flip()
        return True

    def tree(self):
        for obj in self.__objects.values():
            print(obj.name)
            obj.tree()

    def __getitem__(self, name: str):
        return self.get_object(name)

    def __repr__(self):
        return "peapy.PeaPy()"
