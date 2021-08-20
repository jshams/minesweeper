import unittest
from board import Board, Tile
from random import randint


class TestBoard(unittest.TestCase):
    def test_create_board(self):
        board = Board(10, 10, 10)
        selected_tile = Tile(4, 5)
        board._create_board(selected_tile)
        assert board.num_bombs == sum(tile.is_bomb() for tile in board)

    def test_create_board_with_random_tile(self):
        board = Board(10, 10, 10)
        i = randint(0, 9)
        j = randint(0, 9)
        selected_tile = Tile(i, j)
        board._create_board(selected_tile)
        assert board.num_bombs == sum(tile.is_bomb() for tile in board)
        # ensure selected tile has no bombs next to it
        assert all(
            not tile.is_bomb() for tile in board.tile_neighbors(selected_tile)
        )

    def test_tile_neighbors_center_tile(self):
        board = Board(3, 3, 0)
        neighbors = board.tile_neighbors(Tile(1, 1))
        self.assertSetEqual(
            set(neighbors),
            set(
                Tile(i, j) for i, j in (
                    (0, 0), (0, 1), (0, 2),
                    (1, 0),         (1, 2),
                    (2, 0), (2, 1), (2, 2)
                )
            )
        )

    def test_tile_neighbors_left_edge(self):
        board = Board(3, 3, 0)
        neighbors = board.tile_neighbors(Tile(1, 0))
        self.assertSetEqual(
            set(neighbors),
            set(
                Tile(i, j) for i, j in (
                    (0, 0), (0, 1),
                            (1, 1),
                    (2, 0), (2, 1),
                )
            )
        )

    def test_tile_neighbors_bottom_edge(self):
        board = Board(3, 3, 0)
        neighbors = board.tile_neighbors(Tile(2, 1))
        self.assertSetEqual(
            set(neighbors),
            set(
                Tile(i, j) for i, j in (
                    (1, 0), (1, 1), (1, 2),
                    (2, 0),         (2, 2)
                )
            )
        )

    def test_tile_neighbors_top_left_corner(self):
        board = Board(3, 3, 0)
        neighbors = board.tile_neighbors(Tile(0, 0))
        self.assertSetEqual(
            set(neighbors),
            set(
                Tile(i, j) for i, j in (
                            (0, 1),
                    (1, 0), (1, 1)
                )
            )
        )

    def test_tile_neighbors_botton_right_corner(self):
        board = Board(3, 3, 0)
        neighbors = board.tile_neighbors(Tile(2, 2))
        self.assertSetEqual(
            set(neighbors),
            set(
                Tile(i, j) for i, j in (
                    (1, 1), (1, 2),
                    (2, 1)
                )
            )
        )
