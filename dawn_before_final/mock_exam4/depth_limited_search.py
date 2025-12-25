node_number, line_number, depth_limit = map(int, input().split())
graph = {}
for _ in range(line_number):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    graph[u].append(v)
    if v not in graph:
        graph[v] = []
    graph[v].append(u)
start_node = int(input())
def depth_limited_search(graph, start, depth_limit) -> list:
    path_list = []
    visited = set()
    def dls(node, depth):
        if depth > depth_limit:
            return
        visited.add(node)
        path_list.append(node)
        if node in graph:
            for neighbor in sorted(graph[node]):
                if neighbor not in visited:
                    dls(neighbor, depth + 1)
    dls(start, 0)
    return path_list
print(' '.join(map(str, depth_limited_search(graph, start_node, depth_limit))))

'''6 8 3
1 0
0 2
1 2
0 4
2 3
4 3
4 5
3 5
1'''