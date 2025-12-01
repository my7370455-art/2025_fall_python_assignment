#need to place pieces on a board of a given shape
#the shape is given in a matrix, where # represents a grid cell that can be occupied, and . represents it cannot be occupied
#any two pieces cannot be placed in the same row or column, figure out how many ways there are to place the pieces
#multiple test cases, each starts with n, meaning the size of the board (n x n) and k, meaning the number of pieces to place
#followed by n lines, each containing n characters (# or .)
#-1 -1 means end of input
def count_ways(board, n, k, row=0, placed=0, cols=set()):
    if placed == k:
        return 1
    if row == n:
        return 0

    total_ways = 0
    for col in range(n):
        if board[row][col] == '#' and col not in cols:
            cols.add(col)
            total_ways += count_ways(board, n, k, row + 1, placed + 1, cols)
            cols.remove(col)

    total_ways += count_ways(board, n, k, row + 1, placed, cols)
    return total_ways

def main():
    while True:
        n, k = map(int, input().split())
        if n == -1 and k == -1:
            break
        board = [input().strip() for _ in range(n)]
        result = count_ways(board, n, k)
        print(result)

main()