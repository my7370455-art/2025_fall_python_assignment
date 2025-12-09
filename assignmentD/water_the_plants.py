n, a, b = map(int, input().strip().split())
current_a = a
current_b = b
plants_lis = list(map(int, input().strip().split()))
pointer_a = 0
pointer_b = n - 1
fill_time = 0
if n % 2 == 0:
    while pointer_a < pointer_b:
        if current_a < plants_lis[pointer_a]:
            fill_time += 1
            current_a = a - plants_lis[pointer_a]
        else:
            current_a -= plants_lis[pointer_a]
        if current_b < plants_lis[pointer_b]:
            fill_time += 1
            current_b = b - plants_lis[pointer_b]
        else:
            current_b -= plants_lis[pointer_b]
        pointer_a += 1
        pointer_b -= 1
    print(fill_time)
else:
    while pointer_a < pointer_b:
        if current_a < plants_lis[pointer_a]:
            fill_time += 1
            current_a = a - plants_lis[pointer_a]
        else:
            current_a -= plants_lis[pointer_a]
        if current_b < plants_lis[pointer_b]:
            fill_time += 1
            current_b = b - plants_lis[pointer_b]
        else:
            current_b -= plants_lis[pointer_b]
        pointer_a += 1
        pointer_b -= 1
    if pointer_a == pointer_b:
        if current_a >= plants_lis[pointer_a] or current_b >= plants_lis[pointer_b]:
            pass
        else:
            fill_time += 1
    print(fill_time)