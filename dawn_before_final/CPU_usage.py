n = int(input())
info = []
for _ in range(n):
    compute, write = map(int, input().split())
    info.append((write, compute))

info.sort(reverse = True)
total_time = 0
total_write_time = 0
for write, compute in info:
    total_time += compute
    total_write_time = max(total_write_time, total_time + write)
print(total_write_time)
