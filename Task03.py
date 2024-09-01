"""
Задание №3
📌 Создайте класс-генератор.
📌 Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
📌 Если переданы два параметра, считаем step=1.
📌 Если передан один параметр, также считаем start=1.
"""


class Factorial:

    def __init__(self, stop: int, start: int = 1, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self._current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._current > self.stop:
            raise StopIteration
        res = 1
        for num in range(1, self._current + 1):
            res *= num
        self._current += self.step
        return res


factorial = Factorial(5, 2, 2)
for f in factorial:
    print(f)