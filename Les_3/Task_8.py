"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
   Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
   В конце следует вывести полученную матрицу.
"""


def print_matrix(matrix):
    print("**************************")
    for line in matrix:
        for item in line:
            print(f"{item:>4}", end="")
        print()


def sum_lines(matrix):
    last_line_index = len(matrix) - 1
    for line in matrix[:last_line_index]:
        for i, number in enumerate(line):
            matrix[last_line_index][i] = matrix[last_line_index][i] + number

    return matrix


def generate_matrix(m, n):
    M = [[0 for _ in range(n)] for _ in range(m)]
    for i, line in enumerate(M[:n]):
        for j in range(len(line)):
            number = int(input(f"Введите M[{i}][{j}]: "))
            M[i][j] = number
    return M


matrix = generate_matrix(5, 4)
sum_lines(matrix)
print_matrix(matrix)
