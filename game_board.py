from typing import List
import random

class Tile:
	def __init__(self, resource: str=None, production: int=None, location: int=None):
		self.resource: str = resource
		self.production: int = production
		self.location: int = location

	def __str__(self):
		return f'Tile ({self.location}): {self.production} {self.resource}'

	def __repr__(self):
		return f'{self.production}{self.resource[0].upper()}'


class Board:
	def __init__(self):
		# Create a board with the following layout
		'''
		  0   1
		2   3   4
		  5   6
		'''

		self.board_ids: List[int] = [0,1,2,3,4,5,6]
		self.board: List[Tile] = [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()]
		self.resources: List[str] = ['lumber', 'brick', 'sheep', 'wheat', 'ore']
		self.productions: List[int] = [2,3,4,5,6,7,8,9,10,11,12]


	def create_custom_board(self):
		custom_productions = [4,5,6,8,9,4]
		custom_resources = ['wheat', 'wheat', 'lumber', 'sheep', 'ore', 'brick']
		
		# Set up the desert tile first
		desert_location = random.randrange(7)
		self.board[desert_location] = Tile('desert', 7, desert_location)
		
		for i in range(7):
			if i != desert_location:
				res: str = random.choice(custom_resources)
				custom_resources.remove(res)
				prod: int = random.choice(custom_productions)
				custom_productions.remove(prod)
				self.board[i] = Tile(res, prod, i)
			

	def create_random_board(self):
		for i in range(len(self.board)):
			self.board[i] = Tile(random.choice(self.resources), random.choice(self.productions), i)

	def __repr__(self):
		ret_string = ''
		for tile in self.board:
			ret_string += f'{str(tile)}\n'
		return ret_string

	# Currently configured for a 7 tile board
	def __str__(self):
		ret_str =  '       A      B\n'   
		ret_str += f'   C  {repr(self.board[0])}  D  {repr(self.board[1])}  E\n'
		ret_str += '   F      G      H\n'
		ret_str += f'I  {repr(self.board[2])}  J  {repr(self.board[3])}  K  {repr(self.board[4])}  L\n'
		ret_str += 'M      N      O      P\n'
		ret_str += f'   P  {repr(self.board[5])}  Q  {repr(self.board[6])}  R\n'
		ret_str += '   S      T      U\n'
		ret_str += '       V       W'
		return ret_str
		
			
#def test_vis():
	#print(f'''
        #   c /a\\ d/ b \\e\n
	#   | {self.board[0]}  | {self.board[1]  |\n   
	#   f\\ i /g\\ j /h
	#''')       

def main():
	b = Board()
	b.create_custom_board()
	print(repr(b))
	print(str(b))
if __name__ == '__main__':
	main()
