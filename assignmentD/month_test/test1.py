n = int(input())
if n == 1:
    print("End")
else:
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(f"{n*2}/2={n}")
        else:
            n = 3 * n + 1
            print(f"{(n-1)//3}*3+1={n}")
    print("End")