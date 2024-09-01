"""
Задание №1
📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
📌 Экземпляр должен запоминать последние k значений.
📌 Параметр k передаётся при создании экземпляра.
📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
"""


class Factorial:
    """Класс, реализующий расчет факториала числа"""

    def __init__(self, k: int):
        self._k = k
        self._list = []

    def __call__(self, *args, **kwargs):
        res = 1
        for num in range(1, args[0] + 1):
            res *= num
        self._list.append((args[0], res))
        if len(self._list) > self._k:
            self._list.pop(0)
        return res

    def __str__(self):
        return str(self._list)


f = Factorial(5)
f(1)
f(2)
f(3)
f(4)
f(5)
print(f)
f(6)
print(f)
