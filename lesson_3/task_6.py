# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 3
MIN_ITEM = 0
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

index_min = 0
index_max = 0

print(f'Изначальный массив:\n{array}\n')

for index, element in enumerate(array):
    if element > array[index_max]:
        index_max = index
    if element < array[index_min]:
        index_min = index

sum_min_max = 0

if abs(index_min - index_max) > 1:
    if index_min > index_max:
        from_index = index_max + 1
        to_index = index_min - 1
    else:
        from_index = index_min + 1
        to_index = index_max - 1

    for index in range(from_index, to_index + 1):
        sum_min_max = sum_min_max + array[index]

    print(f'Сумма элементов между минимальным элементом {array[index_min]} на позиции {index_min} и '
          f'максимальным элеметном {array[index_max]} на позиции {index_max} равна {sum_min_max}')
else:
    print(f'Между минимальным и максимальным элементами нет чисел, суммировать нечего (сумма равна нулю)')
