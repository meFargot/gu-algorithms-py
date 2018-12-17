# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три РАЗНЫХ целых числа.')
num_1 = int(input('Введите первое целое число: '))
num_2 = int(input('Введите второе целое число: '))
num_3 = int(input('Введите третье целое число: '))

if num_1 < num_2:
    if num_3 < num_1:
        mid_num = num_1
    elif num_2 < num_3:
        mid_num = num_2
    else:
        mid_num = num_3
elif num_3 < num_2:
    mid_num = num_2
elif num_3 < num_1:
    mid_num = num_3
else:
    mid_num = num_1

print(f'Средним является число {mid_num}')
