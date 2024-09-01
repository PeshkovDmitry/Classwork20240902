"""
Задание №4
📌 Доработайте класс прямоугольник из прошлых семинаров.
📌 Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений
(отрицательных).
📌 Используйте декораторы свойств.
"""


class Rectangle:
    """Класс, реализующий прямоугольник"""

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

    def __add__(self, other):
        return Rectangle((self.perimeter() + other.perimeter()) / 4)

    def __sub__(self, other):
        if other.perimeter() > self.perimeter():
            return Rectangle(0)
        return Rectangle((self.perimeter() - other.perimeter()) / 4)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.__height} и {self.__width}"

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"


if __name__ == "__main__":
    r_1 = Rectangle(5)
