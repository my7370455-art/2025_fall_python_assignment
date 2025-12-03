length, nums = map(int, input().split())
length += 1
interval = []
for _ in range(nums):
    interval.append(tuple(map(int, input().split())))
interval.sort()
previous_end = -1
for start, end in interval:
    if start >= previous_end:
        length -= (end - start if start == previous_end else end - start + 1)
        previous_end = end
    elif start < previous_end < end:
        length -= (end - previous_end)
        previous_end = end
    else:
        continue
print(length)