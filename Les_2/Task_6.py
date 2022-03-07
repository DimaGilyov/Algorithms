"""
6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
  После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
  Если за 10 попыток число не отгадано, вывести ответ.
"""

import random
random_number = random.randint(0, 100)
attempts_count = 0
while attempts_count < 10:
    attempts_count += 1
    input_number = int(input("Введите число: "))
    if random_number == input_number:
        print(f"Ура вы отгадали число {random_number}")
        break
    elif random_number > input_number:
        print(f"Загаданное число больше чем {input_number}")
    else:
        print(f"Загаданное число меньше чем {input_number}")
else:
    print(f"Вы не отгадали число {random_number}")

