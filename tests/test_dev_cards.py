from package.game_board import Board, Tile, Player

def test_board_get_dev():
    board = Board()
    last_dev = board.get_dev()

    assert last_dev == 'monopoly'

def test_board_get_dev_shuffled():
    board = Board()
    board.shuffle_devs()
    random_dev = board.get_dev()
    possible_devs = ['year_of_plenty', 'monopoly', 'road_building', 'knight', 'victory_point']

    assert random_dev in possible_devs


def test_board_get_dev_shuffled_stress():
    board = Board()
    board.shuffle_devs()
    for i in range(25):
        board.get_dev()
    out_of_bounds_dev = board.get_dev()

    assert out_of_bounds_dev == 'none'

def test_player_buy_dev():
    board = Board()
    p1 = Player(1)
    p1.add_resource_card('Wheat')
    p1.add_resource_card('Ore')
    p1.add_resource_card('Sheep')

    new_dev = p1.buy_dev(board)

    assert new_dev == 'monopoly'

def test_player_buy_dev_multiple():
    board = Board()
    p1 = Player(1)
    p1.add_resource_card('Wheat', 5)
    p1.add_resource_card('Ore', 5)
    p1.add_resource_card('Sheep', 5)

    for i in range(4):
        p1.buy_dev(board)
    new_dev = p1.buy_dev(board)

    assert new_dev == 'road_building'

def test_player_buy_dev_no_resources():
    board = Board()
    p1 = Player(1)
    p1.add_resource_card('Wheat', 6)
    p1.add_resource_card('Ore', 5)
    p1.add_resource_card('Sheep', 7)

    for i in range(5):
        p1.buy_dev(board)
    new_dev = p1.buy_dev(board)

    assert new_dev == 'none'
