from typing import List
import random

class Tile:
    def __init__(self, resource: str=None, production: int=None, location: int=None):
        self.resource: str = resource
        self.production: int = production
        self.location: int = location

    def __str__(self):
        return f'Tile ({self.location}): {self.production} {self.resource}'


class Board:
    def __init__(self):
        # Create a board with the following layout
        '''
            0   1
          2   3   4
            5   6
        '''
        # Each 
        self.board_ids: List[int] = [0,1,2,3,4,5,6]
        self.board: List[Tile] = [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()]
        self.resources: List[str] = ['wood', 'brick', 'sheep', 'wheat', 'ore']
        self.productions: List[int] = [2,3,4,5,6,7,8,9,10,11,12]


    def create_set_board(self):
        self.board.append(Tile('wheat', ))

    def create_random_board(self):
        for i in range(len(self.board)):
            self.board[i] = Tile(random.choice(self.resources), random.choice(self.productions), i)

    def __str__(self):
        ret_string = ''
        for tile in self.board:
            ret_string += f'{tile}\n'
        return ret_string
            

def main():
    b = Board()
    b.create_random_board()
    print(b)

if __name__ == '__main__':
    main()
