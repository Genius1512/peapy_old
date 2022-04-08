from .component import Component
from . import exceptions


class Object:
    def __init__(self, name: str):
        self.name = name

        self.__components: dict[str, Component] = {}
        self.should_delete: list[str] = []

    def _init(self, game):
        self.peapy = game

        try:
            self.peapy = self.init(self.peapy)
        except AttributeError:
            pass

    def add_component(self, component: Component):
        if component.__class__.__name__ in self.__components:
            raise exceptions.DuplicateComponentException(component.__class__.__name__)

        self.__components[component.__class__.__name__] = component
        self.__components[component.__class__.__name__]._init(self, self.name)

    def get_component(self, name: str) -> Component:
        if name not in self.__components:
            raise exceptions.ComponentNotFoundException(name)

        return self.__components[name]

    def get_components(self) -> dict[str, Component]:
        return self.__components

    def remove_component(self, name: str):
        if name not in self.__components:
            raise exceptions.ComponentNotFoundException(name)

        self.should_delete.append(name)

    def _update(self, game):
        self.peapy = game
        self.should_delete = []

        # Update object
        for component in self.__components.values():
            self.peapy = component._update(self.peapy, self.name)

        try:
            self.peapy = self.update(self.peapy)
        except AttributeError:
            pass

        # Remove components marked for deletion
        for name in self.should_delete:
            del self.__components[name]

        return self.peapy

    def tree(self):
        for component in self.__components.values():
            print("\t" + component.__class__.__name__)

    def __getitem__(self, name: str):
        return self.get_component(name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"
