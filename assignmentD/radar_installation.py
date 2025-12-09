def radar_optimize(lis, coverage) -> int:
    lis.sort()
    installed_intervals = []
    for x, y in lis:
        if y > coverage:
            return -1
        left = x - (coverage**2 - y**2)**0.5
        right = x + (coverage**2 - y**2)**0.5
        installed_intervals.append((left, right))
    installed_intervals.sort()
    count = 0
    current_end = -float('inf')
    for i, (left, right) in enumerate(installed_intervals):
        if left > current_end:
            count += 1
            current_end = right
        else:
            current_end = min(current_end, right)
    return count

case = 1
while True:
    n, d = map(int, input().strip().split())
    if n == 0 and d == 0:
        break
    islands = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        islands.append((x, y))

    result = radar_optimize(islands, d)
    print(f"Case {case}: {result}")
    case += 1
    cache = input()