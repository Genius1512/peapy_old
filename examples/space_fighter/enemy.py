import peapy
import random
import time


class Enemy(peapy.Object):
    def __init__(self, name: str):
        super().__init__(name)

    def init(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game

        self.size = 30

        # Init object
        self.add_component(
            peapy.Transform(
                random.randint(self.size, game.config.window.width - self.size),
                self.size + 2,
                self.size,
                self.size,
            )
        )
        self.add_component(
            peapy.Renderer(peapy.textures.Rectangle(), peapy.colors.Red())
        )
        self.add_component(peapy.RectCollider())

        return self.peapy

    def update(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game

        # Update object
        self["Transform"].y += self.peapy.delta_time * 100

        if self["RectCollider"].is_colliding("Player"):
            self.peapy.game_over = True
            peapy.sound.Sound("assets/sounds/explosion.wav").play()
            time.sleep(0.5)
            return self.peapy

        if self["Transform"].y > game.config.window.height:
            self.peapy.remove_object(self.name)
            self.peapy["Score"].score += 1
            peapy.sound.Sound("assets/sounds/score.wav").play()

        return self.peapy
