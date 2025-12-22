m, n, p = map(int, input().split())
hills = list(list(map(str, input().split())) for _ in range(m))
def dijkstra(hills, m, n, start, end):
    import heapq
    if hills[start[0]][start[1]] == "#" or hills[end[0]][end[1]] == "#":
        return -1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    priority_queue = [(0, start, int(hills[start[0]][start[1]]))]
    strength_consumption = [[float('inf')] * n for _ in range(m)]
    strength_consumption[start[0]][start[1]] = 0
    while priority_queue:
        current_strength_consumption, (x, y), last_altitude = heapq.heappop(priority_queue)
        if (x, y) == end:
            return current_strength_consumption
        if current_strength_consumption > strength_consumption[x][y]:
            continue
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and hills[nx][ny] != "#":
                new_strength_consumption = current_strength_consumption + abs(int(hills[nx][ny]) - last_altitude)
                if new_strength_consumption < strength_consumption[nx][ny]:
                    strength_consumption[nx][ny] = new_strength_consumption
                    heapq.heappush(priority_queue, (new_strength_consumption, (nx, ny), int(hills[nx][ny])))

    return -1

for _ in range(p):
    start_x, start_y, end_x, end_y = map(int, input().split())
    result = dijkstra(hills, m, n, (start_x, start_y), (end_x, end_y))
    print(result if result != -1 else "NO")

'''4 5 3
0 0 0 0 0
0 1 1 2 3
# 1 0 0 0
0 # 0 0 0
0 0 3 4
1 0 1 4
3 4 3 0'''