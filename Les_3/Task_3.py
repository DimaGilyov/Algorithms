"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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

random_array[min["index"]], random_array[max["index"]] = random_array[max["index"]], random_array[min["index"]]
print(random_array)