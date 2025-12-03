# matrix will be used to store the values
m, n = map(int, input().split())
matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
most_one_row = 0
current_max = 0
for i in range(m):
    count_i_row = sum(matrix[i])
    if count_i_row > current_max:
        current_max = count_i_row
        most_one_row = i
print(most_one_row)
print(current_max)