# simulate the accidents happening in a time ordered manner and find the smallest number of chair needed
def min_chairs(accidents):
    min_chairs_needed = 0
    current_chairs_needed = 0
    for i in accidents:
        if i == "E":
            current_chairs_needed += 1
            min_chairs_needed = max(min_chairs_needed, current_chairs_needed)
        elif i == "L":
            current_chairs_needed -= 1
    return min_chairs_needed

accident = input().strip()
print(min_chairs(accident))