from visul.cell import Cell
from visul.point import Point
from visul.side import Side


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
        context.fillRect(0, 0, self._width, self._height)
        for row in range(self._row_count):
            for col in range(self._col_count):
                self._grid[row][col].draw(context)

    def make_path(self, row1: int, col1: int, row2: int, col2: int):
        orientation = self.get_orientation(row1, col1, row2, col2)
        self._grid[row1][col1].remove_side(orientation)
        self._grid[row2][col2].remove_side((orientation + 2) % 4)

    def get_orientation(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row2 > row1:
            return Side.BOTTOM
        if row2 < row1:
            return Side.TOP
        if col2 > col1:
            return Side.RIGHT
        if col2 < col1:
            return Side.LEFT

    def mark_as_visited(self, row: int, col: int):
        self._grid[row][col].visited = True

    def is_visited(self, row: int, col: int) -> bool:
        return self._grid[row][col].visited

    def in_grid(self, row: int, col: int) -> bool:
        return row >= 0 and row < self._row_count and col >= 0 and col < self._col_count