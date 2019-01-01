from collections import defaultdict


class Graph:
    def __init__(self, nodes, edges, distances):
        self.nodes = nodes
        self.edges = edges
        self.distances = distances


def dijsktra(graph, initial):
    uncovered = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
          if node in uncovered:
            if min_node is None:
              min_node = node
            elif uncovered[node] < uncovered[min_node]:
              min_node = node

        if min_node is None:
          break

        nodes.remove(min_node)
        current_weight = uncovered[min_node]
        if min_node not in graph.edges:
            continue
        for nd in graph.edges[min_node]:
          weight = current_weight + graph.distances[(min_node, nd)]
          if nd not in uncovered or weight < uncovered[nd]:
            uncovered[nd] = weight
            path[nd] = min_node

    return uncovered, path


with open("in.txt", "r", encoding="utf-8") as f:
    nodes_amount = int(f.read(1))
    nodes = list(i for i in range(1, nodes_amount + 1))
    edges = defaultdict()
    distances = {}
    f.read(1)
    for i in range(1, nodes_amount + 1):
        node = f.read(1)
        while node != "0":
            if int(node) not in edges:
                edges[int(node)] = []
            edges[int(node)].append(i)
            f.read(1)
            dist = ""
            possible_dist = f.read(1)
            byte = possible_dist
            while byte != " ":
                dist += byte
                byte = f.read(1)
            if dist == "":
                dist = possible_dist
            distances[(int(node), i)] = int(dist)
            node = f.read(1)
        f.read(1)
    origin = int(f.read(1))
    f.read(1)
    target = int(f.read(1))

g = Graph(nodes, edges, distances)
visited, path = dijsktra(g, origin)
print(visited, path)

nodes_path = ""
from_end_to_start_node = target
reversed_path = []
try:
    while from_end_to_start_node != origin:
        from_end_to_start_node = path[from_end_to_start_node]
        reversed_path.append(from_end_to_start_node)
except Exception:
    with open("out.txt", "w", encoding="utf-8") as f:
        f.write("N")
        exit(0)

not_reversed_path = reversed(reversed_path)
for i in not_reversed_path:
    nodes_path += str(i) + " "
nodes_path += str(target)

with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Y\n" + nodes_path + "\n" + str(visited[target]))



