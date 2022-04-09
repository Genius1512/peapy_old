import peapy
from .__pygame import pygame


class Text(peapy.Component):
    """
    PeaPy text component
    """

    def __init__(
        self,
        text: str,
        font_size: int = 24,
        x_offset: int = 0,
        y_offset: int = 0,
        color: peapy.colors.Color = peapy.colors.Black(),
    ):
        """
        Construct a new Text object

        Args:
            text (str): The text to render
            font_size (int): The font size of the text
            x_offset (int): The x offset of the text
            y_offset (int): The y offset of the text
            color (Color): The color of the text
        """
        super().__init__()

        self.text = text
        self.font_size = font_size
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.color = color

        pygame.font.init()
        self.__font = pygame.font.SysFont("Arial", self.font_size)

    def set_font_size(self, font_size: int):
        """
        Set the font size of the text

        Args:
            font_size (int): The new font size
        """
        self.font_size = font_size
        self.__font = pygame.font.SysFont("Arial", self.font_size)

    # Called when the component is created
    def init(self, game: peapy.PeaPy, obj_name: str) -> peapy.PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Init component

        return self.peapy

    # Called every frame
    def update(self, game: peapy.PeaPy, obj_name: str) -> peapy.PeaPy:
        self.peapy = game  # The parent PeaPy object
        self.obj_name = obj_name  # The name of the parent object

        # Update component
        text = self.__font.render(self.text, True, self.color.rgba)
        self.peapy.screen.blit(
            text,
            (
                self.peapy[self.obj_name]["Transform"].x + self.x_offset,
                self.peapy[self.obj_name]["Transform"].y + self.y_offset,
            ),
        )

        return self.peapy
