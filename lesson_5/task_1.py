# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.

from collections import namedtuple


def input_data():
    """ Запрашивает данные о предприятиях у пользователя и возвращает список из Namedtuple
    """
    number_company = int(input('Введите количество предприятий для анализа (целое положительное число): '))
    assert number_company > 0, 'Число предприятий должно быть больше нуля'

    companies = []
    Company = namedtuple('Company', 'name, profit', defaults=['Имя предприятия', [0, 0, 0, 0]])

    for i in range(1, number_company + 1):
        tmp_name = input(f'Введите название {i} компании: ')
        tmp_profit = [0, 0, 0, 0]
        for q in range(4):
            tmp_profit[q] = int(input(f'Введите прибыль компании {tmp_name} '
                                      f'за {q+1} квартал: '))
        current_company = Company(tmp_name, tmp_profit)
        companies.append(current_company)
    return companies


# Ввод данных
# Список из namedtuple
print(input_data())
# Определить среднюю прибыль за год для всех предприятий


# Вывести предприятия с прибылью выше среднего и ниже среднего

