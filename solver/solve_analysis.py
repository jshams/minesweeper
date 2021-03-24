from solver_with_metrics import SolverWithMetrics
from math import sqrt
import matplotlib.pyplot as plt

class ManySolveMetrics:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines

        self.all_solves = []
        self.num_games = 0
        self.num_games_won = 0
        self.num_games_lost = 0
        self.average_flagged_pct = 0
        self.average_num_iters = 0
    
    @property
    def win_percentage(self):
        return self.num_games_won / self.num_games

    def solve_n_times(self, n):
        '''
        solve n games of minesweeper and update the data from all of them.
        '''
        for _ in range(n):
            self._add_solve()

        self.recalculate_metrics()

    def _add_solve(self):
        s = SolverWithMetrics(self.width, self.height, self.num_mines)
        s.solve()
        self.all_solves.append(s)

    def _get_new_average(self, avg, n, count):
        return (avg * count + n) / (count + 1)

    def recalculate_metrics(self):
        self.num_games = len(self.all_solves)
        self.num_games_won = sum(not s.game_over for s in self.all_solves)
        self.num_games_lost = sum(s.game_over for s in self.all_solves)
        self.average_flagged_pct = self.average(
            [s.num_flagged for s in self.all_solves]) / self.num_mines
        
        self.average_num_iters = self.average(
            [s.num_iters for s in self.all_solves]
        )

    def average(self, nums):
        return sum(nums) / len(nums)


class MetricsByBombs:
    def __init__(self, area, num_mines_range=(5, 20), n_iters=50):
        self.area = area
        self.num_mines_range = num_mines_range
        self.n_iters = n_iters

        self.width = int(sqrt(area))
        self.height = int(sqrt(area))
        self.metrics = []
    
        for num_mines in range(*num_mines_range):
            print(f'Solving {self.n_iters} games with {num_mines} mines')
            m = ManySolveMetrics(self.width, self.height, num_mines)
            self.metrics.append(m)
            m.solve_n_times(n_iters)

    def plot_win_percentage(self):
        num_mines = list(range(*self.num_mines_range))
        win_pctgs = [s.win_percentage for s in self.metrics]

        plt.plot(num_mines, win_pctgs, 'bo')
        plt.title('Win Percentage by Bomb Count')
        plt.show()

    def plot_average_flagged_pct(self):
        num_mines = list(range(*self.num_mines_range))
        avg_flagged = [s.average_flagged_pct for s in self.metrics]

        plt.plot(num_mines, avg_flagged, 'bo')
        plt.title('Average Flagged Pct by Bomb Count')
        plt.show()

    def plot_num_iterations(self):
        num_mines = list(range(*self.num_mines_range))
        avg_iters = [s.average_num_iters for s in self.metrics]

        plt.plot(num_mines, avg_iters, 'bo')
        plt.title('Average Number of Matrix Iters by Bomb Count')
        plt.show()


if __name__ == '__main__' and False:
    easy = (10, 10, 10)
    medium = (18, 14, 40)
    hard = (24, 20, 99)

    difficulty = medium

    s = ManySolveMetrics(*difficulty)
    s.solve_n_times(100)

    print('all_solves:', s.all_solves)
    print('num_games:', s.num_games)
    print('num_games_won:', s.num_games_won)
    print('num_games_lost:', s.num_games_lost)
    print('average_flagged_pct:', s.average_flagged_pct)

if __name__ == '__main__':
    a = MetricsByBombs(100, (1, 25))
    a.plot_win_percentage()
    a.plot_average_flagged_pct()
    a.plot_num_iterations()