import networkx as nx
import matplotlib.pyplot as plt
import random

random.seed(42)

# Створення графа
G = nx.Graph()

num_nodes = 10
prob_edge = 0.3

# Додавання вершин
nodes = [f"Node_{i}" for i in range(num_nodes)]
G.add_nodes_from(nodes)

# Додавання ребер 
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if random.random() < prob_edge:
            G.add_edge(nodes[i], nodes[j])

# DFS через рекурсію
def dfs(graph, start, visited=None, path=None, parent=None):
    if visited is None:
        visited = set()
        path = []

    # Відмічаємо вузол як відвіданий
    visited.add(start)
    print(f"DFS: visited {start}")
    if parent is not None:
        path.append((parent, start))

    # Перевірка всіх суміжних вузлів
    for next in graph[start]:
        if next not in visited:  # Перевіряємо, чи вузол вже відвіданий
            dfs(graph, next, visited, path, start)
    return path

# BFS через чергу
def bfs(graph, start):
    visited, queue = {start}, [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        print(f"BFS: visited {vertex}")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append((vertex, neighbour))
    return path

# Виконання DFS та BFS
dfs_path = dfs(G, "Node_5")
bfs_path = bfs(G, "Node_5")

print(f"DFS path: {dfs_path}")
print(f"BFS path: {bfs_path}")

# Візуалізація графа
nx.draw(G, with_labels=True)
plt.show()
