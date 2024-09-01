"""
Задание №5
📌 Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.
"""


class Rectangle:
    """Класс, реализующий прямоугольник"""

    __slots__ = ["__width", "__height"]

    def __init__(self, width, height = None):
        self.__width = width
        if height is None:
            self.__height = width
        else:
            self.__height = height

    def perimeter(self):
        """Метод вычисления периметра прямоугольника"""
        return 2 * (self.__height + self.__width)

    def area(self):
        """Метод вычисления площади прямоугольника"""
        return self.__width * self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value >= 0:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value >= 0:
            self.__height = value

    def __str__(self):
        return f"Прямоугольник со сторонами {self.__height} и {self.__width}"


if __name__ == "__main__":
    r = Rectangle(5, 4)
    print(r)
    r.width = 7
    print(r)
