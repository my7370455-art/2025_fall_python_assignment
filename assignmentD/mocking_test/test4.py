def snake_in_matrix(n, operations) -> int:
    current_place = [0, 0]
    for op in operations:
        if op == "UP":
            current_place[0] -= 1
        elif op == "DOWN":
            current_place[0] += 1
        elif op == "LEFT":
            current_place[1] -= 1
        elif op == "RIGHT":
            current_place[1] += 1
    return (current_place[0] * n) + current_place[1]

n = int(input().strip())
operations = list(map(str, input().strip().split()))
print(snake_in_matrix(n, operations))