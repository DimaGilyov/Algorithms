"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
   Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья
   прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple


def average(numbers: list):
    return sum(numbers) / len(numbers)


companies_count = int(input("Введите количество предприятий: "))
companies = []
for i in range(1, companies_count + 1):
    Company = namedtuple("Company", "name, profits, average_profit")
    name = input(f"Введите имя предприятия №{i}: ")
    company_profits = []
    for j in range(1, 5):
        profit = float(input(f"Введите прибыль предприятия {name} за {j}-й квартал: "))
        company_profits.append(profit)
    companies.append(Company(name, company_profits, average(company_profits)))

print("\n\n")
all_profits = []
for company in companies:
    all_profits.extend(company.profits)
all_companies_average_profit = average(all_profits)
print(f"Средряя прибыль всех компаний: {all_companies_average_profit}")

for company in companies:
    if company.average_profit > all_companies_average_profit:
        print(f"Компания {company.name} имеет прибыль выше среднего ({company.average_profit})")
    elif company.average_profit < all_companies_average_profit:
        print(f"Компания {company.name} имеет прибыль ниже среднего ({company.average_profit})")
    else:
        print(f"Компания {company.name} имеет среднюю прибыль ({company.average_profit})")
