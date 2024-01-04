import networkx as nx
import matplotlib.pyplot as plt

def find_ancestors(graph, node, generations):
    ancestors = set()
    queue = [node]
    visited = set()

    for generation in range(generations):
        new_queue = []
        for current_node in queue:
            if current_node in graph:
                if current_node not in visited:
                    visited.add(current_node)
                    ancestors.add(current_node)
                    new_queue.extend(graph.predecessors(current_node))
        queue = new_queue

    return ancestors

def find_descendants(graph, node, generations):
    descendants = set()
    queue = [node]
    visited = set()

    for generation in range(generations):
        new_queue = []
        for current_node in queue:
            if current_node in graph:
                if current_node not in visited:
                    visited.add(current_node)
                    descendants.add(current_node)
                    new_queue.extend(graph.successors(current_node))
        queue = new_queue

    return descendants

# 그래프 생성
graph = nx.DiGraph()

with open("Sofia2.txt", "r") as f:
    for line in f:
        addresses = line.strip().split(",")
        if len(addresses) == 2:
            parent, child = addresses
            graph.add_edge(parent, child)

# 특정 노드들과 관련된 노드들 찾기
target_nodes = ['0x55f087019250', '0x55f0870191e0', '0x55f0868e8738']
related_nodes = set(target_nodes)
for node in target_nodes:
    print(f"Node {node} exists: {node in graph}")
    if node in graph:
        related_nodes.update(find_ancestors(graph, node, 4))
        related_nodes.update(find_descendants(graph, node, 4))

# 관련된 노드들을 서브그래프로 만들어서 시각화
subgraph = graph.subgraph(related_nodes)

# 그래프 시각화
pos = nx.spring_layout(subgraph)
nx.draw(subgraph, pos, with_labels=True, font_size=5, node_size=1000, font_color="white")
plt.savefig("Sofia2.png")

