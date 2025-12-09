def matrix_multiply(a, b, mod = 1000000007):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % mod
    return result

def identity_matrix(n):
    output = [[0] * n for _ in range(n)]
    for i in range(n):
        output[i][i] = 1
    return output

def matrix_fast_power(a, k):
    n = len(a)
    output = identity_matrix(n)
    while k:
        if k & 1:
            output = matrix_multiply(output, a)
        a = matrix_multiply(a, a)
        k >>= 1
    return output

base_vector = [[1], [1]]
a_base = [[1, 1], [1, 0]]
wanted_index = int(input().strip())
if wanted_index <= 2:
    print(1)
    exit(0)
result_matrix = matrix_fast_power(a_base, wanted_index - 2)
result = (result_matrix[0][0] * base_vector[0][0] + result_matrix[0][1] * base_vector[1][0]) % 1000000007
print(result)