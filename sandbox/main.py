import peapy


def main():
    game = peapy.PeaPy()
    game.add_object(peapy.Box(
        "Box",
        100,
        100,
        100,
        50
    ))

    while game.update():
        pass


if __name__ == "__main__":
    main()
