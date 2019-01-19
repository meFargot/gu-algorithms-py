# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые
# данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
# снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в
# качестве делителя.

while True:
    print(f'Введите два числа и оператор')
    num_1 = float(input(f'1-ое число: '))
    num_2 = float(input(f'2-ое число: '))
    operator = input(f'Оператор (+, -, *, /) или ноль для завершения работы: ')

    if operator != '0':
        if operator == '+':
            result = num_1 + num_2
            print(f'{num_1} {operator} {num_2} = {result}\n')
            continue
        if operator == '-':
            result = num_1 - num_2
            print(f'{num_1} {operator} {num_2} = {result}\n')
            continue
        if operator == '*':
            result = num_1 * num_2
            print(f'{num_1} {operator} {num_2} = {result}\n')
            continue
        if operator == '/':
            if num_2 != 0:
                result = num_1 / num_2
                print(f'{num_1} {operator} {num_2} = {result}\n')
                continue
            else:
                print(f'На ноль делить нельзя!\n')
                continue
        else:
            print(f'Неверный оператор\n')
            continue
    else:  # operator == '0'
        print(f'Завершаю работу\n')
        break
