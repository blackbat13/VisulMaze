class Settings:
    def __init__(self):
        self.__width = 0
        self.__height = 0

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int):
        self.__width = value

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int):
        self.__height = value

    def read_settings(self):
        pass