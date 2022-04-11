class Color:
    """
    PeaPy Color class
    """

    def __init__(self, r: int, g: int, b: int, a: int = 255):
        """
        Construct a new Color object

        Args:
            r (int): Red value
            g (int): Green value
            b (int): Blue value
            a (int): Alpha value
        """
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @property
    def rgb(self):
        """
        Get the RGB value of the color
        """
        return self.r, self.g, self.b

    @property
    def rgba(self):
        """
        Get the RGBA value of the color
        """
        return self.r, self.g, self.b, self.a

    @property
    def hex(self):
        """
        Get the hex value of the color
        """
        return "#{:02x}{:02x}{:02x}".format(self.r, self.g, self.b)

    def __repr__(self) -> str:
        return f"Color({self.r}, {self.g}, {self.b}, {self.a})"


class Transparent(Color):
    """
    Standard transparent color: (0, 0, 0, 0)
    """

    def __init__(self):
        super().__init__(0, 0, 0, 0)


class Black(Color):
    """
    Standard black color: (0, 0, 0, 255)
    """

    def __init__(self):
        super().__init__(0, 0, 0)


class White(Color):
    """
    Standard white color: (255, 255, 255, 255)
    """

    def __init__(self):
        super().__init__(255, 255, 255)


class Red(Color):
    """
    Standard red color: (255, 0, 0, 255)
    """

    def __init__(self):
        super().__init__(255, 0, 0)


class Green(Color):
    """
    Standard green color: (0, 255, 0, 255)
    """

    def __init__(self):
        super().__init__(0, 255, 0)


class Blue(Color):
    """
    Standard blue color: (0, 0, 255, 255)
    """

    def __init__(self):
        super().__init__(0, 0, 255)


class Yellow(Color):
    """
    Standard yellow color: (255, 255, 0, 255)
    """

    def __init__(self):
        super().__init__(255, 255, 0)


class Cyan(Color):
    """
    Standard cyan color: (0, 255, 255, 255)
    """

    def __init__(self):
        super().__init__(0, 255, 255)


class Magenta(Color):
    """
    Standard magenta color: (255, 0, 255, 255)
    """

    def __init__(self):
        super().__init__(255, 0, 255)
