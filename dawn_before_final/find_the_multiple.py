# given a positive integer n, find a nonzero multiple m of n whose decimal representation consists of only digit 0 and 1
# add explaination
# use bfs to find the smallest such multiple
def find_multiple(n: int) -> str:
    from collections import deque

    queue = deque()
    visited = set()

    queue.append('1')
    while queue:
        current = queue.popleft()
        current_mod = int(current) % n

        if current_mod == 0:
            return current

        if current_mod not in visited:
            visited.add(current_mod)
            queue.append(current + '0')
            queue.append(current + '1')

    return ""

while True:
    n = int(input().strip())
    if n == 0:
        break
    print(find_multiple(n))