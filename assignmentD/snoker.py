white_position = tuple(map(int, input().split()))
black_position = tuple(map(int, input().split()))
directions = tuple(map(int, input().split()))
energy = int(input().strip())
active = False
lis = [(0,0), (8, 0), (16, 0), (0, 5), (8, 5), (16, 5)]
set_of_the_holes = set(lis)
while energy > 0:
    dx, dy = directions
    white_position = (white_position[0] + dx, white_position[1] + dy)
    energy -= 1
    if white_position == black_position:
        active = True
        break
    if white_position in set_of_the_holes:
        print(-1)
        break
    if white_position[0] == 0 or white_position[0] == 16:
        directions = (-directions[0], directions[1])
    if white_position[1] == 0 or white_position[1] == 5:
        directions = (directions[0], -directions[1])

if active:
    while energy > 0:
        dx, dy = directions
        black_position = (black_position[0] + dx, black_position[1] + dy)
        energy -= 1
        if black_position in set_of_the_holes:
            print(1)
            exit(0)
            break
        if black_position[0] == 0 or black_position[0] == 16:
            directions = (-directions[0], directions[1])
        if black_position[1] == 0 or black_position[1] == 5:
            directions = (directions[0], -directions[1])

if energy == 0:
    print(0)