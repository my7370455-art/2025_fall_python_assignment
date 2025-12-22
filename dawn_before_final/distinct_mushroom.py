# give you a list of mushrooms, count the ways to select a part of the list so mushrooms in that part have less than k colors or k colors
# one number represents one color
# sliding window needed
n, k = map(int, input().split())
mushrooms = list(map(int, input().split()))
left = 0
color_count = {}
result = 0
for right in range(n):
    color = mushrooms[right]
    if color in color_count:
        color_count[color] += 1
    else:
        color_count[color] = 1
    while len(color_count) > k:
        left_color = mushrooms[left]
        color_count[left_color] -= 1
        if color_count[left_color] == 0:
            del color_count[left_color]
        left += 1
    result += right - left + 1
print(result)