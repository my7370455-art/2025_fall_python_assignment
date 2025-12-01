#give you a sequence of integers, you can choose a number i in sequence and delete it,
#then all i+1 and i-1 in this sequence will also be deleted, you can get i points for deleting i,
#from the remaining sequence you can continue to do this operation, what is the maximum points you can get
def max_points(sequence):
    from collections import Counter

    if not sequence:
        return 0

    count = Counter(sequence)
    max_num = max(count)

    dp = [0] * (max_num + 1)
    dp[0] = 0
    dp[1] = count[1] * 1

    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + count[i] * i)

    return dp[max_num]

n = int(input())
sequence = list(map(int, input().split()))
result = max_points(sequence)
print(result)