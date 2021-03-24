from random import randint


class Board:
    def __init__(self, width=10, height=10, num_bombs=10):
        self.width = width
        self.height = height
        self.num_bombs = num_bombs
        self.board = None
        self.bomb_rep = 9

    # board setup methods

    def _create_board(self, i, j):
        self.board = [[0] * self.width for _ in range(self.height)]

        click_radius = set(self.tile_neighbors(i, j))
        click_radius.add((i, j))
        # add the bombs
        bombs_added = 0
        while bombs_added < self.num_bombs:
            # chose a random location to plave a bomb
            ri, rj = randint(0, self.height - 1), randint(0, self.width - 1)
            # dont repeat bombs and dont place bomb on the orignal (i, j)
            if not self.is_bomb(ri, rj) and (ri, rj) not in click_radius:
                self.board[ri][rj] = self.bomb_rep
                bombs_added += 1
                # add 1 to neighbors
                self.increment_neighbors(ri, rj)

    def increment_neighbors(self, i, j):
        for i, j in self.tile_neighbors(i, j):
            if not self.is_bomb(i, j):
                self.board[i][j] += 1

    def move(self, i, j):
        if self.board is None:
            self._create_board(i, j)

    # tile methods
    def _is_inbounds(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width

    def is_bomb(self, i, j):
        return self.board[i][j] == self.bomb_rep

    def is_blank(self, i, j):
        return self.board[i][j] == 0

    def tile_val(self, i, j):
        return self.board[i][j]

    def tile_neighbors(self, i, j):
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
                yield i, j
