# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трех уроков.

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

import cProfile

def func_v1(n):
    """ Первая реализация, через цикл
    """
    sum_series = 1
    if n > 1:
        prev = 1
        for _ in range(1, n):
            current = prev * -0.5
            sum_series += current
            prev = current
    return sum_series


# $ python -m timeit -n 100 -s "import task_1" "task_1.func_v1(100000)"
#
# 100 loops, best of 5: 829 nsec per loop   n = 10
# 100 loops, best of 5: 1.3 usec per loop   n = 20
# 100 loops, best of 5: 1.73 usec per loop  n = 30
# 100 loops, best of 5: 2.17 usec per loop  n = 40
# 100 loops, best of 5: 2.51 usec per loop  n = 50
# 100 loops, best of 5: 2.98 usec per loop  n = 60
# 100 loops, best of 5: 3.46 usec per loop  n = 70
# 100 loops, best of 5: 4.04 usec per loop  n = 80
# 100 loops, best of 5: 4.21 usec per loop  n = 90
# 100 loops, best of 5: 4.94 usec per loop  n = 100
# 100 loops, best of 5: 51.6 usec per loop  n = 1000
# 100 loops, best of 5: 546 usec per loop   n = 10000
# 100 loops, best of 5: 5.48 msec per loop  n = 100000
#
# cProfile.run('func_v1(100000)')
#
# 1    0.000    0.000    0.000    0.000 task_1.py:6(func_v1)   n = 10
# 1    0.000    0.000    0.000    0.000 task_1.py:6(func_v1)   n = 20
# 1    0.000    0.000    0.000    0.000 task_1.py:6(func_v1)   n = 30
# 1    0.000    0.000    0.000    0.000 task_1.py:6(func_v1)   n = 40
# 1    0.000    0.000    0.000    0.000 task_1.py:6(func_v1)   n = 50
# 1    0.000    0.000    0.000    0.000 task_1.py:6(func_v1)   n = 60
# 1    0.000    0.000    0.000    0.000 task_1.py:6(func_v1)   n = 70
# 1    0.000    0.000    0.000    0.000 task_1.py:6(func_v1)   n = 80
# 1    0.000    0.000    0.000    0.000 task_1.py:6(func_v1)   n = 90
# 1    0.000    0.000    0.000    0.000 task_1.py:6(func_v1)   n = 100
# 1    0.000    0.000    0.000    0.000 task_1.py:6(func_v1)   n = 1000
# 1    0.001    0.001    0.001    0.001 task_1.py:6(func_v1)   n = 10000
# 1    0.005    0.005    0.005    0.005 task_1.py:6(func_v1)   n = 100000
#
# Время растет линейно, сложность O(n)


def func_v2(n):
    """ Вторая реализация, через рекурсию
    """
    if n == 1:
        return 1
    return (-0.5) ** (n-1) + func_v2(n - 1)


# $ python -m timeit -n 100 -s "import task_1" "task_1.func_v2(100000)"
#
# 100 loops, best of 5: 2.14 usec per loop   n = 10
# 100 loops, best of 5: 4.84 usec per loop   n = 20
# 100 loops, best of 5: 7.05 usec per loop   n = 30
# 100 loops, best of 5: 9.4 usec per loop    n = 40
# 100 loops, best of 5: 12.6 usec per loop   n = 50
# 100 loops, best of 5: 14.8 usec per loop   n = 60
# 100 loops, best of 5: 17.5 usec per loop   n = 70
# 100 loops, best of 5: 20.5 usec per loop   n = 80
# 100 loops, best of 5: 22.3 usec per loop   n = 90
# 100 loops, best of 5: 25.7 usec per loop   n = 100
# RecursionError: maximum recursion depth exceeded in comparison  n = 1000
#
# cProfile.run('func_v2(1000)')
#
# 10/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2)   n = 10
# 20/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2)   n = 20
# 30/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2)   n = 30
# 40/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2)   n = 40
# 50/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2)   n = 50
# 60/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2)   n = 60
# 70/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2)   n = 70
# 80/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2)   n = 80
# 90/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2)   n = 90
# 100/1    0.000    0.000    0.000    0.000 task_1.py:54(func_v2)  n = 100
# RecursionError: maximum recursion depth exceeded in comparison   n = 1000
#
# Время растет линейно, сложность O(n)


def func_v3(n):
    """ Третья реализация, через формулу суммы геом. прогрессии
    """
    b1 = 1
    q = -0.5
    s = (b1 * (1-q**n)) / (1 - q)
    return s


# $ python -m timeit -n 100 -s "import task_1" "task_1.func_v3(100000)"
#
# 100 loops, best of 5: 340 nsec per loop  n = 10
# 100 loops, best of 5: 328 nsec per loop  n = 20
# 100 loops, best of 5: 316 nsec per loop  n = 30
# 100 loops, best of 5: 319 nsec per loop  n = 40
# 100 loops, best of 5: 378 nsec per loop  n = 50
# 100 loops, best of 5: 327 nsec per loop  n = 60
# 100 loops, best of 5: 319 nsec per loop  n = 70
# 100 loops, best of 5: 332 nsec per loop  n = 80
# 100 loops, best of 5: 321 nsec per loop  n = 90
# 100 loops, best of 5: 316 nsec per loop  n = 100
# 100 loops, best of 5: 319 nsec per loop  n = 1000
# 100 loops, best of 5: 345 nsec per loop  n = 10000
# 100 loops, best of 5: 344 nsec per loop  n = 100000
#
# cProfile.run('func_v3(100000)')
#
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 10
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 20
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 30
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 40
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 50
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 60
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 70
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 80
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 90
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 100
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 1000
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 10000
# 1    0.000    0.000    0.000    0.000 task_1.py:93(func_v3)   n = 100000
#
# Время константно и не зависит от входных данных, сложность O(1)

def test_func(func):
    """ Тест реализаций
    """
    sum_5 = [1, 0.5, 0.75, 0.625, 0.6875]
    for i in range(5):
        if round(func(i+1), 4) == sum_5[i]:
            print(f'TEST {i+1} - OK')
        else:
            print(f'TEST {i+1} - ERROR')
    print()


# Тестируем реализации
# test_func(func_v1)
# test_func(func_v2)
# test_func(func_v3)


# ВЫВОД
# Проведя анализ можно сказать, что самым быстрым вариантом стало решение с использованием формулы.
# В данном случае сложность алгоритма не зависит от количества входных данных и является постоянной.
#
# Мой первоначальный вариант занимает второе место и имеет сложность O(n). Вариант с рекурсией не отличается по
# сложности, от первого, но работает медленнее.

