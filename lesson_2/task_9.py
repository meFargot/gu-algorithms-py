# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

max_num = 0
max_num_digit_sum = 0

while True:
    number = int(input('Введите натуральное число (ноль для завершения): '))
    if number != 0:
        cur_num = number
        cur_digit_sum = 0
        while cur_num != 0:
            cur_digit_sum += cur_num % 10
            cur_num = cur_num // 10
        if cur_digit_sum > max_num_digit_sum:
            max_num_digit_sum = cur_digit_sum
            max_num = number
    else:
        break
print(f'Наибольшее число по сумме цифр = {max_num}; сумма цифр = {max_num_digit_sum}')
