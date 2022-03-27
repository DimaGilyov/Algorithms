"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
   Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        n = len(array) // 2
        left_array = merge_sort(array[:n])
        right_array = merge_sort(array[n:])
        return merge(left_array, right_array)


def merge(left_array, right_array):
    result = []
    i, j = 0, 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1
            
    if i < len(left_array):
        result.extend(left_array[i:])
    if j < len(right_array):
        result.extend(right_array[j:])
    return result


random_array = [round(random.uniform(0, 50), 2) for _ in range(10)]
print(random_array)
sorted_array = merge_sort(random_array)
print(sorted_array)
