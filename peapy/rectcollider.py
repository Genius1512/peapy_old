import peapy
from . import exceptions
from shapely.geometry import Polygon


class RectCollider(peapy.Component):

    def __init__(self, x_offset=0, y_offset=0, width=None, height=None):
        super().__init__()

        self.x_offset = x_offset
        self.y_offset = y_offset
        self.width = width
        self.height = height

    def init(self, game: peapy.PeaPy, obj_name: str) -> peapy.PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Init object

        return self.peapy

    def is_colliding(self, target: str) -> bool:
        """
        Check if this RectCollider is colliding with another RectCollider
        """
        if "RectCollider" not in self.peapy[target].get_components():
            raise exceptions.RequiredComponentNotFoundException("RectCollider")

        p1 = Polygon(
            [
                self.peapy[self.obj_name]["Transform"].top_left,
                self.peapy[self.obj_name]["Transform"].top_right,
                self.peapy[self.obj_name]["Transform"].bottom_right,
                self.peapy[self.obj_name]["Transform"].bottom_left,
            ]
        )

        p2 = Polygon(
            [
                self.peapy[target]["Transform"].top_left,
                self.peapy[target]["Transform"].top_right,
                self.peapy[target]["Transform"].bottom_right,
                self.peapy[target]["Transform"].bottom_left,
            ]
        )

        return p1.intersects(p2)

    def __repr__(self):
        return f"peapy.components.{self.__class__.__name__}()"