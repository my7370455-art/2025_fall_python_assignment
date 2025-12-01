n = int(input())
state_lis = list(map(int, input().split()))
def sleep_when_old(n: int, state_lis: list) -> int:
    """Return the minimum number of rest days.

    dp_table[i][0] = min rest days up to day i if day i is rest
    dp_table[i][1] = ... if day i is gym
    dp_table[i][2] = ... if day i is contest
    """
    # make the list 1-indexed
    state_lis.insert(0, 0)
    INF = float('inf')

    # proper independent rows and initialize with INF
    dp_table = [[INF] * 3 for _ in range(n + 1)]
    dp_table[0] = [0, 0, 0]

    for i in range(1, n + 1):
        # rest: take the best of previous day and add 1 rest day
        dp_table[i][0] = min(dp_table[i - 1]) + 1

        s = state_lis[i]
        if s == 0:
            dp_table[i][1] = INF
            dp_table[i][2] = INF
        elif s == 2:  # gym only
            dp_table[i][1] = min(dp_table[i - 1][0], dp_table[i - 1][2])
            dp_table[i][2] = INF
        elif s == 1:  # contest only
            dp_table[i][1] = INF
            dp_table[i][2] = min(dp_table[i - 1][0], dp_table[i - 1][1])
        else:  # s == 3, both available
            dp_table[i][1] = min(dp_table[i - 1][0], dp_table[i - 1][2])
            dp_table[i][2] = min(dp_table[i - 1][0], dp_table[i - 1][1])

    return int(min(dp_table[n]))

result = sleep_when_old(n, state_lis)
print(result)