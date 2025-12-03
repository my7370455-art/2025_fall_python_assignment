# use a matrix to decide who is the strongest player
total_players = int(input())
matrix = []
for _ in range(total_players):
    row = list(map(int, input().split()))
    matrix.append(row)
win_list = set()
lost_list = set()
for i in range(total_players):
    for j in range(total_players):
        if i == j:
            continue
        if i in lost_list and j in lost_list:
            continue
        if matrix[i][j] == 1:
            win_list.add(i)
            lost_list.add(j)
            if j in win_list:
                win_list.remove(j)
        else:
            win_list.add(j)
            lost_list.add(i)
            if i in win_list:
                win_list.remove(i)
if len(win_list) == 1:
    print(win_list.pop())