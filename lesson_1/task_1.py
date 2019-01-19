# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите трехзначное число: '))

num1 = number % 10
num2 = number % 100 // 10
num3 = number // 100

sum = num1 + num2 + num3
prod = num1 * num2 * num3

print(f'Сумма цифр = {sum}')
print(f'Произведение цифр = {prod}')
