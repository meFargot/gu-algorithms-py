# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_number = int(input('Введите номер буквы в алфавите (от 1 до 26): '))

letter_code = ord('a') - 1 + letter_number

letter = chr(letter_code)

print(f'Это буква "{letter}"')
