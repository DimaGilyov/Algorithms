"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.

Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии сортировки,
   например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random
import copy


def bubble_sort(array):
    new_array = copy.deepcopy(array)
    for i in range(1, len(new_array)):
        for j in range(len(new_array) - i):
            if new_array[j] < new_array[j + 1]:
                new_array[j], new_array[j + 1] = new_array[j + 1], new_array[j]
    return new_array


random_array = [random.randint(-100, 100) for _ in range(10)]
print(random_array)
sorted_array = bubble_sort(random_array)
print(sorted_array)
