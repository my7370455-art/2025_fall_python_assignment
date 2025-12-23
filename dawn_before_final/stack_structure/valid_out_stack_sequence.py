n = int(input())
sequence = list(map(int, input().split()))
# judge whether the sequence can be a valid stack pop sequence
stack = []
index = 0
for i in range(1, n + 1):
    stack.append(i)
    while stack and stack[-1] == sequence[index]:
        stack.pop()
        index += 1

if index == n:
    print("Yes")
else:
    print("No")