import peapy
import keyboard


class player(peapy.Object):
    def __init__(self, name: str):
        super().__init__(name)

    def init(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game

        # Init object
        self.size = 50
        self.vel = 300

        self.add_component(peapy.Transform(
            self.peapy.config.window.width / 2 - self.size / 2,
            self.peapy.config.window.height - 25 - self.size,
            self.size,
            self.size
        ))
        self.add_component(peapy.Renderer(
            peapy.textures.Rectangle(),
            peapy.colors.Black()
        ))
        self.add_component(peapy.RectCollider())

        return self.peapy

    def update(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game

        # Update object
        if keyboard.is_pressed('a') and not self["Transform"].x <= 0:
            self["Transform"].x -= game.delta_time * self.vel
        if keyboard.is_pressed('d') and not self["Transform"].x + self["Transform"].width >= self.peapy.config.window.width:
            self["Transform"].x += game.delta_time * self.vel

        return self.peapy
