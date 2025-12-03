# you know stock prices in n days, find the max profit you can make, you can only sell once after buy once
def max_profit(prices, n) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

n = int(input().strip())
prices = list(map(int, input().strip().split()))
print(max_profit(prices, n))