from random import randint, choice
from solver import Solver


class SolverWithMetrics(Solver):
    '''
    A subclass of Solver utilizing method override for tracking metrics.
    '''

    def __init__(self, width=10, height=10, num_bombs=10):
        super().__init__(width=width, height=height, num_bombs=num_bombs)
        self.num_iters = 0

        self.num_selections_by_iter = []
        self.num_flags_by_iter = []

        self.total_flags_by_iter = []
        self.total_selections_by_iter = []

        self.num_flagged = 0
        self.num_selected = 0

    def __repr__(self):
        return 'W' if not self.game_over else 'L'

    def solve(self):
        self.num_iters = 0
        self.select(randint(0, self.height - 1), randint(0, self.width - 1))
        self.display_board()

        while not self.game_over and self.num_hidden_tiles > self.num_bombs:
            num_changes = 0

            # flag all known bombs
            for i, j in self.identify_bombs():
                self.flag(i, j)
                self.num_flagged += 1
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

        # if self.game_over:
        #     print('Oops! You selected the bomb.')
        # else:
        #     print('Nice work legend!')
    
    def display_board(self):
        pass


if __name__ == '__main__':
    easy = (10, 10, 10)
    medium = (18, 14, 40)
    hard = (24, 20, 99)

    difficulty = easy

    s = Solver(*difficulty)
    s.solve()
