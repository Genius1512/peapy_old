import peapy


def main():
    game = peapy.PeaPy(peapy.config.default_config)

    while game.update():
        pass


if __name__ == "__main__":
    main()
