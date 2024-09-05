from package.game_board import Player, Tile, Board

def test_player_add_res():
	p1 = Player(1)
	p1.add_resource_card('Wheat')

	wheat_cards = p1.resource_cards['Wheat']

	assert wheat_cards == 1

def test_player_add_res_multiple():
	p1 = Player(1)
	p1.add_resource_card('Brick', 5)
	
	brick_cards = p1.resource_cards['Brick']

	assert brick_cards == 5	
