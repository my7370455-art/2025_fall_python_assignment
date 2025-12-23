n = int(input())
vocab = [input().strip() for _ in range(4)]
for _ in range(n):
    word = input().strip()
    visited = [False] * 4
    def backtrack(index):
        if index == len(word):
            return True
        for i in range(4):
            if not visited[i] and word[index] in vocab[i]:
                visited[i] = True
                if backtrack(index + 1):
                    return True
                visited[i] = False
        return False
    if backtrack(0):
        print("YES")
    else:
        print("NO")