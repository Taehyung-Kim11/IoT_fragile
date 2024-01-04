graph = []

with open("Sofia1.txt", "r") as f:
    for line in f:
        addresses = line.strip().split(",")
        if len(addresses) == 2:
            parent, child = addresses
            graph.append((parent, child))

filtered_graph = [(parent, child) for parent, child in graph
                  if not any('0x55f08701ce90' in x for x in (parent, child))]

with open("Sofia2.txt", "w") as output_file:
    for edge in filtered_graph:
        output_file.write(f"{edge[0]}, {edge[1]}\n")

