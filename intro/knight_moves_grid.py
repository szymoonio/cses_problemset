from collections import deque

def solve(board: list[list[int]]):
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    size = len(board)
    q = deque()
    q.append((0, 0, 0))
    board[0][0] = 0
    while q:
        next_row, next_col, next_val = q.popleft()
        for move in moves:
            move_row, move_col = move
            if 0 <= next_row + move_row < size and 0 <= next_col + move_col < size and board[next_row + move_row][next_col + move_col] == -1:
                board[next_row + move_row][next_col + move_col] = next_val + 1
                q.append((next_row + move_row, next_col + move_col, next_val + 1))
    
n = int(input())
board = [[-1 for _ in range(n)] for _ in range(n)]
solve(board)
for row in board:
    print(" ".join(map(str, row)))