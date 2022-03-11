"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
"""

import random

random_array = [random.randint(-100, -1) for _ in range(10)]
print(random_array)

min_element = {"index": 0, "value": random_array[0]}
for i, value in enumerate(random_array):
    min_value = min_element["value"]
    if min_value > value:
        min_element["index"] = i
        min_element["value"] = value

print(f"min_element={min_element}")