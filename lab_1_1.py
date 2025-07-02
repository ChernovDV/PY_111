"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self._queue = [] # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:     # сложность операции О(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._queue.append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:                 # сложность операции О(n)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self._queue:
            raise IndexError("Очередь пуста")
        return self._queue.pop(0)  # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:       # сложность операции О(1)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Индексация должна выполняться целыми числами")

            # Проверяем, что индекс находится в границах очереди
        if ind < 0 or ind >= len(self._queue):
            raise IndexError("Указанный индекс вне диапазона очереди")

            # Возврат значения элемента по индексу
        return self._queue[ind]  # TODO реализовать метод peek

    def clear(self) -> None:                   # сложность операции О(1)
        """ Очистка очереди. """
        self._queue.clear()  # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self._queue)  # TODO реализовать метод __len__

    # def __repr__(self):
    #     return f"({self._queue})"


