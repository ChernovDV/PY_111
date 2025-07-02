from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if len(container) <= 1:    # TODO реализовать алгоритм сортировки подсчетами
        return list(container)

    max_value = max(container) + 1  # определяем максимальный элемент массива и добавляем единицу
    count_array = [0] * max_value  # создаем массив счётчиков нужного размера

    for num in container:
        count_array[num] += 1  # считаем количество каждого числа

    sorted_container = []
    for i, count in enumerate(count_array):
        sorted_container.extend([i] * count)  # восстанавливаем отсортированный массив по количеству повторений

    return sorted_container

