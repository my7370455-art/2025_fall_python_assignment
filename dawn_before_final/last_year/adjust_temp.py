t = int(input())
for _ in range(t):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    if abs(b - r) < x and abs(b - l) < x and a != b:
        print(-1)
        continue
    if abs(l - a) < x and abs(r - a) < x and a != b:
        print(-1)
        continue
    if a == b:
        print(0)
        continue
    steps = 0
    while abs(a - b) < x:
        if abs(b - r) >= abs(b - l):
            a = r if abs(r - a) >= x else l
        else:
            a = l if abs(l - a) >= x else r
        steps += 1
    steps += 1
    print(steps)
        
            

