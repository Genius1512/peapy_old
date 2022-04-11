from .component import Component
from . import exceptions


class Object:
    """
    PeaPy object class
    """

    def __init__(self, name: str):
        """
        Construct a new Object

        Args:
            name (str): The name of the object
        """
        self.name = name
        self.peapy = None

        self.__components: dict[str, Component] = {}
        self.should_delete: list[str] = []

    def init_(self, game):
        """
        Called when the object is added to a game.

        Args:
            game (Game): The game object
        """
        self.peapy = game

        try:
            self.peapy = self.init(self.peapy)
        except AttributeError:
            pass

    def init(self, game):
        pass

    def add_component(self, component: Component):
        """
        Add a component to the object.

        Args:
            component (Component): The component to add
        """
        if component.__class__.__name__ in self.__components:
            raise exceptions.DuplicateComponentException(component.__class__.__name__)

        self.__components[component.__class__.__name__] = component
        self.__components[component.__class__.__name__].init_(self.peapy, self.name)

    def get_component(self, name: str) -> Component:
        """
        Get a component by name.

        Args:
            name (str): The name of the component
        """
        if name not in self.__components:
            raise exceptions.ComponentNotFoundException(name)

        return self.__components[name]

    def get_components(self) -> dict[str, Component]:
        """
        Get all components.

        Returns:
            dict[str, Component]: The components
        """
        return self.__components

    def remove_component(self, name: str):
        """
        Remove a component by name.

        Args:
            name (str): The name of the component
        """
        if name not in self.__components:
            raise exceptions.ComponentNotFoundException(name)

        self.should_delete.append(name)

    def update_(self, game):
        """
        Called when the object is updated.

        Args:
            game (Game): The game object
        """
        self.peapy = game
        self.should_delete = []

        # Update object
        for component in self.__components.values():
            self.peapy = component.update_(self.peapy, self.name)

        try:
            self.peapy = self.update(self.peapy)
        except AttributeError:
            pass

        # Remove components marked for deletion
        for name in self.should_delete:
            del self.__components[name]

        return self.peapy

    def update(self, game):
        pass

    def tree(self):
        """
        Print the object tree.
        """
        for component in self.__components.values():
            print("\t" + component.__class__.__name__)

    def __getitem__(self, name: str):
        return self.get_component(name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"
