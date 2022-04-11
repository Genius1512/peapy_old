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

    game.add_object(
        peapy.Object(
            "Score",
        )
    )
    game["Score"].add_component(peapy.Transform(0, 0, 0, 0))
    game["Score"].add_component(peapy.Text("0", 48))
    game["Score"].score = 0

    game.won = False
    game.game_over = False
    rand_num = 75

    while game.update():
        if game.game_over:
            break

        if rand_num == 5:
            game.won = True
            break

        if game.frame_count % 500 == 0:
            rand_num -= 5

        if random.randint(0, rand_num) == 0:
            game.add_object(enemy.Enemy("Enemy" + str(game.frame_count)))

        game["Score"]["Text"].text = str(game["Score"].score)

    if not game.won:
        print("Game Over")
        print("Score: " + str(game["Score"].score))
    else:
        print("You Win")


if __name__ == "__main__":
    main()
