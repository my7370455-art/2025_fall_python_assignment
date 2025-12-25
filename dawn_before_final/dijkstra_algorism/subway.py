import sys
import math

def get_dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        home_x = int(next(iterator))
        home_y = int(next(iterator))
        school_x = int(next(iterator))
        school_y = int(next(iterator))
    except StopIteration:
        return

    nodes = []
    nodes.append((home_x, home_y)) # Index 0: Home
    nodes.append((school_x, school_y)) # Index 1: School

    # Adjacency list for subway connections
    # We will handle walking connections implicitly as they exist between all pairs
    subway_adj = {} # Map u -> list of (v, time)

    while True:
        try:
            # Read a subway line
            line_stops = []
            while True:
                x = int(next(iterator))
                y = int(next(iterator))
                if x == -1 and y == -1:
                    break
                
                nodes.append((x, y))
                line_stops.append(len(nodes) - 1)
            
            # Add subway edges for this line
            for i in range(len(line_stops) - 1):
                u = line_stops[i]
                v = line_stops[i+1]
                d = get_dist(nodes[u], nodes[v])
                # Subway speed: 40 km/h = 40000 m / 60 min
                # Time = distance / speed = distance * 60 / 40000 = distance * 0.0015
                t = d * 0.0015
                
                if u not in subway_adj: subway_adj[u] = []
                if v not in subway_adj: subway_adj[v] = []
                
                subway_adj[u].append((v, t))
                subway_adj[v].append((u, t))
                
        except StopIteration:
            break

    num_nodes = len(nodes)
    
    # Dijkstra's Algorithm
    # Since the graph is dense (walking edges between all pairs), 
    # we use the O(V^2) implementation without a priority queue.
    
    dist = [float('inf')] * num_nodes
    dist[0] = 0
    visited = [False] * num_nodes
    
    # Walking speed: 10 km/h = 10000 m / 60 min
    # Time = distance * 60 / 10000 = distance * 0.006
    WALK_FACTOR = 0.006
    
    for _ in range(num_nodes):
        # Find unvisited node with smallest distance
        u = -1
        min_val = float('inf')
        for i in range(num_nodes):
            if not visited[i] and dist[i] < min_val:
                min_val = dist[i]
                u = i
        
        if u == -1 or dist[u] == float('inf'):
            break
            
        visited[u] = True
        
        if u == 1: # Reached School
            break
            
        # Relax edges
        
        # 1. Walking edges (to all other nodes)
        for v in range(num_nodes):
            if not visited[v]:
                d = get_dist(nodes[u], nodes[v])
                new_dist = dist[u] + d * WALK_FACTOR
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    
        # 2. Subway edges (if any)
        if u in subway_adj:
            for v, t in subway_adj[u]:
                if not visited[v]:
                    if dist[u] + t < dist[v]:
                        dist[v] = dist[u] + t

    print(round(dist[1]))

if __name__ == '__main__':
    solve()
