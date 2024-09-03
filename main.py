from game_board import Tile, Player, Board

def test_player_add() -> None:
    p1 = Player(1)
    p1.add_resource_card('Wheat')
    print(p1.resource_cards)
    p1.add_resource_card('Brick', 4)
    print(p1.resource_cards)
    p1.remove_resource_card('Brick', 2)
    print(p1.resource_cards)


def main():
    test_player_add()

if __name__ == '__main__':
    main()
