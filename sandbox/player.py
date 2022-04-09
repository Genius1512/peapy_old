import peapy


class Player(peapy.Object):
    def __init__(self, name: str):
        super().__init__(name)

        self.add_component(peapy.Transform(100, 100, 50, 50))
        self.add_component(
            peapy.Renderer(peapy.textures.Rectangle(), peapy.colors.Black())
        )

    def init(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game

        # Init object

        return self.peapy

    def update(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game

        # Update object

        return self.peapy
