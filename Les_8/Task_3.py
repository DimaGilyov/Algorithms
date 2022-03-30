"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
   по алгоритму поиска в глубину (Depth-First Search).

   Примечания:
   a. граф должен храниться в виде списка смежности;
   b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

import random


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


def depth_first_search(graph, start, finish, visited):
    visited.append(start)

    if start == finish:
        return visited

    for neighbor in graph[start]:
        if neighbor not in visited:
            if depth_first_search(graph, neighbor, finish, visited):
                return visited

    return []


n = int(input("Количество вершин в графе: "))
graph = generate_graph(n)
for i, v in enumerate(graph):
    print(f"{i}) {v}")

start = int(input("Введите вершину начала: "))
finish = int(input("Введите вершину конца: "))
way = depth_first_search(graph, start, finish, [])
print(f"way: {way}")
