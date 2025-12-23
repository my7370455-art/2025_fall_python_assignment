from itertools import permutations
n = int(input())
lis = [i for i in range(1, n + 1)]
all_sequence = list(permutations(lis))
valid_sequence = []
for sequence in all_sequence:
    stack = []
    current = 0
    for num in range(1, n + 1):
        stack.append(num)
        while stack and stack[-1] == sequence[current]:
            stack.pop()
            current += 1
    if current == n:
        valid_sequence.append(sequence)
for seq in valid_sequence:
    print(' '.join(map(str, seq)))