n = int(input())
progress_info = []
for _ in range(n):
    compute_time, write_time = map(int, input().split())
    progress_info.append((write_time, compute_time))
progress_info.sort(reverse = True)
total_compute_time = 0
total_write_time = 0
for write_time, compute_time in progress_info:
    total_compute_time += compute_time
    total_write_time = max(total_write_time, total_compute_time + write_time)

print(total_write_time)
