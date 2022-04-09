import peapy


class Transform(peapy.Component):
    """
    PeaPy transform component
    """

    def __init__(self, x: int, y: int, width: int, height: int, rotation: int = 0):
        """
        Construct a new Transform component

        Args:
            x (int): The x position of the transform
            y (int): The y position of the transform
            width (int): The width of the transform
            height (int): The height of the transform
            rotation (int): The rotation of the transform
        """
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation

    @property
    def rect(self) -> tuple[int]:
        """
        Get the rect of the transform
        """
        return self.x, self.y, self.width, self.height

    @property
    def top_left(self) -> tuple[int]:
        """
        Get the coords of the top left position of the transform
        """
        return self.x, self.y

    @property
    def top_right(self) -> tuple[int]:
        """
        Get the coords of the top right position of the transform
        """
        return self.x + self.width, self.y

    @property
    def bottom_left(self) -> tuple[int]:
        """
        Get the coords of the bottom left position of the transform
        """
        return self.x, self.y + self.height

    @property
    def bottom_right(self) -> tuple[int]:
        """
        Get the coords of the bottom right position of the transform
        """
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
