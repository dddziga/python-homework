"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numb):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numb]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n != 0.0 and n != 1:
        d = 2
        while n % d != 0:
            d += 1
        return d == n
    elif n == 0.0 or n == 1:
        return False

def filter_numbers(numb, fil):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    >>> filter_numbers([2, 3, 4, 5], PRIME)
    <<< [2, 3, 5]
    """
    if fil == EVEN:
        return [number for number in numb if number % 2 == 0]

    if fil == ODD:
        return [number for number in numb if number % 2 != 0]

    if fil == PRIME:
        tmp = []
        for i in numb:
            if is_prime(i):
                tmp.append(i)
        return tmp