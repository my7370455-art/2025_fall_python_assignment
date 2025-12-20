# give you n integers > 0 representing the height of one pillar in a row.
# When it rains, water is trapped between the pillars.
# calculate how much water is trapped after raining.
# The width of each pillar is 1.
def trap_rain_water(heights):
    if not heights:
        return 0

    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    trapped_water = 0
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - heights[i]

    return trapped_water

n = int(input().strip())
heights = list(map(int, input().strip().split()))
print(trap_rain_water(heights))