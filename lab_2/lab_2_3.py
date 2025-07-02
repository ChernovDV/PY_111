def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # TODO реализовать рекурсивный алгоритм нахождения факториала
    if not isinstance(n, int):  # Проверка на целочисленность
        raise TypeError("Аргумент должен быть целым числом")
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
