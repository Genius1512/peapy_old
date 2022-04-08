import peapy



class Transform(peapy.Component):
    def __init__(self, x: int, y: int, width: int, height: int, rotation: int = 0):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation

    @property
    def rect(self) -> tuple[int]:
        return self.x, self.y, self.width, self.height

    @property
    def top_left(self) -> tuple[int]:
        return self.x, self.y

    @property
    def top_right(self) -> tuple[int]:
        return self.x + self.width, self.y

    @property
    def bottom_left(self) -> tuple[int]:
        return self.x, self.y + self.height

    @property
    def bottom_right(self) -> tuple[int]:
        return self.x + self.width, self.y + self.height

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
