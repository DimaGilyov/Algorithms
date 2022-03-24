"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
   Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
   Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

-a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
-b. написать 3 варианта кода (один у вас уже есть);
 проанализировать 3 варианта и выбрать оптимальный;
-c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
    Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
-d. написать общий вывод: какой из трёх вариантов лучше и почему.
------------------------------------------------------------------------------------------------------------------------
"""

import random
import sys


def print_size(x, level=0):
    print('\t' * level, f"type={x.__class__}, value={x}, bytes={sys.getsizeof(x)}")
    if hasattr(x, "__iter__"):
        if hasattr(x, "items"):
            for item in x.items():
                print_size(item, level + 1)
        elif not isinstance(x, str):
            for e in x:
                print_size(e, level + 1)


# -----------------------------------------------------------------------------------------------------------------------
"""
Версия Python и платформа" 
3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] win32
"""
# -----------------------------------------------------------------------------------------------------------------------
"""
a. Выбрана задача Lesson_3/Task_3
Условия задачи.
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
# -----------------------------------------------------------------------------------------------------------------------
"""
b. 3 Версии кода
"""


def version_1(random_array):
    print(random_array)

    min_item = {"index": 0, "value": random_array[0]}
    max_item = {"index": 0, "value": 0}
    for index, value in enumerate(random_array):
        min_value = min_item["value"]
        if min_value > value:
            min_item["index"] = index
            min_item["value"] = value

        max_value = max_item["value"]
        if max_value < value:
            max_item["index"] = index
            max_item["value"] = value

    print(f"min_item={min_item}")
    print(f"max_item={max_item}")

    random_array[min_item["index"]], random_array[max_item["index"]] = random_array[max_item["index"]], random_array[
        min_item["index"]]
    print(random_array)
    print("*" * 50)
    print("Переменная random_array:")
    print_size(random_array)
    print("\nПеременная min_item:")
    print_size(min_item)
    print("\nПеременная max_item:")
    print_size(max_item)
    print("*" * 50)


def version_2(random_array):
    print(random_array)

    min_item = [0, random_array[0]]
    max_item = [0, 0]
    for index, value in enumerate(random_array):
        min_value = min_item[1]
        if min_value > value:
            min_item[0] = index
            min_item[1] = value

        max_value = max_item[1]
        if max_value < value:
            max_item[0] = index
            max_item[1] = value

    print(f"min_item={min_item}")
    print(f"max_item={max_item}")

    random_array[min_item[0]], random_array[max_item[0]] = random_array[max_item[0]], random_array[
        min_item[0]]
    print(random_array)
    print("*" * 50)
    print("Переменная random_array:")
    print_size(random_array)
    print("\nПеременная min_item:")
    print_size(min_item)
    print("\nПеременная max_item:")
    print_size(max_item)
    print("*" * 50)


def version_3(random_array):
    print(random_array)

    min_index = 0
    min_value = random_array[0]
    max_index = 0
    max_value = 0
    for index, value in enumerate(random_array):
        if min_value > value:
            min_index = index
            min_value = value

        if max_value < value:
            max_index = index
            max_value = value

    print(f"min_item={min_index}, {min_value}")
    print(f"max_item={max_index}, {max_value}")

    random_array[min_index], random_array[max_index] = random_array[max_index], random_array[
        min_index]
    print(random_array)
    print("*" * 50)
    print("Переменная random_array:")
    print_size(random_array)
    print("\nПеременная min_index:")
    print_size(min_index)
    print("\nПеременная min_value:")
    print_size(min_value)
    print("\nПеременная max_index:")
    print_size(max_index)
    print("\nПеременная max_value:")
    print_size(max_value)
    print("*" * 50)


