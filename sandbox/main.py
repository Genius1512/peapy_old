import peapy


def main():
    game = peapy.PeaPy()
    game.add_object(peapy.Object("player"))
    game["player"].add_component(peapy.Transform(
        100,
        100,
        100,
        50,
        45
    ))
    game["player"].add_component(peapy.Renderer(
        peapy.textures.Rectangle()
    ))

    while game.update():
        pass


if __name__ == "__main__":
    main()
