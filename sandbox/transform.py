import peapy


class Transform(peapy.Component):
    def __init__(self):
        super().__init__()

    def init(self, game: peapy.PeaPy, obj_name: str) -> peapy.PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Init component

        return self.peapy

    def update(self, game: peapy.PeaPy, obj_name: str) -> peapy.PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Update component

        return self.peapy
