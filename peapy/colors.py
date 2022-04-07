class Color:
    """
    PeaPy's color class
    """

    def __init__(self, r: int, g: int, b: int, a: int = 255):
        """
        Construct a color

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
    def rgba(self):
        return (self.r, self.g, self.b, self.a)

    @property
    def rgb(self):
        return (self.r, self.g, self.b)

    @property
    def hex(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"


class White(Color):
    def __init__(self):
        super().__init__(255, 255, 255)


class Black(Color):
    def __init__(self):
        super().__init__(0, 0, 0)


class Red(Color):
    def __init__(self):
        super().__init__(255, 0, 0)


class Green(Color):
    def __init__(self):
        super().__init__(0, 255, 0)


class Blue(Color):
    def __init__(self):
        super().__init__(0, 0, 255)


class Yellow(Color):
    def __init__(self):
        super().__init__(255, 255, 0)


class Cyan(Color):
    def __init__(self):
        super().__init__(0, 255, 255)


class Magenta(Color):
    def __init__(self):
        super().__init__(255, 0, 255)
