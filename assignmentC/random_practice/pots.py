def fill_the_pot(a, b, c):
    """using fill and drop and pour to get desired amount of water"""
    from collections import deque
    visited = set()
    queue = deque()
    queue.append((0, 0))
    parent = {}
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        if x == c or y == c:
            path = []
            while (x, y) in parent:
                px, py, action = parent[(x, y)]
                path.append(action)
                x, y = px, py
            path.reverse()
            print(len(path))
            for step in path:
                print(step)
            return
        
        # FILL pot 1
        if (a, y) not in visited:
            queue.append((a, y))
            parent[(a, y)] = (x, y, "FILL(1)")
        
        # FILL pot 2
        if (x, b) not in visited:
            queue.append((x, b))
            parent[(x, b)] = (x, y, "FILL(2)")
        
        # DROP pot 1
        if (0, y) not in visited:
            queue.append((0, y))
            parent[(0, y)] = (x, y, "DROP(1)")
        
        # DROP pot 2
        if (x, 0) not in visited:
            queue.append((x, 0))
            parent[(x, 0)] = (x, y, "DROP(2)")
        
        # POUR from pot 1 to pot 2 (both fit)
        if x + y <= b and (0, x + y) not in visited:
            queue.append((0, x + y))
            parent[(0, x + y)] = (x, y, "POUR(1,2)")
        
        # POUR from pot 2 to pot 1 (both fit)
        if x + y <= a and (x + y, 0) not in visited:
            queue.append((x + y, 0))
            parent[(x + y, 0)] = (x, y, "POUR(2,1)")
        
        # POUR from pot 1 to pot 2 (pot 2 fills up)
        if x + y > b and (x - (b - y), b) not in visited:
            queue.append((x - (b - y), b))
            parent[(x - (b - y), b)] = (x, y, "POUR(1,2)")
        
        # POUR from pot 2 to pot 1 (pot 1 fills up)
        if x + y > a and (a, y - (a - x)) not in visited:
            queue.append((a, y - (a - x)))
            parent[(a, y - (a - x))] = (x, y, "POUR(2,1)")
    
    print("impossible")
    return

# Read input
a, b, c = map(int, input().split())
fill_the_pot(a, b, c)
