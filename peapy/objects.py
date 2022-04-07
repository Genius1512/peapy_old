from .components import Component
from . import exceptions
from .interfaces import PeaPy


class Object:
    """
    Object class
    """
    def __init__(self, name: str):
        """
        Construct an object

        Args:
            name (str): The name of the object
        """
        self.name = name

        self.__components: dict[str, Component] = {}

    def _init(self, game: PeaPy):
        """
        Called when creating an object
        Don't override this
        """
        self.peapy = game

    def add_component(self, component: Component):
        """
        Add a component to the object

        Args:
            component (Component): The component to add
        """
        if component.NAME in self.__components:
            raise exceptions.DuplicateComponentException(component.NAME)

        self.__components[component.NAME] = component
        self.__components[component.NAME]._init(self.peapy, self.name)

    def get_component(self, name: str) -> Component:
        """
        Get a component by name

        Args:
            name (str): The name of the component

        Returns:
            Component: The component
        """
        if name not in self.__components:
            raise exceptions.ComponentNotFoundException(name)

        return self.__components[name]

    def get_components(self) -> dict[str, Component]:
        """
        Get all components

        Returns:
            dict[str, Component]: The components
        """
        return self.__components

    def remove_component(self, name: str):
        """
        Remove a component by name

        Args:
            name (str): The name of the component
        """
        if name not in self.__components:
            raise exceptions.ComponentNotFoundException(name)

        self.peapy = self.__components[name].quit(self.peapy, self.name)
        del self.__components[name]

    def update(self, game: PeaPy) -> PeaPy:
        """
        Called every frame

        Args:
            game (PeaPy): The parent game object

        Returns:
            PeaPy: The updated game object
        """
        self.peapy = game

        for component in self.__components.values():
            self.peapy = component.update(self.peapy, self.name)

        return self.peapy

    def quit(self, game: PeaPy) -> PeaPy:
        """
        Called when the object is destroyed

        Args:
            game (PeaPy): The parent game object

        Returns:
            PeaPy: The updated game object
        """
        self.peapy = game

        # Quit object

        return self.peapy

    def __repr__(self):
        return f"peapy.objects.{self.__class__.__name__}({self.name})"
