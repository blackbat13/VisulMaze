from visul.cell import Cell
from visul.point import Point


class Grid:
    def __init__(self, width: float, height: float, col_count: int, row_count: int):
        self._width = width
        self._height = height
        self._col_count = col_count
        self._row_count = row_count
        self._cell_width = self._width / self._col_count
        self._cell_height = self._height / self._row_count
        self._grid = [
            [
                Cell(Point(col * self._cell_width, row * self._cell_height), self._cell_width, self._cell_height)
                for col in range(self._col_count)
            ] for row in range(self._row_count)
        ]

    def draw(self, context):
        context.fillStyle = "#fff"
        context.fillRect(0,0, self._width, self._height)
        for row in range(self._row_count):
            for col in range(self._col_count):
                self._grid[row][col].draw(context)
