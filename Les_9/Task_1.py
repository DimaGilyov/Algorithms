"""
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
   Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.
"""

import hashlib


# Не совсем понял задание, в голову приходят только кривые реализации что бы решение соответствовало
def get_substrings_count(string: str) -> int:
    substrings = []
    for i in range(0, len(string)):
        for j in range(i, len(string)):
            if i == 0 and j == len(string) - 1:
                continue

            substring = string[i: j + 1]
            hash = get_hash1(substring)
            if hash not in substrings:
                substrings.append(hash)
    return len(substrings)


def get_hash1(text: str):
    h_list = [None]


def get_hash1(text: str):
    return hashlib.sha1(text.encode("UTF-8")).hexdigest()


if __name__ == "__main__":
    text = "abcde"  # 15
    # text = "aaaaa"  # 5
    substrings_count = get_substrings_count(text)
    print(f"В строке '{text}' {substrings_count} подстрок(и).")
