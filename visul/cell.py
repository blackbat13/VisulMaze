from visul.point import Point


class Cell:
    def __init__(self, pos: Point, width: float, height: float):
        self._pos = pos
        self._sides = [True for _ in range(4)]
        self._width = width
        self._height = height
        self._movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self._visited = False

    @property
    def pos(self) -> Point:
        return self._pos

    @property
    def sides(self) -> list:
        return self._sides

    @property
    def visited(self) -> bool:
        return self._visited

    @visited.setter
    def visited(self, value: bool):
        self._visited = value

    def draw(self, context):
        context.beginPath()
        context.strokeStyle = "#000"
        context.lineWidth = 5
        x, y = self._pos.x, self._pos.y
        for i in range(4):
            nx = x + self._movement[i][0] * self._width
            ny = y + self._movement[i][1] * self._height

            if self._sides[i]:
                context.moveTo(x, y)
                context.lineTo(nx, ny)

            x, y = nx, ny

        context.stroke()

    def remove_side(self, side: int):
        self._sides[side] = False
