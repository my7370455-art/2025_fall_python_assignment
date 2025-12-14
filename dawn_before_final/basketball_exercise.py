def choose_the_best(lis1, lis2, n) -> int:
    dp = [[0] * (n + 1) for _ in range(3)]

    for i in range(1, n + 1):
        dp[0][i] = max(dp[2][i - 1] + lis1[i - 1], dp[1][i - 1] + lis1[i - 1])
        dp[1][i] = max(dp[2][i - 1] + lis2[i - 1], dp[0][i - 1] + lis2[i - 1])
        dp[2][i] = max(dp[1][i - 1], dp[0][i - 1])

    return max(dp[0][n], dp[1][n])

n = int(input().strip())
lis1 = list(map(int, input().strip().split()))
lis2 = list(map(int, input().strip().split()))
print(choose_the_best(lis1, lis2, n))