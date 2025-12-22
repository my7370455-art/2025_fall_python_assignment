def judge_and_calculate_the_shortest_path(w, h, board, start, goal):
    from collections import deque
    dist = [[float('inf')] * (w + 2) for _ in range(h + 2)]
    queue = deque([(start[0], start[1])])
    dist[start[1]][start[0]] = 0
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            # 射线逻辑：沿一个方向一直走
            while 0 <= nx <= w + 1 and 0 <= ny <= h + 1:
                # 如果撞到了卡片
                if board[ny][nx] == 'X':
                    # 特判：如果是终点，更新距离但结束此射线
                    if nx == goal[0] and ny == goal[1]:
                        if dist[ny][nx] > dist[cy][cx] + 1:
                            dist[ny][nx] = dist[cy][cx] + 1
                            # 终点不需要入队去扩展，因为它不能穿过
                    break 
                
                # 如果是空格，尝试更新最短线段数
                if dist[ny][nx] > dist[cy][cx] + 1:
                    dist[ny][nx] = dist[cy][cx] + 1
                    queue.append((nx, ny))
                
                nx += dx
                ny += dy
                
    return dist[goal[1]][goal[0]] if dist[goal[1]][goal[0]] != float('inf') else -1
board_num = 1
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [[' '] * (w + 2)] + [[' '] + list(input()) + [' '] for _ in range(h)] + [[' '] * (w + 2)]
    print(f'Board #{board_num}:')
    board_num += 1
    pairs = 1
    while True:
        start_x, start_y, goal_x, goal_y = map(int, input().split())
        if start_x == 0 and start_y == 0 and goal_x == 0 and goal_y == 0:
            break
        result = str(judge_and_calculate_the_shortest_path(w, h, board, (start_x, start_y), (goal_x, goal_y)))
        if result == '-1':
            result = 'impossible.'
        else:
            result += ' segments.'
        print(f'Pair {pairs}: {result}')
        pairs += 1
    print()  # Blank line after each board
        