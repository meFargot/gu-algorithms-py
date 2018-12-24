# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

CODE_FROM = 32
CODE_TO = 127

for cur_code in range(CODE_FROM, CODE_TO + 1):
    if (cur_code - CODE_FROM) % 10 == 0:
        print()
    print(f'{cur_code}-"{chr(cur_code)}"\t', end='')

print()
