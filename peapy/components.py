from .interfaces import PeaPy


class Component:
    """
    Component class
    """
    NAME = "Component"

    def __init__(self):
        """
        Construct a component
        """

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
        return f"peapy.components.{self.__class__.__name__}()"
