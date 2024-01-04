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

# 전체 그래프에서 특정 엣지들의 상위, 하위 노드 개수 출력
target_edges = [
    ('0x55f087019250', '0x55f08701ce90'),
    ('0x55f0870191e0', '0x55f08701ce90'),
    ('0x55f08701ce90', '0x55f0868e8738'),
]

all_ancestors_count = 0
all_descendants_count = 0

for source, target in graph.edges:
    if any(node in edge for edge in target_edges for node in (source, target)):
        ancestors_count = count_ancestors(graph, source)
        descendants_count = count_descendants(graph, target)
        all_ancestors_count += ancestors_count
        all_descendants_count += descendants_count

print(f"All Ancestors Count = {all_ancestors_count}")
print(f"All Descendants Count = {all_descendants_count}")

