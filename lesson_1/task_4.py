# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо
# получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ
# алфавита от 'a' до 'f' включительно.

import random

int_start = int(input('Введите нижнюю границу для случайного целого числа: '))
int_stop = int(input('Введите верхнюю границу для случайного целого числа: '))
float_start = int(input('Введите нижнюю границу для случайного вещественного числа: '))
float_stop = int(input('Введите верхнюю границу для случайного вещественного числа: '))
chr_start = str(input('Введите начальный символ для случайного символа (от "a" до "z"): '))
chr_stop = str(input('Введите конечный символ для случайного символа (от "a" до "z"): '))

random_int = random.randint(int_start, int_stop)

random_float = random.uniform(float_start, float_stop)

chr_start_code = ord(chr_start)
chr_stop_code = ord(chr_stop)
random_chr_code = random.randint(chr_start_code, chr_stop_code)
random_chr = chr(random_chr_code)

print(f'Случайное целое число: {random_int}')
print(f'Случайное вещественное число: {random_float}')
print(f'Случайный символ: {random_chr}')
