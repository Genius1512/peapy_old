import peapy
import player


def main():
    game = peapy.PeaPy()

    game.add_object(player.Player("player1"))
    game["player1"].add_component(peapy.RectCollider(x_offset=0, y_offset=0, width=None, height=None))

    game.add_object(player.Player("player2"))
    game["player2"].add_component(peapy.RectCollider(x_offset=0, y_offset=0, width=None, height=None))
    game["player2"]["Transform"].y = 200

    while game.update():
        game["player1"]["Transform"].y += 1
        print(game["player1"]["RectCollider"].is_colliding("player2"))


if __name__ == "__main__":
    main()

