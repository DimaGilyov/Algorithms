"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random

random_array = [random.randint(3, 9) for _ in range(10)]
print(random_array)

numbers = {}
for number in random_array:
    if number in numbers:
        numbers[number] = numbers[number] + 1
    else:
        numbers[number] = 1

for number, count in numbers.items():
    print(f"{number} - {count}")