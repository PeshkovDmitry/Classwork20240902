"""
Задание №6
📌 Изменяем класс прямоугольника.
📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
"""


class Dimension:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if value >= 0:
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Размер стороны прямоугольника не может быть отрицательным')

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)


class Rectangle:
    """Класс, реализующий прямоугольник"""

    width = Dimension()
    height = Dimension()

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """Метод вычисления периметра прямоугольника"""
        return 2 * (self.height + self.width)

    def area(self):
        """Метод вычисления площади прямоугольника"""
        return self.width * self.height

    def __str__(self):
        return f"Прямоугольник со сторонами {self.height} и {self.width}"


if __name__ == "__main__":
    r = Rectangle(5, 4)
    print(r)
    r.width = 7
    print(r)
    r.width = -1