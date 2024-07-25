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

# Візуалізація графа
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
plt.title("Randomly Generated Graph")
plt.show()

# Аналіз характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print("Node degrees:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

# Візуалізація графа
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
plt.title("Randomly Generated Graph")
plt.savefig('random_graph.png')
