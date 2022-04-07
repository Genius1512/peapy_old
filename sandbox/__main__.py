import peapy


def main():
    game = peapy.PeaPy()

    game.add_object(peapy.objects.Object("player"))
    game.add_object(peapy.objects.Object("enemy"))

    game.get_object("player").add_component(peapy.components.Component())
    game.get_object("enemy").add_component(peapy.components.Component())

    peapy.print_peapy_tree(game)

    while game.update():
        pass


if __name__ == "__main__":
    main()
