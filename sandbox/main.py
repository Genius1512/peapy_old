import peapy


def main():
    game = peapy.PeaPy()
    game.add_object(peapy.Object("player"))
    game["player"].add_component(
        peapy.Renderer(peapy.textures.Rectangle(), peapy.colors.Red())
    )

    while game.update():
        pass


if __name__ == "__main__":
    main()
