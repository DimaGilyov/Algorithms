"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
   Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

import random

random_array = [random.randint(1, 9) for _ in range(10)]
print(f"random_array={random_array}")

min_1 = min_2 = random_array[0]
for number in random_array[1:]:
    if number < min_1:
        min_2 = min_1
        min_1 = number
    elif number < min_2:
        min_2 = number

print(f"min_1={min_1}, min_2={min_2}")
