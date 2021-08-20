from random import randint
from tile import Tile


class Board:
    def __init__(self, width=10, height=10, num_bombs=10):
        self.width = width
        self.height = height
        self.num_bombs = num_bombs
        self.board = [
            [Tile(i, j) for j in range(self.width)]
            for i in range(self.height)
        ]

    def __repr__(self):
        return f'Board(w = {self.width}, h={self.height}, n={self.num_bombs})'

    def __str__(self):
        return '\n'.join(''.join(map(str, row_tiles)) for row_tiles in self.board)

    def __iter__(self):
        for i in range(self.height):
            for j in range(self.width):
                yield self.board[i][j]

    # board setup methods
    def _create_board(self, clicked_tile):
        '''
        Create a board by adding bombs randomly.
        It's important to note that bombs cannot appear on, or adjacent to the
        first selected tile.
        '''
        blank_tiles = set(self.tile_neighbors(clicked_tile))
        blank_tiles.add(clicked_tile)
        # add the bombs
        bombs_added = 0
        while bombs_added < self.num_bombs:
            # chose a random location to plave a bomb
            i, j = randint(0, self.height - 1), randint(0, self.width - 1)
            random_tile = self.board[i][j]
            # dont repeat bombs and dont place bomb on the orignal (i, j)
            if not random_tile.is_bomb() and random_tile not in blank_tiles:
                random_tile.make_bomb()
                self.increment_neighbors(random_tile)
                bombs_added += 1

    def make_tile_bomb(self, tile):
        tile.make_bomb()

    def increment_neighbors(self, tile):
        for tile in self.tile_neighbors(tile):
            tile.num_adjacent_bombs += 1

    def _is_inbounds(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width

    def tile_neighbors(self, tile):
        i, j = tile.i, tile.j
        neighbor_indices = (
            (i - 1, j),  # up
            (i + 1, j),  # down
            (i, j - 1),  # left
            (i, j + 1),  # right
            (i - 1, j - 1),  # top left
            (i - 1, j + 1),  # top right
            (i + 1, j - 1),  # bottom left
            (i + 1, j + 1)   # bottom right
        )
        for i, j in neighbor_indices:
            if self._is_inbounds(i, j):
                yield self.board[i][j]


if __name__ == '__main__':
    board = Board(10, 10, 10)
    selected_tile = Tile(randint(0, 9), randint(0, 9))
    print(f'Selected tile: {(selected_tile.i, selected_tile.j)}')
    board._create_board(selected_tile)
    print(board)
