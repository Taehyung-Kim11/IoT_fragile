import networkx as nx

def count_ancestors(graph, node):
    return len(nx.ancestors(graph, node))

def count_descendants(graph, node):
    return len(nx.descendants(graph, node))

# 그래프 생성
graph = nx.DiGraph()

# Sofia1.txt에서 엣지 정보 읽어오기
with open("Sofia1.txt", "r") as f:
    for line in f:
        parent, child = line.strip().split(",")
        graph.add_edge(parent.strip(), child.strip())

# 특정 엣지들의 상위, 하위 엣지 개수 출력
target_edges = [
    ('0x55f087019250', '0x55f08701ce90'),
    ('0x55f0870191e0', '0x55f08701ce90'),
    ('0x55f08701ce90', '0x55f0868e8738'),
]

for edge in target_edges:
    parent, child = edge
    ancestors_count = count_ancestors(graph, parent)
    descendants_count = count_descendants(graph, child)
    print(f"Edge {edge}: Ancestors Count = {ancestors_count}, Descendants Count = {descendants_count}")

