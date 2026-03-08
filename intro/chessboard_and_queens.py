def solve(board: list[list[int]], row: int, cols: list[int], diag1: list[int], diag2: list[int]) -> int:
    if row == 8:
        return 1
    total_ways = 0
    for i in range(8):
        if cols[i] == 0 and diag1[row - i + 7] == 0 and diag2[row + i] == 0 and board[row][i] == 0:
            cols[i] = 1
            diag1[row - i + 7] = 1
            diag2[row + i] = 1
            total_ways += solve(board, row + 1, cols, diag1, diag2)
            cols[i] = 0
            diag1[row - i + 7] = 0
            diag2[row + i] = 0
    return total_ways

board = [[0 for _ in range(8)] for _ in range(8)]

for i in range(8):
    line = input()
    for j in range(8):
        if line[j] == '*':
            board[i][j] = -1

print(solve(board, 0, [0 for _ in range(8)], [0 for _ in range(15)], [0 for _ in range(15)]))

