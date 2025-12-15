def cat_coin(coins):
    coins.sort(reverse = True)
    odd_coins = [coin for coin in coins if coin % 2 == 1]
    even_coins = [coin for coin in coins if coin % 2 == 0]
    result = [0] * len(coins)

    if not odd_coins:
        return result
    result[0] = odd_coins[0]

    if not even_coins:
        for i in range(len(coins)):
            if i % 2 == 0:
                result[i] = odd_coins[0]
            else:
                result[i] = 0
        return result

    for i in range(1, len(even_coins) + 1):
        result[i] = result[i - 1] + even_coins[i-1]

    start_point = len(even_coins) + 1

    if len(odd_coins) <= 2:
        for i in range(start_point, len(coins)):
            result[i] = 0
    else:
        ans1 = result[start_point - 1]
        ans2 = result[start_point - 1] - even_coins[-1]
        for i in range(start_point, len(coins)):
            if (i - start_point) % 2 == 0:
                if i == len(coins) - 1:
                    result[i] = 0
                    continue
                result[i] = ans2
            else:
                result[i] = ans1
    return result

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    coins = list(map(int, input().strip().split()))
    res = cat_coin(coins)
    print(' '.join(map(str, res)))
        

