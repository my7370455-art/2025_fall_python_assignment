def cal_how_many_power(n):
    power = 0
    current = 1
    while current <= n:
        current *= 2
        power += 1
    return power - 1

def cal_strange_sequence(n):
    return (n + 1) * n // 2 - 2 * (2 ** (cal_how_many_power(n)+1) - 1)

t = int(input())
for _ in range(t):
    n = int(input())
    print(cal_strange_sequence(n))