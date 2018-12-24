# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов (n > 0) ряда чисел (1 -0.5 0.25 -0.125 ...): '))

sum_series = 0
prev = 0

for i in range(n):
    if i == 0:
        sum_series = 1
        prev = 1
        continue
    current = prev * -0.5
    sum_series += current
    prev = current

print(f'Сумма {n} элементов = {sum_series}')
