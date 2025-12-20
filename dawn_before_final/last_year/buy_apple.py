from collections import defaultdict
n, m = map(int, input().strip().split())
price_tag = list(map(int, input().strip().split()))
fruit_dict = defaultdict(int)
for _ in range(m):
    fruit = input().strip()
    fruit_dict[fruit] = fruit_dict.get(fruit, 0) + 1
min_sum = 0
max_sum = 0
nums = sorted(fruit_dict.values(), reverse=True)
price_tag.sort()
for i in range(len(nums)):
    min_sum += nums[i] * price_tag[i]

price_tag.sort(reverse=True)
for i in range(len(nums)):
    max_sum += nums[i] * price_tag[i]

print(min_sum, max_sum)