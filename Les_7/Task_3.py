"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
   Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
   Примечание:
   Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки,
   который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
import random


def median(array, half):
    if len(array) == 1:
        return array[0]

    pivot = array[random.randint(0, len(array) - 1)]
    left_elements = []
    middle_elements = []
    right_elements = []

    for e in array:
        if e < pivot:
            left_elements.append(e)
        elif e == pivot:
            middle_elements.append(e)
        else:
            right_elements.append(e)

    if half < len(left_elements):
        return median(left_elements, half)
    elif half < len(left_elements) + len(middle_elements):
        return middle_elements[0]
    else:
        return median(right_elements, half - len(left_elements) - len(middle_elements))


n = 5
random_array = [random.randint(-100, 100) for _ in range(2 * n + 1)]
print(random_array)
m = median(random_array, n)
print(f'Медиана {m}')

left_array = []
medians = []
right_array = []
for e in random_array:
    if e < m:
        left_array.append(e)
    elif e > m:
        right_array.append(e)
    else:
        medians.append(e)
print(left_array, medians, right_array)
