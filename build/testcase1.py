graph = []

with open("Sofia_test.txt", "r") as f:
    for line in f:
        cleaned_line = ''.join(c for c in line if c not in ['<', '>'])
        addresses = cleaned_line.strip().split(",")
        if len(addresses) == 2:
            parent, child = addresses
            graph.append((parent, child))


with open("Sofia1.txt", "w") as output_file:
    for edge in graph:
        output_file.write(f"{edge[0]}, {edge[1]}\n")

