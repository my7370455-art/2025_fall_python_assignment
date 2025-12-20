# give you n integers in a list, devide them into m parts, such that the maximum sum of each part is minimized
# parts must be continuous
def divide_into_parts(nums, m):
    def can_divide(max_sum):
        current_sum = 0
        parts = 1
        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                parts += 1
                current_sum = num
                if parts > m:
                    return False
        return True

    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if can_divide(mid):
            right = mid
        else:
            left = mid + 1
    return left

n, m = map(int, input().split())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)
print(divide_into_parts(nums, m))