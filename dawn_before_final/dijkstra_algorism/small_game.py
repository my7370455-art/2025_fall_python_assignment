# notice that in this file, w stands for the width of the board (number of columns), and h stands for the height of the board (number of rows).
# meanwhile, start and goal are tuples in the form of (x, y), where x starts from 1 to w and y starts from 1 to h.

def judge_and_calculate_the_shortest_path(w, h, board, start, goal):
    from collections import deque
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()
    queue.append((start[0]-1, start[1]-1, 0))  # (x, y, distance)
    visited = set()
    visited.add((start[0]-1, start[1]-1))
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == (goal[0]-1, goal[1]-1):
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                if board[ny][nx] != 'X' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
            else:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))

    return -1

while True:
    board_num = 1
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [list(input().strip()) for _ in range(h)]
    print(f'Board #{board_num}:')
    board_num += 1
    while True:
        pairs = 1
        start_x, start_y, goal_x, goal_y = map(int, input().split())
        if start_x == 0 and start_y == 0 and goal_x == 0 and goal_y == 0:
            break
        result = str(judge_and_calculate_the_shortest_path(w, h, board, (start_x, start_y), (goal_x, goal_y)))
        if result == -1:
            result = 'impossible.'
        else:
            result += ' segments.'
        print(f'Pair {pairs}: {result}')
        pairs += 1
    print()  # Blank line after each board


