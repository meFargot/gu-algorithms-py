# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Введите год в формате YYYY: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap = True
else:
    is_leap = False

print(f'Год {year} високосный - {is_leap}')
