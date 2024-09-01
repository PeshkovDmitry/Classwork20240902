"""
Задание №2
📌 Доработаем задачу 1.
📌 Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
"""

import json


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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("Task02.json", "w") as file:
            json.dump(self._list, file)


factorial = Factorial(5)
with factorial as f:
    f(1)
    f(2)
    f(3)
    f(4)
    f(5)
    print(f)
    f(6)
    print(f)
