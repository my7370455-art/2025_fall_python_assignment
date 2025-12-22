n, target = map(int, input().split())
arr = list(map(int, input().split()))
def binary_search(arr, target):
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            right = mid
        else:
            left = mid + 1
    return left if arr[left] == target else -1

result = binary_search(arr, target)
print(result)