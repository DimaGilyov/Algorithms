"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
   по алгоритму поиска в глубину (Depth-First Search).

   Примечания:
   a. граф должен храниться в виде списка смежности;
   b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

from collections import deque


def generate_graph(num):
    new_graph = {}
    for i in range(num):
        new_graph[i] = tuple(j for j in range(num) if j != i)

    return new_graph


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
