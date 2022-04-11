from .component import Component
from . import exceptions
from . import textures
from .peapy import PeaPy
from shapely.geometry import Polygon


class Collider(Component):
    """
    PeaPy Collider component
    """

    def __init__(
            self,
            shape: textures.Rectangle | textures.Circle,
            x_offset=0,
            y_offset=0,
            width: int = -1,
            height: int = -1,
    ):
        """
        Construct a new Collider component

        Args:
            x_offset (int): The x offset to the transform of the parent object
            y_offset (int): The y offset to the transform of the parent object
            width (int): The width of the collider. When -1, the width of the parent object's Transform is used
            height (int): The height of the collider. When -1, the height of the parent object's Transform is used
        """
        super().__init__()

        self.object_name = None
        self.shape = shape
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.width = width
        self.height = height

    def init(self, game: PeaPy, object_name: str) -> PeaPy:
        self.peapy = game
        self.object_name = object_name

        # Init object

        return self.peapy

    # Called every frame
    def update(self, game: PeaPy, object_name: str) -> PeaPy:
        self.peapy = game
        self.object_name = object_name

        # Update component

        return self.peapy

    def is_colliding(self, target: str) -> bool:
        if (
                not "Transform" in self.peapy[target].get_components()
                or not "Transform" in self.peapy[self.object_name].get_components()
        ):
            raise exceptions.RequiredComponentNotPresent("Transform is required")

        if self.width == -1:
            width = self.peapy[self.object_name]["Transform"].width
        else:
            width = self.width
        if self.height == -1:
            height = self.peapy[self.object_name]["Transform"].height
        else:
            height = self.height

        if self.peapy[target]["Collider"].width == -1:
            target_width = self.peapy[target]["Transform"].width
        else:
            target_width = self.peapy[target]["Collider"].width
        if self.peapy[target]["Collider"].height == -1:
            target_height = self.peapy[target]["Transform"].height
        else:
            target_height = self.peapy[target]["Collider"].height
        match self.shape:
            case textures.Rectangle():
                match self.peapy[target]["Collider"].shape:
                    case textures.Rectangle():

                        p1 = Polygon(
                            [
                                (
                                    self.peapy[self.object_name]["Transform"].x
                                    + self.x_offset,
                                    self.peapy[self.object_name]["Transform"].y
                                    + self.y_offset,
                                ),
                                (
                                    self.peapy[self.object_name]["Transform"].x
                                    + self.x_offset
                                    + width,
                                    self.peapy[self.object_name]["Transform"].y
                                    + self.y_offset,
                                ),
                                (
                                    self.peapy[self.object_name]["Transform"].x
                                    + self.x_offset
                                    + width,
                                    self.peapy[self.object_name]["Transform"].y
                                    + self.y_offset
                                    + height,
                                ),
                                (
                                    self.peapy[self.object_name]["Transform"].x
                                    + self.x_offset,
                                    self.peapy[self.object_name]["Transform"].y
                                    + self.y_offset
                                    + height,
                                ),
                            ]
                        )

                        p2 = Polygon(
                            [
                                (
                                    self.peapy[target]["Transform"].x
                                    + self.peapy[target]["Collider"].x_offset,
                                    self.peapy[target]["Transform"].y
                                    + self.peapy[target]["Collider"].y_offset,
                                ),
                                (
                                    self.peapy[target]["Transform"].x
                                    + self.peapy[target]["Collider"].x_offset
                                    + target_width,
                                    self.peapy[target]["Transform"].y
                                    + self.peapy[target]["Collider"].y_offset,
                                ),
                                (
                                    self.peapy[target]["Transform"].x
                                    + self.peapy[target]["Collider"].x_offset
                                    + target_width,
                                    self.peapy[target]["Transform"].y
                                    + self.peapy[target]["Collider"].y_offset
                                    + target_height,
                                ),
                                (
                                    self.peapy[target]["Transform"].x
                                    + self.peapy[target]["Collider"].x_offset,
                                    self.peapy[target]["Transform"].y
                                    + self.peapy[target]["Collider"].y_offset
                                    + target_height,
                                ),
                            ]
                        )

                        return p1.intersects(p2)

                    case textures.Circle():
                        radius = target_height
                        x = (
                                self.peapy[target]["Transform"].x
                                + self.peapy[target]["Collider"].x_offset
                        )
                        y = (
                                self.peapy[target]["Transform"].y
                                + self.peapy[target]["Collider"].y_offset
                        )

                        x1 = self.peapy[self.object_name]["Transform"].x + self.x_offset
                        y1 = self.peapy[self.object_name]["Transform"].y + self.y_offset
                        x2 = (
                                self.peapy[self.object_name]["Transform"].x
                                + self.x_offset
                                + width
                        )
                        y2 = (
                                self.peapy[self.object_name]["Transform"].y
                                + self.y_offset
                                + height
                        )

                        x_nearest = max(x1, min(x, x2))
                        y_nearest = max(y1, min(y, y2))

                        x_distance = x_nearest - x
                        y_distance = y_nearest - y
                        return (x_distance ** 2 + y_distance ** 2) <= radius ** 2

                    case _:
                        raise TypeError(
                            "Collider shape must be either Rectangle or Circle"
                        )

            case textures.Circle():
                match self.peapy[target]["Collider"].shape:
                    case textures.Rectangle():
                        radius = height
                        x = self.peapy[self.object_name]["Transform"].x + self.x_offset
                        y = self.peapy[self.object_name]["Transform"].y + self.y_offset

                        x1 = (
                                self.peapy[target]["Transform"].x
                                + self.peapy[target]["Collider"].x_offset
                        )
                        y1 = (
                                self.peapy[target]["Transform"].y
                                + self.peapy[target]["Collider"].y_offset
                        )
                        x2 = (
                                self.peapy[target]["Transform"].x
                                + self.peapy[target]["Collider"].x_offset
                                + target_width
                        )
                        y2 = (
                                self.peapy[target]["Transform"].y
                                + self.peapy[target]["Collider"].y_offset
                                + target_height
                        )

                        x_nearest = max(x1, min(x, x2))
                        y_nearest = max(y1, min(y, y2))

                        x_distance = x_nearest - x
                        y_distance = y_nearest - y
                        return (x_distance ** 2 + y_distance ** 2) <= radius ** 2

                    case textures.Circle():
                        d_x = abs(
                            self.peapy[self.object_name]["Transform"].x
                            + self.x_offset
                            - self.peapy[target]["Transform"].x
                            - self.peapy[target]["Collider"].x_offset
                        )
                        d_y = abs(
                            self.peapy[self.object_name]["Transform"].y
                            + self.y_offset
                            - self.peapy[target]["Transform"].y
                            - self.peapy[target]["Collider"].y_offset
                        )
                        d = (d_x ** 2 + d_y ** 2) ** 0.5

                        return d < target_height + target_height

                    case _:
                        raise TypeError(
                            "Collider shape must be either Rectangle or Circle"
                        )

            case _:
                raise TypeError("Collider shape must be either Rectangle or Circle")
