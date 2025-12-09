# give you a matrix, the flight cost between i and j is matrix[i][j], from i to j and j to i have the same cost
# find the minimum cost to visit all the cities and return to the starting city
# the starting city can be any city
# optimized dp or dfs solution
def flight_problem(matrix: list):
    n = len(matrix)
    visited = [False] * n
    min_cost = float('inf')

    def dfs(city: int, count: int, cost: int, start_city):
        nonlocal min_cost
        if count == n and matrix[city][0] > 0:
            min_cost = min(min_cost, cost + matrix[city][start_city])
            return
        for next_city in range(n):
            if not visited[next_city]:
                visited[next_city] = True
                dfs(next_city, count + 1, cost + matrix[city][next_city], start_city)
                visited[next_city] = False

    for start_city in range(n):
        visited[start_city] = True
        dfs(start_city, 1, 0, start_city)
        visited[start_city] = False
    return min_cost

n = int(input().strip())
matrix = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

print(flight_problem(matrix))
