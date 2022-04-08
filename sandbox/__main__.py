import os
import time

import peapy


def main():
    game = peapy.PeaPy()

    game.add_object(peapy.Object("player"))
    game["player"].add_component(peapy.Transform(100, 100, 50, 50, 0))
    game["player"].add_component(
        peapy.Renderer(
            peapy.textures.Rectangle(),
            peapy.colors.Black(),
        )
    )
    game["player"].add_component(peapy.RectCollider())

    game.add_object(peapy.Object("enemy"))
    game["enemy"].add_component(peapy.Transform(100, 200, 50, 50, 0))
    game["enemy"].add_component(
        peapy.Renderer(peapy.textures.Rectangle(), peapy.colors.Red())
    )
    game["enemy"].add_component(peapy.RectCollider())

    while game.update():
        game["player"]["Transform"].y += 1

        game.logger.info(game["player"]["RectCollider"].is_colliding("enemy"))


if __name__ == "__main__":
    main()