# -----------------------------------------------------------------------------------------------------------------------\
"""
c. Результаты анализа
"""
random_array = [random.randint(0, 100) for _ in range(10)]
version_1(random_array)
"""
Версия 1)
Переменная random_array:
 type=<class 'list'>, value=[76, 18, 99, 6, 87, 27, 23, 35, 40, 10], bytes=184
	 type=<class 'int'>, value=76, bytes=28
	 type=<class 'int'>, value=18, bytes=28
	 type=<class 'int'>, value=99, bytes=28
	 type=<class 'int'>, value=6, bytes=28
	 type=<class 'int'>, value=87, bytes=28
	 type=<class 'int'>, value=27, bytes=28
	 type=<class 'int'>, value=23, bytes=28
	 type=<class 'int'>, value=35, bytes=28
	 type=<class 'int'>, value=40, bytes=28
	 type=<class 'int'>, value=10, bytes=28

Переменная min_item:
 type=<class 'dict'>, value={'index': 2, 'value': 6}, bytes=232
	 type=<class 'tuple'>, value=('index', 2), bytes=56
		 type=<class 'str'>, value=index, bytes=54
		 type=<class 'int'>, value=2, bytes=28
	 type=<class 'tuple'>, value=('value', 6), bytes=56
		 type=<class 'str'>, value=value, bytes=54
		 type=<class 'int'>, value=6, bytes=28

Переменная max_item:
 type=<class 'dict'>, value={'index': 3, 'value': 99}, bytes=232
	 type=<class 'tuple'>, value=('index', 3), bytes=56
		 type=<class 'str'>, value=index, bytes=54
		 type=<class 'int'>, value=3, bytes=28
	 type=<class 'tuple'>, value=('value', 99), bytes=56
		 type=<class 'str'>, value=value, bytes=54
		 type=<class 'int'>, value=99, bytes=28
"""
version_2(random_array)
"""
Версия 2)
Переменная random_array:
 type=<class 'list'>, value=[76, 18, 6, 99, 87, 27, 23, 35, 40, 10], bytes=184
	 type=<class 'int'>, value=76, bytes=28
	 type=<class 'int'>, value=18, bytes=28
	 type=<class 'int'>, value=6, bytes=28
	 type=<class 'int'>, value=99, bytes=28
	 type=<class 'int'>, value=87, bytes=28
	 type=<class 'int'>, value=27, bytes=28
	 type=<class 'int'>, value=23, bytes=28
	 type=<class 'int'>, value=35, bytes=28
	 type=<class 'int'>, value=40, bytes=28
	 type=<class 'int'>, value=10, bytes=28

Переменная min_item:
 type=<class 'list'>, value=[3, 6], bytes=72
	 type=<class 'int'>, value=3, bytes=28
	 type=<class 'int'>, value=6, bytes=28

Переменная max_item:
 type=<class 'list'>, value=[2, 99], bytes=72
	 type=<class 'int'>, value=2, bytes=28
	 type=<class 'int'>, value=99, bytes=28
"""

version_3(random_array)
"""
Версия 3)
Переменная random_array:
 type=<class 'list'>, value=[76, 18, 99, 6, 87, 27, 23, 35, 40, 10], bytes=184
	 type=<class 'int'>, value=76, bytes=28
	 type=<class 'int'>, value=18, bytes=28
	 type=<class 'int'>, value=99, bytes=28
	 type=<class 'int'>, value=6, bytes=28
	 type=<class 'int'>, value=87, bytes=28
	 type=<class 'int'>, value=27, bytes=28
	 type=<class 'int'>, value=23, bytes=28
	 type=<class 'int'>, value=35, bytes=28
	 type=<class 'int'>, value=40, bytes=28
	 type=<class 'int'>, value=10, bytes=28

Переменная min_index:
 type=<class 'int'>, value=2, bytes=28

Переменная min_value:
 type=<class 'int'>, value=6, bytes=28

Переменная max_index:
 type=<class 'int'>, value=3, bytes=28

Переменная max_value:
 type=<class 'int'>, value=99, bytes=28
"""
# -----------------------------------------------------------------------------------------------------------------------
"""
d. Общий вывод:
Наиболее эффективное использование памяти получилось у третьего варианта, 
т.к там для значений используются простые переменные, не выделяем доп.память для словаря или списка
"""

# -----------------------------------------------------------------------------------------------------------------------
