from .components import Component
from . import exceptions
from .interfaces import PeaPy


class Object:
    def __init__(self, name: str):
        self.name = name

        self.__components: dict[str, Component] = {}

    def _init(self, game: PeaPy):
        self.peapy = game

    def add_component(self, component: Component):
        if component.NAME in self.__components:
            raise exceptions.DuplicateComponentException(component.NAME)

        self.__components[component.NAME] = component
        self.__components[component.NAME]._init(self.peapy, self.name)

    def get_component(self, name: str) -> Component:
        if name not in self.__components:
            raise exceptions.ComponentNotFoundException(name)

        return self.__components[name]

    def get_components(self) -> dict[str, Component]:
        return self.__components

    def remove_component(self, name: str):
        if name not in self.__components:
            raise exceptions.ComponentNotFoundException(name)

        self.peapy = self.__components[name].quit(self.peapy, self.name)
        del self.__components[name]

    def update(self, game: PeaPy) -> PeaPy:
        self.peapy = game

        for component in self.__components.values():
            self.peapy = component.update(self.peapy, self.name)

        return self.peapy

    def quit(self, game: PeaPy) -> PeaPy:
        self.peapy = game

        # Quit object

        return self.peapy

    def __repr__(self):
        return f"peapy.objects.{self.__class__.__name__}({self.name})"
