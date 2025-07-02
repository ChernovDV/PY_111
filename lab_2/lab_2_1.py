"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:  # Проверка пустого массива   # TODO реализовать итеративный линейный поиск
        raise ValueError("Минимум невозможно найти в пустой последовательности")

    current_min = arr[0]  # Берём первый элемент массива как начальное минимальное значение
    min_indx = 0  # Запоминаем индекс текущего минимального элемента

    for i in range(1, len(arr)):  # Начинаем проверку элементов начиная со второго
        if arr[i] < current_min:  # Если нашли меньший элемент
            current_min = arr[i]  # Обновляем минимальный элемент
            min_indx = i  # Записываем новый индекс минимального элемента

    return min_indx  # Возвращаем индекс найденного минимального элемента




