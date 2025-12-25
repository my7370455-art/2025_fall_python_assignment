from collections import deque

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
crab_position = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 9:
            target = (i, j)
        if map[i][j] == 5:
            crab_position.append((i, j))

def bfs(start1, start2, target):
    queue = deque()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    queue.append((start1, start2))
    visited.add(tuple(sorted((start1, start2))))
    while queue:
        curr1, curr2 = queue.popleft()
        if curr1 == target or curr2 == target:
            return True
        for dx, dy in directions:
            new1 = (curr1[0] + dx, curr1[1] + dy)
            new2 = (curr2[0] + dx, curr2[1] + dy)
            if 0 <= new1[0] < n and 0 <= new1[1] < n and map[new1[0]][new1[1]] != 1:
                if 0 <= new2[0] < n and 0 <= new2[1] < n and map[new2[0]][new2[1]] != 1:
                    state = tuple(sorted((new1, new2)))
                    if state not in visited:
                        visited.add(state)
                        queue.append((new1, new2))
    return False

if bfs(crab_position[0], crab_position[1], target):
    print("yes")
else:
    print("no")

'''0 0 0 0 0 9
0 0 1 0 1 1
0 0 0 0 0 0
0 0 0 1 0 0
0 0 0 1 0 0
0 0 0 1 5 5'''