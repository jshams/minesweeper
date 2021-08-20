import unittest
from tile import Tile


class TestTile(unittest.TestCase):
    def test_init(self):
        tile = Tile(0, 2)
        assert tile.i == 0
        assert tile.j == 2
        assert tile.num_adjacent_bombs == 0
        assert tile.is_bomb() is False

    def test_tile_is_hashable(self):
        assert hasattr(Tile, '__hash__')
