from settings import Settings
from visul.grid import Grid


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
        self._grid = Grid(self._canvas.width, self._canvas.height, 50, 50)
        self._grid.draw(self._context)


maze = Maze()
