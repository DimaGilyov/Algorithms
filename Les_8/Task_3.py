"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
   по алгоритму поиска в глубину (Depth-First Search).

   Примечания:
   a. граф должен храниться в виде списка смежности;
   b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

import random
from collections import deque


def generate_graph(vertexes_count):
    graph = [[]] * vertexes_count
    v_list = [i for i in range(vertexes_count)]

    for i in range(vertexes_count):
        count = 0
        while count == 0:
            presence = [random.randint(0, 1) for i in range(vertexes_count - 1)]
            random.shuffle(presence)
            new_list = v_list.copy()
            new_list.remove(i)
            for index, element in enumerate(new_list):
                if presence[index] == 1:
                    graph[i] = graph[i] + [element]
                    count += 1
    return graph


def depth_first_search(graph, start, finish):
    length = len(graph)
    parent = [None] * length
    is_visited = [False] * length

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:
        current = deq.pop()

        if current == finish:
            break

        for vertex in graph[current]:
            if not is_visited[vertex]:
                is_visited[vertex] = True
                parent[vertex] = current
                deq.appendleft(vertex)
    else:
        return f"Из вершины {start} невозможно попасть в вершину {finish}"

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return list(way)


n = int(input("Количество вершин в графе: "))
graph = generate_graph(n)
print(*graph, end="\n")

start = int(input("Введите вершину начала: "))
finish = int(input("Введите вершину конца: "))
way = depth_first_search(graph, start, finish)
print(f"way: {way}")
