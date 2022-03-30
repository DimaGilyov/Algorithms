"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
   Примечание. Решите задачу при помощи построения графа.
"""

friends_count = int(input("Введите количество друзей: "))
friends_handshake = []
for i in range(friends_count):
    friends_handshake.append([1 if i != friend_index else 0 for friend_index in range(friends_count)])

print(*friends_handshake, sep="\n")

handshakes_count = sum([sum(handshakes) for handshakes in friends_handshake]) // 2
print(f"\nУ {friends_count} человек было {handshakes_count} рукопожатий")
