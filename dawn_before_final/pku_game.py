n, k = map(int, input().strip().split())
player_dict = dict()
total_list = []
for i in range(n):
    temp_list = list(map(int, input().strip().split()))
    total_list.extend(temp_list)
    player_dict[i] = set(temp_list)

losing_time = [0] * n
length = n * k
for i in total_list:
    for j in range(n-1, -1, -1):
        if i in player_dict[j]:
            losing_time[j] += 1
            break

for player in losing_time:
    print ('%.9f' % (player / length))





