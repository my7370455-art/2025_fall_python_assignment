# give you m same apples and n same plates, find the sum of ways to put apples into plates
# the plate can be empty
# add explaination
# 1,3,1 and 3,1,1 are the same so we don't count them twice
# dp solution
# test case input:
# 7 3
# output:
# 8
def place_apple(m: int, n: int) -> int:
    # dp[i][j] will be the number of ways to place i apples into j plates.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: There is one way to place any number of apples on one plate.
    for i in range(m + 1):
        dp[i][1] = 1
    
    # Base case: There is one way to place 0 apples on any number of plates.
    for j in range(n + 1):
        dp[0][j] = 1

    for i in range(1, m + 1):
        for j in range(2, n + 1):
            if i >= j:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j]
            else:
                # Not enough apples to place one on each plate,
                # so at least one plate must be empty.
                dp[i][j] = dp[i][j - 1]

    return dp[m][n]

t = int(input().strip())
for _ in range(t):
    m, n = map(int, input().strip().split())
    print(place_apple(m, n))