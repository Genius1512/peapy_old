from .interfaces import PeaPy


class Object:
    def __init__(self, name: str):
        self.name = name

    def _init(self, game: PeaPy):
        self.peapy = game

    def update(self, game: PeaPy) -> PeaPy:
        self.peapy = game

        # Update object

        return self.peapy

    def quit(self, game: PeaPy) -> PeaPy:
        self.peapy = game

        # Quit object

        return self.peapy

    def __repr__(self):
        return f"peapy.objects.{self.__class__.__name__}({self.name})"
