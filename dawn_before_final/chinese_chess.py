from collections import deque

start_pos = tuple(map(int, input().strip().split()))
end_pos = tuple(map(int, input().strip().split()))
pieces = int(input().strip())
pieces_list = set()
for _ in range(pieces):
    piece_pos = tuple(map(int, input().strip().split()))
    pieces_list.add(piece_pos)

queue = deque()
parent_dic = dict()
visited = set()
queue.append(start_pos)
parent_dic[start_pos] = None
visited.add(start_pos)
directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

while queue:
    current_pos = queue.popleft()
    if current_pos == end_pos:
        break
    for dx, dy in directions:
        next_x = current_pos[0] + dx
        next_y = current_pos[1] + dy
        if tuple([next_x - dx//abs(dx), next_y - dy//abs(dy)]) in pieces_list:
            continue
        next_pos = (next_x, next_y)
        if 0 <= next_x <= 10 and 0 <= next_y <= 10 and next_pos not in visited and next_pos not in pieces_list:
            visited.add(next_pos)
            parent_dic[next_pos] = current_pos
            queue.append(next_pos)

count = 1
while queue:
    current_pos = queue.popleft()
    if current_pos == end_pos:
        count += 1

if count > 1:
    print(count)
else:
    path = []
    backtrack_pos = end_pos
    while backtrack_pos is not None:
        path.append(backtrack_pos)
        backtrack_pos = parent_dic[backtrack_pos]
    path.reverse()
    output_str = '-'.join([f"({pos[0]},{pos[1]})" for pos in path])
    print(output_str)