from .component import Component
from . import exceptions
from .interfaces import PeaPy
from shapely.geometry import Polygon


class RectCollider(Component):
    """
    RectCollider class
    """

    NAME = "RectCollider"

    def __init__(self, x_offset=0, y_offset=0, width=None, height=None):
        """
        Construct a RectCollider
        """
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.width = width
        self.height = height

    def _init(self, game: PeaPy, obj_name: str):
        """
        Called when creating a component
        Don't override this
        """
        self.peapy = game
        self.obj_name = obj_name

    def is_colliding(self, target: str) -> bool:
        """
        Check if this RectCollider is colliding with another RectCollider
        """
        if "RectCollider" not in self.peapy[target].get_components():
            raise exceptions.ComponentMissingException("RectCollider")

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
