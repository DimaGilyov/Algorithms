"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
   Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

import random


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot_index = random.randint(0, len(array) - 1)
    pivot = array[pivot_index]
    left_array = [number for index, number in enumerate(array) if index != pivot_index and number <= pivot]
    right_array = [number for index, number in enumerate(array) if index != pivot_index and number > pivot]
    return quick_sort(left_array) + [pivot] + quick_sort(right_array)


random_array = [random.randint(1, 9) for _ in range(10)]
print(f"random_array={random_array}")
sorted_array = quick_sort(random_array)
print(f"два наименьших элемента = {sorted_array[:2]}")
