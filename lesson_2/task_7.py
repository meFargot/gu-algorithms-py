# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

print('Я проверяю, что для любого натурального n выполняется равенство 1+2+...+n = n(n+1)/2')
n = int(input('Введите любое натуральное число: '))

left_part = 0
right_part = 0

for i in range(n):
    left_part += i + 1

right_part = n * (n + 1) / 2

print(f'1+2+...+n = {left_part}')
print(f'n(n+1)/2 = {right_part}')

if left_part != right_part:
    print(f'Формула не верна: {left_part} <> {right_part}')
else:
    print(f'Формула верна: {left_part} = {right_part}')
