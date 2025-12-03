def find_the_longest_one(lis, n) -> int:
    current_length = 0
    max_length = 0
    for i in range(n):
        if lis[i] == 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return max_length

n = int(input().strip())
sequence = list(map(int, input().strip().split()))
print(find_the_longest_one(sequence, n))