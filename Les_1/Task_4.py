"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

a = input("Введите начальную букву: ")
b = input("Введите конечную букву: ")

position_1 = ord(a)
position_2 = ord(b)

# Найдем позицию в алфавите
if 97 <= position_1 <= 122:
    position_1 = position_1 - 96
if 97 <= position_2 <= 122:
    position_2 = position_2 - 96

between_chars_count = position_2 - position_1 - 1
print(f"position_1={position_1}, position_2={position_2}, between_chars_count={between_chars_count}")