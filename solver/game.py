import sys
from board import Board


class Game(Board):
    def __init__(self, width=10, height=10, num_bombs=10):
        super().__init__(width=width, height=height, num_bombs=num_bombs)
        self.visible_board = [[0] * self.width for _ in range(self.height)]
        self.game_over = False
        # self._create_board(5, 5)
        self.num_hidden_tiles = width * height

    def play(self):
        while not self.game_over and self.num_hidden_tiles > self.num_bombs:
            self.prompt_move()
            self.display_board()

        if self.game_over:
            print('Oops! You selected the bomb.')
        else:
            print('Nice work legend!')

    def prompt_move(self):

        self.display_board()

        flag_or_select = None
        while flag_or_select != 'f' and flag_or_select != 's':
            flag_or_select = input(
                'Would you like to flag or select a tile? (f/s): ')

        i = None
        while i is None:
            print()
            indices = input(
                'Enter the coordinate of the item separeted by ", ": ')
            try:
                i, j = tuple(map(int, indices.split(', ')))
                if not self._is_inbounds(i, j):
                    print('Coordinates entered out of bounds.')
                    i = None
                elif self._tile_is_visible(i, j):
                    print('Coordinates entered have already been selected.')
                    i = None
                elif self.is_flag(i, j) and flag_or_select == 's':
                    print('Cannot select coordinate that has been flagged.')

            except ValueError:
                print('Please enter a valid value.')

        if flag_or_select == 'f':
            self.flag(i, j)
        else:
            self.select(i, j)

    # game actions

    def _tile_is_visible(self, i, j):
        return self.visible_board[i][j] == 1

    def flag(self, i, j):
        if self.is_flag(i, j):
            self.visible_board[i][j] = 0
        else:
            self.visible_board[i][j] = 'f'

    def is_flag(self, i, j):
        return self.visible_board[i][j] == 'f'

    def select(self, i, j):
        # print(self.board)
        if self._tile_is_visible(i, j):
            return
        if self.is_flag(i, j):
            return

        if self.board is None:
            self._create_board(i, j)

        self.visible_board[i][j] = 1
        self.num_hidden_tiles -= 1

        if self.is_bomb(i, j):
            self.game_over = True
        # if a tile is blank (next to 0 bombs) reveal all its neighbors
        elif self.is_blank(i, j):
            for ni, nj in self.tile_neighbors(i, j):
                if not self._tile_is_visible(ni, nj):
                    try:
                        self.select(ni, nj)
                    except RecursionError:
                        rl = sys.getrecursionlimit()
                        sys.setrecursionlimit(rl * 2)
                        self.select(ni, nj)
'''
    # board vis
    def display_number_tile(self, i, j):
        num = self.board[i][j]
        ENDC = '\033[0m'

        colors = [None,
                  '\033[92m',  # 1 green
                  '\033[94m',  # 2 blue
                  '\033[91m',  # 3 red
                  '\033[95m',  # 4 pink/purple
                  '\033[96m',  # 5+ light blue
                  ]
        color = colors[min(num, 5)]
        return f'{color}{num}{ENDC}'

    def tile_representation(self, i, j):
        if not self._tile_is_visible(i, j) and not self.is_flag(i, j):
            # block representation of blocked tile
            return '\u2588'
        elif self.is_flag(i, j):
            # red block to show flag
            return '\033[91m\u2588\033[0m'
        elif self.is_blank(i, j):
            # blank visible tile
            return ' '
        elif self.is_bomb(i, j):
            return '\033[91m*\033[0m'
        else:
            # the number on the visible tile
            return self.display_number_tile(i, j)

    def display_board(self):
        rows = []
        # rows.append('  ' + ''.join(map(str, range(self.width))))
        for i in range(self.height):
            row = ''
            # row += f'{0} '
            for j in range(self.width):
                row += self.tile_representation(i, j)
            rows.append(row)

        print()
        for row in rows:
            print(row)


if __name__ == '__main__':
    g = Game(5, 5, 2)
    g.play()
'''