import peapy


def main():
    game = peapy.PeaPy(peapy.config.default_config)

    while game.update():
        game.logger.info(peapy.keyboard.get_pressed_keys())


if __name__ == "__main__":
    main()
