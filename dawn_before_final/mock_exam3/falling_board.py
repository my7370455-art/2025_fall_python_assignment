h, l, n = map(int, input().split())
velocity_list = list(map(int, input().split()))
velocity_list.sort()
if n % 2 == 0:
    must_get = n // 2 + 1
else:
    must_get = n - n // 2
split_velocity = velocity_list[must_get - 1]
reach_time = l / split_velocity
height = h - reach_time ** 2 * 5
print(f"{height:.2f}")