import peapy


class Bullet(peapy.Object):
    def __init__(self, name: str, x: int):
        super().__init__(name)

        self.size = 20
        self.x = x
        self.vel = 700

    # Called when the object is created
    def init(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game

        # Init object
        self.add_component(peapy.Transform(
            self.x,
            self.peapy.config.window.height - 25 - self.size,
            5,
            self.size
        ))
        self.add_component(peapy.Renderer(
            peapy.textures.Rectangle()
        ))
        self.add_component(peapy.Collider(
            peapy.textures.Rectangle()
        ))

        return self.peapy

    # Called every frame
    def update(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game  # The parent PeaPy object

        # Update object
        self.peapy[self.name]["Transform"].y -= self.vel * self.peapy.delta_time

        for obj in self.peapy.get_objects():
            if "Enemy" in obj:
                if self.peapy[self.name]["Collider"].is_colliding(obj):
                    self.peapy.remove_object(obj)
                    self.peapy.remove_object(self.name)
                    self.peapy["Score"].score += 1
                    break

        return self.peapy
