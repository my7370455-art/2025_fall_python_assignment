#from the integer 1, you can perform the following operations:
# multiply by 2
# plus 1
# Given a target number n, find the minimum number of operations to reach n from 1 using bfs
from collections import deque
def min_operations(n):
    if n == 1:
        return 0
    
    queue = deque()
    queue.append((1, 0))  # (current number, steps)
    visited = set()
    visited.add(1)
    
    while queue:
        current, steps = queue.popleft()
        
        # Generate the next possible numbers
        next_nums = [current * 2, current + 1]
        
        for next_num in next_nums:
            if next_num == n:
                return steps + 1
            if next_num < n * 2 and next_num not in visited:  # limit search space
                visited.add(next_num)
                queue.append((next_num, steps + 1))
    
    return -1  # should not reach here for valid n

n = int(input())
result = min_operations(n)
print(result)