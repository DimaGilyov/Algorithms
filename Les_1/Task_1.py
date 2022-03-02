"""
1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
   Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

n1 = 5
n2 = 6

bit_or = n1 | n2
bit_and = n1 & n2
bit_xor = n1 ^ n2

print(f"n1: {bin(n1)}")
print(f"n2: {bin(n2)}")
print(f"OR: {bin(bit_or)}")
print(f"AND: {bin(bit_and)}")
print(f"XOR: {bin(bit_xor)}")


print(f"5 << 2: {bin(n1 << 2)}")
print(f"5 >> 2: {bin(n1 >> 2)}")


