# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
# введено число 3486, то надо вывести число 6843.

num = int(input('Введите целое положительное число: '))
r_num = ''
while num // 10 != 0:
    r_num = r_num + f'{num % 10}'
    num = num // 10
r_num = r_num + f'{num}'
r_num = int(r_num)
print(f'{r_num}')
