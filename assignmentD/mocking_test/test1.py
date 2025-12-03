# find all mountains of one sequence
def find_mountains(seq, n):
    count = 0
    for i in range(1, n-1):
        if seq[i-1] < seq[i] > seq[i+1]:
            count += 1
    return count

n = int(input().strip())
sequence = list(map(int, input().strip().split()))
result = find_mountains(sequence, n)
print(result)