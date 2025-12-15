from functools import lru_cache

@lru_cache(None)
def interesting_drink(m_values) -> int:
        # Binary search to find the number of shops with price <= m
    left, right = 0, len(prices)
    while left < right:
        mid = (left + right) // 2
        if prices[mid] <= m:
            left = mid + 1
        else:
            right = mid
    result = left
    return result

n = int(input().strip())
prices = list(map(int, input().strip().split()))
prices.sort()
q = int(input().strip())
for _ in range(q):
    m = int(input().strip())
    print(interesting_drink(m))