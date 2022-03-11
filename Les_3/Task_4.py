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

max_count = 0
value = 0
for number, count in numbers.items():
    print(f"{number} - {count}")
    if count > max_count:
        max_count = count
        value = number

print(f"Число {value}, встречается {max_count} раз")
