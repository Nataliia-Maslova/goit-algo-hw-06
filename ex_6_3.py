import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq

random.seed(42)

# Створення графа
G = nx.Graph()

num_nodes = 10
prob_edge = 0.3

# Додавання вершин
nodes = [f"Node_{i}" for i in range(num_nodes)]
G.add_nodes_from(nodes)

# Додавання ребер з випадковими вагами
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if random.random() < prob_edge:
            weight = random.randint(1, 10)  # Випадкова вага від 1 до 10
            G.add_edge(nodes[i], nodes[j], weight=weight)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Якщо поточна відстань більше, ніж вже знайдена, пропустити
        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor, data in graph[current_vertex].items():
            weight = data.get('weight', 1)  # Витягнути вагу або використати 1 за замовчуванням
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths

# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "Node_5")
print(shortest_paths)

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
