# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

import cProfile

SIZE = 100000  # размер массива целых цисел


def sieve(n):
    """ Решето Эратосфена
    """
    a = [0] * SIZE
    for i in range(SIZE):
        a[i] = i

    a[1] = 0

    m = 2
    n_num = 0
    while m < SIZE:
        if a[m] != 0:
            n_num += 1
            if n_num == n:
                return a[m]
            j = m * 2
            while j < SIZE:
                a[j] = 0
                j = j + m
        m += 1
    return 0


# $ python -m timeit -n 100 -s "import task_2" "task_2.sieve(10)"
# 100 loops, best of 5: 15.5 msec per loop  n = 10
# 100 loops, best of 5: 17.2 msec per loop  n = 20
# 100 loops, best of 5: 17.9 msec per loop  n = 30
# 100 loops, best of 5: 18.4 msec per loop  n = 40
# 100 loops, best of 5: 20.2 msec per loop  n = 50
# 100 loops, best of 5: 19.8 msec per loop  n = 100
# 100 loops, best of 5: 23.7 msec per loop  n = 1000
#
# cProfile.run('sieve(1000)')
#
# 1    0.016    0.016    0.016    0.016 task_2.py:8(sieve)  n = 10
# 1    0.017    0.017    0.017    0.017 task_2.py:8(sieve)  n = 20
# 1    0.018    0.018    0.018    0.018 task_2.py:8(sieve)  n = 30
# 1    0.018    0.018    0.018    0.018 task_2.py:8(sieve)  n = 40
# 1    0.018    0.018    0.018    0.018 task_2.py:8(sieve)  n = 50
# 1    0.020    0.020    0.020    0.020 task_2.py:8(sieve)  n = 100
# 1    0.023    0.023    0.023    0.023 task_2.py:8(sieve)  n = 1000
#
# Сложность O(n)


def not_sieve(n):
    """ Поиск в цикле
    """
    n_num = 0
    for num in range(2, SIZE):
        is_simple = True
        for div in range(num-1, 1, -1):
            if num % div == 0:
                is_simple = False
                break
        if is_simple:
            n_num += 1
        if n_num == n:
            return num
    return 0


# $ python -m timeit -n 100 -s "import task_2" "task_2.not_sieve(10)"
# 100 loops, best of 5: 18.2 usec per loop  n = 10
# 100 loops, best of 5: 79.9 usec per loop  n = 20
# 100 loops, best of 5: 184 usec per loop   n = 30
# 100 loops, best of 5: 406 usec per loop   n = 40
# 100 loops, best of 5: 695 usec per loop   n = 50
# 100 loops, best of 5: 4.03 msec per loop  n = 100
# 100 loops, best of 5: 23.2 msec per loop  n = 200
# 100 loops, best of 5: 63.6 msec per loop  n = 300
# 100 loops, best of 5: 124 msec per loop   n = 400
# 100 loops, best of 5: 214 msec per loop   n = 500
#
# cProfile.run('not_sieve(1000)')
#
# 1    0.000    0.000    0.000    0.000 task_2.py:51(not_sieve)  n = 10
# 1    0.000    0.000    0.000    0.000 task_2.py:51(not_sieve)  n = 20
# 1    0.000    0.000    0.000    0.000 task_2.py:51(not_sieve)  n = 30
# 1    0.000    0.000    0.000    0.000 task_2.py:51(not_sieve)  n = 40
# 1    0.001    0.001    0.001    0.001 task_2.py:51(not_sieve)  n = 50
# 1    0.004    0.004    0.004    0.004 task_2.py:51(not_sieve)  n = 100
# 1    0.023    0.023    0.023    0.023 task_2.py:51(not_sieve)  n = 200
# 1    0.064    0.064    0.064    0.064 task_2.py:51(not_sieve)  n = 300
# 1    0.129    0.129    0.129    0.129 task_2.py:51(not_sieve)  n = 400
# 1    0.217    0.217    0.217    0.217 task_2.py:51(not_sieve)  n = 500
# 1    0.325    0.325    0.325    0.325 task_2.py:51(not_sieve)  n = 600
# 1    0.485    0.485    0.485    0.485 task_2.py:51(not_sieve)  n = 700
# 1    0.663    0.663    0.663    0.663 task_2.py:51(not_sieve)  n = 800
# 1    0.880    0.880    0.880    0.880 task_2.py:51(not_sieve)  n = 900
# 1    1.064    1.064    1.064    1.064 task_2.py:51(not_sieve)  n = 1000
#
# Сложность O(n**2)


def test_func(func):
    """ Тест реализаций
    """
    # список простых чисел с Википедии
    simple = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
              103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    for i in range(len(simple)):
        if func(i+1) == simple[i]:
            print(f'TEST {i + 1} - OK')
        else:
            print(f'TEST {i + 1} - ERROR')
    print()


# Тестируем реализации
# test_func(sieve)
# test_func(not_sieve)




