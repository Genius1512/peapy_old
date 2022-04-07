import os
import time

import peapy


def main():
    game = peapy.PeaPy()

    game.add_object(peapy.objects.Object("player"))
    game["player"].add_component(peapy.Transform(0, 0, 50, 50, 0))
    game["player"].add_component(
        peapy.Renderer(
            peapy.textures.Circle(),
            peapy.colors.Black(),
        )
    )

    while game.update():
        pass


if __name__ == "__main__":
    main()
