# given two sequence of player heights, the players were numbered from 1 to n
# we need to choose players such that no two chosen players are adjacent and the number of chosen players should strictly increase
# return the maximum height sum of the chosen players
def choose_method(n, height1, height2) -> int:
    dp = [[0] * 3 for _ in range(n + 1)]

    for i in range(1, n + 1):
        h1 = height1[i - 1]
        h2 = height2[i - 1]

        dp[i][0] = max(dp[i - 1])  # not choosing any player at position i
        dp[i][1] = max(dp[i - 1][0] + h1, dp[i-1][2] + h1)  # choosing player from height1
        dp[i][2] = max(dp[i - 1][0] + h2, dp[i-1][1] + h2)  # choosing player from height2

    return max(dp[n])

n = int(input())
height1 = list(map(int, input().split()))
height2 = list(map(int, input().split()))
result = choose_method(n, height1, height2)
print(result)