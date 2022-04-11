from .object import Object
from .peapy import PeaPy
from .transform import Transform
from . import colors
from .renderer import Renderer
from . import textures


class Rectangle(Object):
    def __init__(self, name: str, x: int, y: int, width: int, height: int, color: colors.Color = colors.Black()):
        super().__init__(name)
        self.peapy = None

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    # Called when the object is created
    def init(self, game: PeaPy) -> PeaPy:
        self.peapy = game

        # Init object
        self.add_component(Transform(
            self.x,
            self.y,
            self.width,
            self.height
        ))
        self.add_component(Renderer(
            textures.Rectangle(),
            self.color
        ))

        return self.peapy

    # Called every frame
    def update(self, game: PeaPy) -> PeaPy:
        self.peapy = game  # The parent PeaPy object

        # Update object

        return self.peapy
