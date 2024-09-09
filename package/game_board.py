from typing import List, Dict
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
        self.settle_spots: List[str] = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
        self.dev_cards: List[str] = ['victory_point']*5 + ['knight']*14 + ['road_building']*2 + ['year_of_plenty']*2 + ['monopoly']*2


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

    
    def shuffle_devs(self) -> None:
        random.shuffle(self.dev_cards)
        return

    def get_dev(self) -> str:
        if not self.dev_cards:
            return "none"
        else:
            return self.dev_cards.pop()
    
    def __repr__(self):
        ret_string = ''
        for tile in self.board:
            ret_string += f'{str(tile)}\n'
        return ret_string

    # Currently configured for a 7 tile board
    def __str__(self):
        underline = "\u0332"

        ret_str =  f'      {self.settle_spots[0]}      {self.settle_spots[1]}\n'   
        ret_str += f'   {self.settle_spots[2]} {underline.join(repr(self.board[0])+" ")} {self.settle_spots[3]} {underline.join(repr(self.board[1])+" ")} {self.settle_spots[4]}\n'
        ret_str += f'   {self.settle_spots[5]}     {self.settle_spots[6]}     {self.settle_spots[7]}\n'
        ret_str += f'{self.settle_spots[8]} {underline.join(repr(self.board[2])+" ")} {self.settle_spots[9]} {underline.join(repr(self.board[3])+" ")} {self.settle_spots[10]} {underline.join(repr(self.board[4])+" ")} {self.settle_spots[11]}\n'
        ret_str += f'{self.settle_spots[12]}     {self.settle_spots[13]}     {self.settle_spots[14]}     {self.settle_spots[15]}\n'
        ret_str += f'   {self.settle_spots[16]} {underline.join(repr(self.board[5])+" ")} {self.settle_spots[17]} {underline.join(repr(self.board[6])+" ")} {self.settle_spots[18]}\n'
        ret_str += f'   {self.settle_spots[19]}     {self.settle_spots[20]} {self.settle_spots[21]}\n'
        ret_str += f'      {self.settle_spots[22]}     {self.settle_spots[23]}'
        return ret_str
    
class Player:
    def __init__(self, player_number: int):
        self.player_number = player_number
        self.resource_cards: Dict[str, int] = {
            "Wheat": 0,
            "Ore": 0,
            "Sheep": 0,
            "Brick": 0,
            "Lumber": 0
        }
        self.victory_points = 0

    
    def add_resource_card(self, res_card_type: str, num_cards: int=1) -> None:
        if not isinstance(res_card_type, str):
            raise TypeError(f"Invalid input: '{res_card_type}'. Must be a string")
        elif res_card_type not in self.resource_cards.keys():
            raise ValueError(f"Invalid resource card type: '{res_card_type}'. Input type must be in:\n{self.resource_cards.keys()}")
        else:
            self.resource_cards[res_card_type] += num_cards

    def remove_resource_card(self, res_card_type: str, num_cards: int=1) -> None:
        if not isinstance(res_card_type, str):
            raise TypeError(f"Invalid input: '{res_card_type}'. Must be a string")
        elif res_card_type not in self.resource_cards.keys():
            raise ValueError(f"Invalid resource card type: '{res_card_type}'. Input type must be in:\n{self.resource_cards.keys()}")
        elif self.resource_cards[res_card_type] < num_cards:
            raise ValueError(f"Player does not have '{num_cards}' '{res_card_type}' to remove.")
        else:
            self.resource_cards[res_card_type] -= num_cards
    
    def buy_dev(self, board: Board) -> str:
        if (self.resource_cards['Wheat'] >= 1) and (self.resource_cards['Sheep'] >= 1) and (self.resource_cards['Ore'] >= 1):
            new_dev = board.get_dev()
            self.resource_cards['Wheat'] -= 1
            self.resource_cards['Sheep'] -= 1
            self.resource_cards['Ore'] -= 1
        else:
            new_dev = 'none'
            print('No development cards remaining!')
        return new_dev


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
    print(b.dev_cards)
    b.shuffle_devs()
    print(b.dev_cards)

if __name__ == '__main__':
    main()
