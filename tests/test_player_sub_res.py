from package.game_board import Player, Tile, Board
import pytest

def test_player_sub_res():
	p1 = Player(1)
	p1.add_resource_card('Wheat', 3)
	p1.add_resource_card('Ore', 4)
	p1.add_resource_card('Sheep', 2)

	p1.remove_resource_card('Ore')

	ore_cards = p1.resource_cards['Ore']

	assert ore_cards == 3
	
def test_player_sub_res_multiple():
	p1 = Player(1)
	p1.add_resource_card('Wheat', 3)
	p1.add_resource_card('Ore', 4)
	p1.add_resource_card('Sheep', 2)

	p1.remove_resource_card('Wheat', 2)

	wheat_cards = p1.resource_cards['Wheat']
	
	assert wheat_cards == 1

def test_player_sub_res_type_error():
	with pytest.raises(TypeError) as e_info:
		p1 = Player(1)
		p1.add_resource_card('Wheat', 3)
		p1.add_resource_card('Ore', 4)
		p1.add_resource_card('Sheep', 2)

		p1.remove_resource_card(4)

def test_player_sub_res_value_error():
	with pytest.raises(ValueError) as e_info:
		p1 = Player(1)
		p1.add_resource_card('Wheat', 3)
		p1.add_resource_card('Ore', 4)
		p1.add_resource_card('Sheep', 2)

		p1.remove_resource_card('Wood')
		
def test_player_sub_res_value_error2():
	with pytest.raises(ValueError) as e_info:
		p1 = Player(1)
		p1.add_resource_card('Wheat', 3)
		p1.add_resource_card('Ore', 4)
		p1.add_resource_card('Sheep', 2)

		p1.remove_resource_card('Sheep', 3)
