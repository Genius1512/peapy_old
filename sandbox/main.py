import peapy


def main():
    game = peapy.PeaPy()
    game.add_object(peapy.Object("player"))
    game["player"].add_component(peapy.Transform(x=100, y=100, width=100, height=50))
    game["player"].add_component(peapy.Collider(peapy.textures.Rectangle()))
    game["player"].add_component(
        peapy.Renderer(peapy.textures.Rectangle(), peapy.colors.Red())
    )

    game.add_object(peapy.Object("player2"))
    game["player2"].add_component(peapy.Transform(x=100, y=100, width=100, height=50))
    game["player2"].add_component(peapy.Collider(peapy.textures.Circle()))
    game["player2"].add_component(
        peapy.Renderer(peapy.textures.Circle(), peapy.colors.Green())
    )

    print(game["player2"]["Collider"].is_colliding("player"))

    while game.update():
        pass


if __name__ == "__main__":
    main()
