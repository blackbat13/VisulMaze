from settings import Settings
from visul.grid import Grid
import random


class Maze:
    def __init__(self):
        self._settings = Settings()
        self._canvas = document.getElementById("maze_canvas")
        self._canvas.width = self._canvas.clientWidth
        self._canvas.height = self._canvas.clientHeight

        self._settings.width = self._canvas.width
        self._settings.height = self._canvas.height

        self._context = self._canvas.getContext('2d')

        self._grid = None

    def generate(self):
        self._grid = Grid(self._canvas.width, self._canvas.height, 30, 30)
        self.recursive_backtracker(0, 0)
        self._grid.draw(self._context)

    def recursive_backtracker(self, row: int, col: int):
        if self._grid.is_visited(row, col):
            return

        self._grid.mark_as_visited(row, col)
        movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        random.shuffle(movement)

        for move in movement:
            nrow = row + move[0]
            ncol = col + move[1]
            if not self._grid.in_grid(nrow, ncol) or self._grid.is_visited(nrow, ncol):
                continue

            self._grid.make_path(row, col, nrow, ncol)
            self.recursive_backtracker(nrow, ncol)


maze = Maze()
