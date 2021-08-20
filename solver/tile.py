class Tile:
    def __init__(self, i, j, num_adjacent_bombs=0, is_bomb=False):
        self.i = i
        self.j = j
        self.num_adjacent_bombs = num_adjacent_bombs
        self._is_bomb = is_bomb

    def is_bomb(self):
        return self._is_bomb

    def is_blank(self):
        return self.num_adjacent_bombs == 0 and not self.is_bomb()

    def __repr__(self):
        return f'Tile(i={self.i}, j={self.j}, n={self.num_adjacent_bombs}, b={self.is_bomb()})'

    def __str__(self):
        if self.is_bomb():
            return '\033[91m*\033[0m'
        elif self.is_blank():
            # blank visible tile
            return ' '
        else:
            ENDC = '\033[0m'
            colors = [
                None,
                '\033[92m',  # 1 green
                '\033[94m',  # 2 blue
                '\033[91m',  # 3 red
                '\033[95m',  # 4 pink/purple
                '\033[96m',  # 5+ light blue
            ]
            color = colors[min(self.num_adjacent_bombs, 5)]
            return f'{color}{self.num_adjacent_bombs}{ENDC}'

    def __hash__(self):
        return hash((self.i, self.j))
    
    def __eq__(self, other_tile):
        '''
        Equals method to compare the location of 2 tiles. Should only be
        used by test_board - consider using another method of checking tile
        equality
        '''
        return self.i == other_tile.i and self.j == other_tile.j

    def make_bomb(self):
        self._is_bomb = True
