"""
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

number = int(input("Введите номер буквы буквы: "))
char = chr(number + 64)
print(f"Номер буквы: {number}, буква:{char}")