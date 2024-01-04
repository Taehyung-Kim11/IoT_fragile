graph1 = []
with open("Sofia2.txt", "r") as f:
    for line in f:
        # line을 출력하여 어떤 형식으로 데이터가 저장되어 있는지 확인
        parent, child = line.strip().split(",")
        graph1.append((parent.strip(), child.strip()))

graph2 = []
with open("Sofia1.txt", "r") as f:
    for line in f:
        # line을 출력하여 어떤 형식으로 데이터가 저장되어 있는지 확인
        parent, child = line.strip().split(",")
        graph2.append((parent.strip(), child.strip()))

def diff(graph1, graph2):
    difference = set(graph2) - set(graph1)
    print(f"Number of differing edges: {len(difference)}")

diff(graph1, graph2)
