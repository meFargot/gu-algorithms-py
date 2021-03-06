# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

print('Я считаю кол-во цифр в веденной последовательности чисел.')
num_count = int(input('Введите кол-во вводимых чисел (целое положительное число): '))
digit = int(input('Введите искомую цифру (0-9): '))

answer = 0

for i in range(num_count):
    cur_num = int(input(f'Введите целое положительное число ({i+1}-ое): '))
    while cur_num > 0:
        if cur_num % 10 == digit:
            answer += 1
        cur_num = cur_num // 10

print(f'В введеной последовательности чисел цифра {digit} встречается {answer} раз.')
