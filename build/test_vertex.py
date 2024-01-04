graph = set()  # 중복된 엣지를 허용하지 않는 집합으로 정의

with open("Sofia1.txt", "r") as f:
    for line in f:
        # 각 줄에서 정점들을 추출
        vertices = line.strip().split(",")
        
        # 각 정점을 그래프에 추가
        graph.update(vertices)

# 정점의 개수 출력
print("정점의 개수:", len(graph))

