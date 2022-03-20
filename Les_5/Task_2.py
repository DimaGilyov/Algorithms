"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
   Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
   произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque
from collections import defaultdict

hex_table = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def hex_add(hex_number_1, hex_number_2):
    hex_number_1, hex_number_2 = align_numbers(hex_number_1, hex_number_2)

    d_1 = hex_to_dec(hex_number_1)
    d_2 = hex_to_dec(hex_number_2)
    d_1.reverse()
    d_2.reverse()

    isTransfer = False
    response = deque()
    for n_1, n_2 in zip(d_1, d_2):
        s = n_1 + n_2
        if isTransfer:
            isTransfer = False
            s += 1

        if s >= 16:
            isTransfer = True
            s -= 16
            response.appendleft(dec_to_hex(s))
        else:
            response.appendleft(dec_to_hex(s))

    return list(response)


def hex_multiply(hex_number_1, hex_number_2):
    hex_number_1, hex_number_2 = align_numbers(hex_number_1, hex_number_2)

    d_1 = hex_to_dec(hex_number_1)
    d_2 = hex_to_dec(hex_number_2)
    d_1.reverse()
    d_2.reverse()

    count = 0
    numbers = defaultdict(deque)
    for i, n_1 in enumerate(d_2):
        for n_2 in d_1:
            s = n_1 * n_2
            if count:
                s += count

            count = s // 16
            if count:
                s -= count * 16
                numbers[i].appendleft(dec_to_hex(s))
            else:
                numbers[i].appendleft(dec_to_hex(s))
        if count:
            numbers[i].appendleft(dec_to_hex(count))
        for k in range(i):
            numbers[i].append(dec_to_hex(0))

    last_sum = []
    for i in range(1, len(numbers)):
        if not last_sum:
            last_sum = numbers[i - 1]
        current_number = numbers[i]
        last_sum = hex_add(last_sum, current_number)

    return last_sum


def hex_to_dec(hex_number):
    dec_number = deque()
    for e in hex_number:
        try:
            dec_number.append(int(e))
        except:
            dec_number.append(hex_table[e])

    return dec_number


def dec_to_hex(dec_number):
    if dec_number < 10:
        return str(dec_number)
    else:
        for k, v in hex_table.items():
            if dec_number == v:
                return k

    return None


def align_numbers(hex_number_1, hex_number_2):
    """
    Возвращаем hex_number_1 и hex_number_2 одинаковый длины
    """
    hex_number_1 = deque(hex_number_1)
    hex_number_2 = deque(hex_number_2)
    max_len = len(hex_number_1) if len(hex_number_1) > len(hex_number_2) else len(hex_number_2)
    if len(hex_number_1) < max_len:
        for _ in range(max_len - len(hex_number_1)):
            hex_number_1.appendleft("0")
    else:
        for _ in range(max_len - len(hex_number_2)):
            hex_number_2.appendleft("0")
    return hex_number_1, hex_number_2


number_1 = list(input("Введиче число (HEX) №1: ").upper())
number_2 = list(input("Введиче число (HEX) №2: ").upper())

s = hex_add(number_1, number_2)
print("Сумма: ", s)
m = hex_multiply(number_1, number_2)
print("Произведение: ", m)
