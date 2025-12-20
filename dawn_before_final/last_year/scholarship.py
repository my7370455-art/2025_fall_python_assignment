t = int(input().strip())
stu_info = []
for i in range(1, t+1):
    a, b, c = map(int, input().strip().split())
    sum = a + b + c
    stu_info.append((sum, a, i))
stu_info.sort(key=lambda x: (-x[0], -x[1], x[2]))
pointer = 1
for info in stu_info:
    print(f"{info[2]} {info[0]}")
    pointer += 1
    if pointer > 5:
        break