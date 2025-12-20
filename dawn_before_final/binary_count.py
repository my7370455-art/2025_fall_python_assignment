# calculate how many binary numbers in 1 to n has k 1s in their binary representation
# large n up to 10^9
def binary_count(n: int, k: int) -> int:
    # Precompute binomial coefficients C(n, k) for n, k <= 30
    C = [[0] * 31 for _ in range(31)]
    for i in range(31):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    count = 0
    ones_count = 0
    for i in range(30, -1, -1):
        if n & (1 << i):
            # If the i-th bit is set, add combinations of remaining bits
            if k - ones_count >= 0:
                count += C[i][k - ones_count]
            ones_count += 1
            if ones_count > k:
                break
        # Check if the number itself has exactly k ones
    if ones_count == k:
        count += 1

    return count


n, k = map(int, input().strip().split())
print(binary_count(n, k))