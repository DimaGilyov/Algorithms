"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
   Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

random_array = [random.randint(0, 100) for _ in range(10)]
print(random_array)

min = {"index": 0, "value": random_array[0]}
max = {"index": 0, "value": 0}
for index, value in enumerate(random_array):
    min_value = min["value"]
    if min_value > value:
        min["index"] = index
        min["value"] = value

    max_value = max["value"]
    if max_value < value:
        max["index"] = index
        max["value"] = value

print(f"min={min}")
print(f"max={max}")

start_index = min["index"]
end_index = max["index"]
if start_index > end_index:
    start_index, end_index = end_index, start_index

array = random_array[start_index + 1: end_index]
print(f"array={array}, sum={sum(array)}")