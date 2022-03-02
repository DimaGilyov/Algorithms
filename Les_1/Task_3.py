"""
3. Написать программу, которая генерирует в указанных пользователем границах:
   a. случайное целое число,
   b. случайное вещественное число,
   c. случайный символ.

   Для каждого из трех случаев пользователь задает свои границы диапазона.
   Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
   Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random

start_number_integer = int(input("Введите начальное целое число: "))
end_number_integer = int(input("Введите конечное целое число: "))

start_number_float = float(input("Введите начальное вещественное число: "))
end_number_float = float(input("Введите конечное вещественное число: "))

start_char = input("Введите начальный символ: ")
end_char = input("Введите конечный символ: ")

random_integer_number = random.randint(start_number_integer, end_number_integer)
random_float_number = random.uniform(start_number_float, end_number_float)
random_char = chr(random.randint(ord(start_char), ord(end_char)))
print(f"Случайное целое число = {random_integer_number}")
print(f"Случайное вещественное число = {random_float_number}")
print(f"Случайный символ = {random_char}")
