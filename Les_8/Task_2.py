"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
   которые необходимо обойти.
"""

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

g_2 = [
    [0, 6, 2, 0],
    [0, 0, 0, 1],
    [0, 3, 0, 5],
    [0, 0, 0, 0]
]


def dijkstra(graph, start):
    graph_length = len(graph)
    costs = [float("inf") for _ in range(graph_length)]
    is_visited = [False] * graph_length
    costs[start] = 0
    min_cost = 0
    parents = []
    while min_cost < float("inf"):
        is_visited[start] = True
        parents.append(start)
        # 1) Найти узел с наименьшей стоимостью
        for i, neighbor_cost in enumerate(graph[start]):
            if is_visited[i] or neighbor_cost == 0:
                continue
            new_cost = neighbor_cost + costs[start]
            if costs[i] > new_cost:
                costs[i] = new_cost

        min_cost = float('inf')
        for i, cost in enumerate(costs):
            if min_cost > cost and not is_visited[i]:
                min_cost = cost
                start = i

    return costs, parents


print(dijkstra(g, 0))
