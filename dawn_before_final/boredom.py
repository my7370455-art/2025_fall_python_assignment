def max_points(lis) -> int:
    from collections import Counter
    count = Counter(lis)
    dp_table = [0] * (max(lis) + 1)
    dp_table[1] = count[1] * 1
    for i in range(2, len(dp_table)):
        dp_table[i] = max(dp_table[i - 1], dp_table[i - 2] + count[i] * i)
    return dp_table[-1]
n = int(input().strip())
lis = list(map(int, input().strip().split()))
print(max_points(lis))