# give you n stalls and c cows, find the largest minimum distance between cows if you put them in the stalls
# return the minimum distance
import sys

def can_place_cows(stalls: list, c: int, min_dist: int) -> bool:
    count = 1  # Place the first cow in the first stall
    last_position = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= min_dist:
            count += 1
            last_position = stalls[i]
            if count == c:
                return True

    return False

def cows(stalls: list, c: int) -> int:
    stalls.sort()
    left, right = 0, stalls[-1] - stalls[0]
    best_dist = 0

    while left <= right:
        mid = (left + right) // 2
        if can_place_cows(stalls, c, mid):
            best_dist = mid
            left = mid + 1
        else:
            right = mid - 1

    return best_dist

n, c = map(int, input().strip().split())
lines = sys.stdin.readlines()
stalls = [int(line.strip()) for line in lines]
print(cows(stalls, c))