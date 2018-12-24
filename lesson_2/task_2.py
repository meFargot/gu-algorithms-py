# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def count_even(number):
    """
    Рекурсивно считаем количество четных цифр в числе
    """
    if number // 10 == 0:  # базовый случай
        if number % 2 == 0:
            return 1
        else:
            return 0
    else:
        if (number % 10) % 2 == 0:
            count = 1 + count_even(number // 10)
        else:
            count = 0 + count_even(number // 10)
        return count


def count_odd(number):
    """
    Рекурсивно считаем количество нечетных цифр в числе
    """
    if number // 10 == 0:  # базовый случай
        if number % 2 == 1:
            return 1
        else:
            return 0
    else:
        if (number % 10) % 2 == 1:
            count = 1 + count_odd(number // 10)
        else:
            count = 0 + count_odd(number // 10)
        return count


num = int(input('Введите натуральное число: '))

evens = count_even(num)

odds = count_odd(num)

print(f'Четных цифр: {evens}\nНЕчетных цифр: {odds}')
