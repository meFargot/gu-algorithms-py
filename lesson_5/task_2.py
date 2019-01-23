# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


HEX = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def add_numbers(a, b):
    """ Складывает два шестнадцатеричных числа в виде массивов. Возвращает массив по условию ДЗ
    """
    mem = 0  # "в уме" при сложении столбиком
    sum_ = deque()
    if len(a) < len(b):
        a, b = b, a
    for _ in range(len(a) - len(b)):  # дополняем нулями короткое число
        b.appendleft('0')
    for _ in range(len(a)):
        cur_sum_num = HEX.index(a.pop()) + HEX.index(b.pop()) + mem
        to_sum = cur_sum_num % 16
        mem = cur_sum_num // 16
        sum_.appendleft(HEX[to_sum])
    if mem > 0:
        sum_.appendleft(HEX[mem])
    return sum_



def mult_numbers(a, b):
    """ Умножает два шестнадцатеричных числа в виде массивов. Возвращает массив по условию ДЗ
    """
    pass


hex_num_a = deque(input('Введите первое шестнадцатеричное число: '))
hex_num_b = deque(input('Введите второе шестнадцатеричное число: '))

print(f'Первое число в виде массива: {hex_num_a}\nВторое число в виде массива: {hex_num_b}')

sum_a_b = add_numbers(hex_num_a, hex_num_b)
print(f'Сумма чисел A и B = {list(sum_a_b)}')

mult_a_b = mult_numbers(hex_num_a, hex_num_b)
print(f'Произведение чисел A и B = {sum_a_b}')
