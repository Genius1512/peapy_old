import peapy
from . import exceptions
from shapely.geometry import Polygon


class RectCollider(peapy.Component):
    """
    PeaPy RectCollider component
    """

    def __init__(self, x_offset=0, y_offset=0, width=None, height=None):
        """
        Construct a new RectCollider component

        Args:
            x_offset (int): The x offset to the transform of the parent object
            y_offset (int): The y offset to the transform of the parent object
            width (int): The width of the collider. When None, the width of the parent object's Transform is used
            height (int): The height of the collider. When None, the height of the parent object's Transform is used
        """
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
            raise exceptions.RequiredComponentNotPresent(
                "Target needs to have a collider"
            )

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
