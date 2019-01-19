# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letter_1 = str(input('Введите первую букву алфавита (от "a" до "z"): '))
letter_2 = str(input('Введите вторую букву алфавита (от "a" до "z"): '))

if ord(letter_1) > ord(letter_2):
    letter_1, letter_2 = letter_2, letter_1

pos_letter_1 = ord(letter_1) - ord('a') + 1
pos_letter_2 = ord(letter_2) - ord('a') + 1
count_letters_between = pos_letter_2 - pos_letter_1 - 1

print(f'Место буквы "{letter_1}" в алфавите: {pos_letter_1}')
print(f'Место буквы "{letter_2}" в алфавите: {pos_letter_2}')
print(f'Букв между ними: {count_letters_between}')
