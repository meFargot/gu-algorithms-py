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


def get_avg_profit(companies):
    """ Определяет среднюю прибыль за год по всем компаниям из списка companies
    """
    all_profit = 0
    for company in companies:
        all_profit += sum(company.profit)
    return all_profit / len(companies)


def show_companies_by_profit(companies, avg_profit):
    """ Выводит предприятия из companies с прибылью выше и ниже среднего avg_profit
    """
    above = []
    below = []
    for company in companies:
        if sum(company.profit) > avg_profit:
            above.append(company)
        else:  # Если прибыль компании равна средней считаем, что ее прибыль ниже средней
            below.append(company)

    print(f'Предприятия с прибылью выше среднего:')
    for company in above:
        print(company.name, sep='\n')

    print(f'Предприятия с прибылью ниже среднего:')
    for company in below:
        print(company.name, sep='\n')
    return 0


# Ввод данных
companies_data = input_data()
print('\n', '*' * 50, '\n')

# Определить среднюю прибыль за год для всех предприятий
avg_year_profit = get_avg_profit(companies_data)
print(f'Средняя прибыль компаний за год = {avg_year_profit}\n')
# Вывести предприятия с прибылью выше среднего и ниже среднего
show_companies_by_profit(companies_data, avg_year_profit)
