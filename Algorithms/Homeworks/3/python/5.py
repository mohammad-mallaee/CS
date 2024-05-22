from collections import deque
import math


def bfs_path(graph, source, destination):
    queue = deque([source])
    predecessors = {source: None}
    visited = set([source])

    while queue:
        node = queue.popleft()
        if node == destination:
            path = []
            while node is not None:
                path.append(node)
                node = predecessors[node]
            path.reverse()
            return path
        for neighbor in graph[node]["n"]:
            capacity, flow = graph[node]["n"][neighbor]
            if neighbor not in visited and flow < capacity:
                visited.add(neighbor)
                predecessors[neighbor] = node
                queue.append(neighbor)

    return None


def ford_fulkerson(graph, source, destination):
    while (path := bfs_path(graph, source, destination)) is not None:
        path_flow = math.inf
        for i in range(0, len(path) - 1):
            capacity, flow = graph[path[i]]["n"][path[i + 1]]
            path_flow = min(path_flow, capacity - flow)
        for i in range(0, len(path) - 1):
            u, v = path[i], path[i + 1]
            capacity, flow = graph[u]["n"][v]
            graph[u]["n"][v] = (capacity, flow + path_flow)
            capacity, flow = graph[v]["n"].get(u, (0, 0))
            graph[v]["n"][u] = (capacity, flow - path_flow)
    for node in graph.keys():
        for key, value in list(graph[node]["n"].items()):
            if value[1] < 0:
                del graph[node]["n"][key]


def transform_graph(graph):
    i = 0
    new_graph = {}
    for node in graph:
        i -= 1
        in_node = {"n": {i: graph[node]["f"]}, "out": i, "in": True}
        out_node = {"n": graph[node]["n"]}
        new_graph[node] = in_node
        new_graph[i] = out_node
    return new_graph, i


def revert_graph_transform(graph):
    og_graph = {}
    for node in graph:
        if graph[node].get("in", False):
            out_node = graph[node]["out"]
            og_graph[node] = {
                "n": graph[out_node]["n"],
                "f": graph[node]["n"][out_node],
            }
    return og_graph


g = {
    1: {"n": {2: (2, 0), 4: (3, 0)}, "f": (4, 0)},
    2: {"n": {3: (5, 0), 5: (3, 0)}, "f": (5, 0)},
    3: {"n": {6: (2, 0)}, "f": (1, 0)},
    4: {"n": {3: (1, 0)}, "f": (3, 0)},
    5: {"n": {6: (4, 0)}, "f": (2, 0)},
    6: {"n": {}, "f": (7, 0)},
}

new_g, last_node = transform_graph(g)
ford_fulkerson(new_g, 1, last_node)
graph = revert_graph_transform(new_g)
for key in graph:
    print(key, graph[key])
