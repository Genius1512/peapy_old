from .interfaces import PeaPy


class Component:
    NAME = "Component"

    def __init__(self):
        pass

    def _init(self, game: PeaPy, obj_name: str):
        self.peapy = game
        self.obj_name = obj_name

    def update(self, game: PeaPy, obj_name: str) -> PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Update component

        return self.peapy

    def quit(self, game: PeaPy, obj_name: str) -> PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Quit component

        return self.peapy

    def __repr__(self):
        return f"peapy.components.{self.__class__.__name__}()"
