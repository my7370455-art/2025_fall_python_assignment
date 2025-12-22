n, target = map(int, input().split())
arr = list(map(int, input().split()))
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    