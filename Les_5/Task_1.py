"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
   Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья
   прибыль выше среднего и ниже среднего.
"""
import itertools
from collections import defaultdict


def average(numbers: list):
    return sum(numbers) / len(numbers)


companies_count = int(input("Введите количество предприятий: "))
companies = defaultdict(list)
for i in range(1, companies_count + 1):
    name = input(f"Введите имя предприятия №{i}: ")
    company_profits = []
    for j in range(1, 5):
        profit = float(input(f"Введите прибыль предприятия {name} за {j}-й квартал: "))
        companies[name].append(profit)

print("\n\n")
all_profits = list(itertools.chain(*companies.values()))
all_companies_average_profit = average(all_profits)
print(f"Средряя прибыль всех компаний: {all_companies_average_profit}")

report = defaultdict(list)
for name, profits in companies.items():
    average_profit = average(profits)
    if average_profit > all_companies_average_profit:
        report["Прибыль выше среднего"].append(name)
    elif average_profit < all_companies_average_profit:
        report["Прибыль ниже среднего"].append(name)

for k, v in report.items():
    print(k, v)
