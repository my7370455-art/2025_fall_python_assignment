def calcu_one_layer_matrix(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return [sum(matrix[0]) + sum(matrix[1])]
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return [matrix[0][0]]
    else:
        peeled_matrix = [matrix[i][1:len(matrix)-1] for i in range(1, len(matrix)-1)]
        calcu_sum = 0
        calcu_sum += sum(matrix[0]) + sum(matrix[-1])
        for i in range(1, len(matrix)-1):
            calcu_sum += matrix[i][0] + matrix[i][-1]
        return [calcu_sum] + calcu_one_layer_matrix(peeled_matrix)

n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = calcu_one_layer_matrix(matrix)
print(max(result))
'''5
1 0 1 0 1
0 1 1 1 0
0 1 7 1 0
0 1 1 1 0
1 0 1 0 1'''