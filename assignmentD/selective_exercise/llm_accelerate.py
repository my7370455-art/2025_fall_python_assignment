core_num, battery_life = map(int, input().strip().split())
x_list = []
x_y_sum = []
for _ in range(core_num):
    x, y = map(int, input().strip().split())
    x_list.append(x)
    x_y_sum.append(x + y)

x_list.sort()
using_x_y_sum = min(x_y_sum)
max_rounds = 0
for i in range(core_num):
    if x_list[i] >= using_x_y_sum:
        max_rounds = max(max_rounds, rounds)
        break
    current_life = battery_life
    rounds = 0
    for j in range(i):
        if current_life >= x_list[j]:
            current_life -= x_list[j]
            rounds += 1
        else:
            max_rounds = max(max_rounds, rounds)
            break
    if current_life > 0:
        rounds += current_life // using_x_y_sum * 2
        max_rounds = max(max_rounds, rounds)
print(max_rounds)