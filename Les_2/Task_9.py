"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

numbers_count = int(input("Введите количество вводимых числел: "))
max_sum = 0
for _ in range(numbers_count):
    input_number = int(input("Введите число: "))
    sum = 0
    while input_number > 0:
        n = input_number % 10
        sum += n
        input_number //= 10
    if sum > max_sum:
        max_sum = sum

print(f"Максимальная сумма цифр {max_sum}")