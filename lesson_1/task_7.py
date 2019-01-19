# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным
# или равносторонним.

length_1 = float(input('Введите длину первого отрезка ( > 0 ): '))
length_2 = float(input('Введите длину второго отрезка ( > 0 ): '))
length_3 = float(input('Введите длину третьего отрезка ( > 0 ): '))

is_triangle = False
is_versatile = False    # разносторонний
is_isosceles = False    # равнобедренный
is_equilateral = False  # равносторонний

if (length_1 < length_2) and (length_1 < length_3):
    min_length = length_1
    if length_2 < length_3:
        mid_length = length_2
        max_length = length_3
    else:
        mid_length = length_3
        max_length = length_2
elif (length_1 > length_2) and (length_1 > length_3):
    max_length = length_1
    if length_2 < length_3:
        min_length = length_2
        mid_length = length_3
    else:
        min_length = length_3
        mid_length = length_2
else:
    mid_length = length_1
    if length_2 < length_3:
        min_length = length_3
        max_length = length_2
    else:
        min_length = length_2
        max_length = length_3

if mid_length > max_length - min_length:
    is_triangle = True
    if length_1 != length_2 and length_2 != length_3 and length_3 != length_1:
        is_versatile = True  # разносторонний
    elif length_1 == length_2 and length_2 == length_3 and length_3 == length_1:
        is_equilateral = True  # равносторонний
    else:
        is_isosceles = True  # равнобедренный
    print(f'Возможность существования треугольника - {is_triangle}')
    print(f'Треугольник разносторонний? - {is_versatile}')
    print(f'Треугольник равносторонний? - {is_equilateral}')
    print(f'Треугольник равнобедренный? - {is_isosceles}')
else:
    print(f'Возможность существования треугольника = {is_triangle}')
