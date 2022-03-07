"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
   Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

numbers_count = int(input("Введите количество вводимых числел: "))
number = int(input("Введите цифру: "))
count = 0
for _ in range(numbers_count):
    input_number = int(input("Введите число: "))
    while input_number > 0:
        n = input_number % 10
        if number == n:
            count += 1
        input_number //= 10

print(f"Количетво цифр {count}")