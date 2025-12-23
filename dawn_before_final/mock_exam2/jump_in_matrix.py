def find_the_shortest_path(start, target):
    from collections import deque
    queue = deque()
    queue.append((start, 0, ''))
    visited = set()
    while queue:
        position, steps, path = queue.popleft()
        if position == target:
            return steps, path
        if position in visited:
            continue
        visited.add(position)
        # in the house
        queue.append((position * 3, steps + 1, path + 'H'))
        # out of the house
        queue.append((position // 2, steps + 1, path + 'O'))
    return -1, ''
while True:
    start, target = map(int, input().split())
    if start == 0 and target == 0:
        break
    else:
        steps, path = find_the_shortest_path(start, target)
        print(steps)
        print(path)