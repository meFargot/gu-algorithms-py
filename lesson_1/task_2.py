# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака. Объяснить полученный результат.

num_five = 5
num_six = 6

result_and = num_five & num_six

result_or = num_five | num_six

result_xor = num_five ^ num_six

not_five = ~ num_five

not_six = ~ num_six

five_right_2 = num_five >> 2

five_left_2 = num_five << 2

print(f'Результат выполнения логических побитовых операций над числам {num_five} и {num_six}:')
print(f'Представление в двоичной системе счисления: 0b{num_five:b} и 0b{num_six:b}')
print(f'Операция "И" ( 0b{num_five:b} & 0b{num_six:b} ): 0b{result_and:b} = {result_and} ')
print(f'Операция "ИЛИ" ( 0b{num_five:b} | 0b{num_six:b} ): 0b{result_or:b} = {result_or}')
print(f'Операция "ИСКЛЮЧАЮЩЕЕ ИЛИ" ( 0b{num_five:b} ^ 0b{num_six:b} ): 0b{result_xor:b} = {result_xor}')
print(f'Операция "ОТРИЦАНИЕ" ( ~ 0b{num_five:b} ): 0b{not_five:b} = {not_five}')
print(f'Операция "ОТРИЦАНИЕ" ( ~ 0b{num_six:b} ): 0b{not_six:b} = {not_six}')
print(f'Операция "ПОБИТОВЫЙ СДВИГ ВПРАВО" ( 0b{num_five:b} >> 2 ): 0b{five_right_2:b} = {five_right_2}')
print(f'Операция "ПОБИТОВЫЙ СДВИГ ВЛЕВО" ( 0b{num_five:b} << 2 ): 0b{five_left_2:b} = {five_left_2}')

# Операция "И" ( 0b101 & 0b110 ): 0b100 = 4
# Здесь все просто, логическое И применяется к каждой паре битов по разрядам:
# 0b101
# 0b110
# -----
# 0b100 = 4

# Операция "ИЛИ" ( 0b101 | 0b110 ): 0b111 = 7
# Аналогично, только применяем логическое ИЛИ:
# 0b101
# 0b110
# -----
# 0b111 = 7

# Операция "ИСКЛЮЧАЮЩЕЕ ИЛИ" ( 0b101 ^ 0b110 ): 0b11 = 3
# Исключающее ИЛИ немного сложнее, но механизм тот же самый (применяем к каждой паре битов по разрядам):
# 0b101
# 0b110
# -----
# 0b011 = 3

# Операция "ОТРИЦАНИЕ" ( ~ 0b101 ): 0b-110 = -6
# Отрицание работает немного по другому из-за специфичного хранения отрицательных чисел в памяти.
# Сначала применяется логическое НЕ к каждому биту в числе:
# 0b0...0101
# -----
# 0b1...1010
# а затем прибавляется единица:
# 0b1...1010
# 0b0...0001
# -----
# 0b1...1011 - это -5 в дополнительном коде, но мы получили 0b-110, хм...
# Гугл подсказал, что побитовое НЕ (~) в питоне для числа x работает так: -(x+1), что в нашем случае как раз -6 для 5.

# Операция "ПОБИТОВЫЙ СДВИГ ВПРАВО" ( 0b101 >> 2 ): 0b1 = 1
# Побитовый сдвиг вправо сдвигает все биты числа на заданное количество позиций вправо, отбрасывая вышедшие за границы
# 1-го разряда цифры:
# 0b101
# сдвигаем на 1 позицию вправо
# 0b010 1 < эту 1 отбрасываем
# сдвигаем еще на 1 позицию вправо
# 0b001 0 < этот 0 отбрасываем
# Получили число 0b1 = 1

# Операция "ПОБИТОВЫЙ СДВИГ ВЛЕВО" ( 0b101 << 2 ): 0b10100 = 20
# Побитовый сдвиг влево сдвигает все биты числа на заданное количество позиций влево, заполняя младшие разряды нулями:
# 0b101
# сдвигаем на 1 позицию влево
# 0b1010
# сдвигаем еще на 1 позицию влево
# 0b10100
# Получили число 0b10100 = 20