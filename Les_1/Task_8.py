"""
8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

a = int(input("Введиче число a: "))
b = int(input("Введиче число b: "))
c = int(input("Введиче число c: "))

max_number = a
if b > a and b > c:
    max_number = b
elif c > a and c > b:
    max_number = c

min_number = a
if b < a and b < c:
    min_number = b
elif c < a and c < b:
    min_number = c

average_number = a
if min_number < b < max_number:
    average_number = b
elif min_number < c < max_number:
    average_number = c

print(f"Среднее число: {average_number}")