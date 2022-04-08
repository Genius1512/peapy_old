import peapy
import random

import enemy
import player


def main():
    config = peapy.config.get_default_config()
    config.window.width = 400

    game = peapy.PeaPy(config=config)

    game.add_object(player.player("Player"))
    game.add_object(enemy.Enemy("Enemy"))

    game.game_over = False
    game.score = 0
    rand_num = 75

    while game.update():
        if game.game_over:
            break

        if rand_num == 5:
            break

        if game.frame_count % 500 == 0:
            rand_num -= 5
            print("Speed up!")

        if random.randint(0, rand_num) == 0:
            game.add_object(enemy.Enemy("Enemy" + str(game.frame_count)))

    if game.game_over:
        print("Game Over")
        print("Score: " + str(game.score))
    else:
        print("You Win")


if __name__ == "__main__":
    main()

