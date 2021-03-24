'''
To solve the board try to find flags with 100% confidence.
If a tile is found with 100% confidence.


'''
from random import randint, choice
from game import Game


class Solver(Game):
    def __init__(self, width=10, height=10, num_bombs=10):
        super().__init__(width=width, height=height, num_bombs=num_bombs)
        self.num_iters = 0

    # override add_flag
    def iter_nums(self):
        for i in range(self.height):
            for j in range(self.width):
                if self._tile_is_visible(i, j) and not self.is_blank(i, j):
                    yield i, j

    def iter_flags(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.is_flag(i, j):
                    yield i, j

    def get_tile_hidden_neighbors(self, i, j):
        for ni, nj in self.tile_neighbors(i, j):
            if not self._tile_is_visible(ni, nj):
                yield ni, nj

    def identify_bombs(self):
        '''finds a bomb that has 100% certainty. If none are completely certain
        None is returned'''
        for i, j in self.iter_nums():
            num = self.board[i][j]

            neighbors = list(self.get_tile_hidden_neighbors(i, j))
            if len(neighbors) == num:
                for ni, nj in neighbors:
                    if not self.is_flag(ni, nj):
                        yield ni, nj

    def identify_selections(self):
        '''search for numbers that have the satisfied number of flags
        surrounding flags around them. The leftover tiles can be selected.'''
        for i, j in self.iter_nums():
            if self.is_satisfied(i, j):
                for ni, nj in self.get_tile_hidden_neighbors(i, j):
                    if not self.is_flag(ni, nj):
                        yield ni, nj

    def is_satisfied(self, i, j):
        num = self.board[i][j]
        num_flags = 0
        for ni, nj in self.get_tile_hidden_neighbors(i, j):
            num_flags += self.is_flag(ni, nj)

        return num == num_flags

        neighbors = list(self.get_tile_hidden_neighbors(i, j))
        if len(neighbors) == num:
            return neighbors

    def make_random_selection(self):
        hidden_tiles = []
        for i in range(self.height):
            for j in range(self.width):
                if not self._tile_is_visible(i, j) and not self.is_flag(i, j):
                    hidden_tiles.append((i, j))
        i, j = choice(hidden_tiles)
        self.select(i, j)

    def solve(self):
        self.num_iters = 0
        self.select(randint(0, self.height - 1), randint(0, self.width - 1))
        self.display_board()

        while not self.game_over and self.num_hidden_tiles > self.num_bombs:
            num_changes = 0

            # flag all known bombs
            for i, j in self.identify_bombs():
                self.flag(i, j)
                num_changes += 1
            self.display_board()

            # find and select all valid selections
            for i, j in self.identify_selections():
                self.select(i, j)
                num_changes += 1
            self.display_board()

            if num_changes == 0:
                self.make_random_selection()
                self.display_board()

            self.num_iters += 2

        if self.game_over:
            print('Oops! You selected the bomb.')
        else:
            print('Nice work legend!')


if __name__ == '__main__':
    easy = (10, 10, 10)
    medium = (18, 14, 40)
    hard = (24, 20, 99)

    difficulty = easy

    s = Solver(*difficulty)
    s.solve()
