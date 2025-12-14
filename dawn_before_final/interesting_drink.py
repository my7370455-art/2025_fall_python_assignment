def interesting_drink(prices, m_values) -> int:
    results = []
    prices.sort()
    for m in m_values:
        # Binary search to find the number of shops with price <= m
        left, right = 0, len(prices)
        while left < right:
            mid = (left + right) // 2
            if prices[mid] <= m:
                left = mid + 1
            else:
                right = mid
        results.append(left)
    return max(results)

n = int(input().strip())
prices = list(map(int, input().strip().split()))
q = int(input().strip())
for _ in range(q):
    m = int(input().strip())
    print(interesting_drink(prices, [m]))