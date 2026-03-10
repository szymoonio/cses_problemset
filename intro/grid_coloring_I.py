def solve(board: list[list[str]]) -> None:
    num_rows = len(board)
    num_cols = len(board[0])
    letters = ['A', 'B', 'C', 'D']
    for i in range(num_rows):
        for j in range(num_cols):
            top = ''
            left = ''
            if i > 0:
                top = board[i - 1][j]
            if j > 0:
                left = board[i][j - 1]
            for letter in letters:
                if letter != top and letter != left and letter != board[i][j]:
                    board[i][j] = letter
                    break
            
            
rows, cols = [int(c) for c in input().split()]
board = []
for i in range(rows):
    line = input()
    board.append(list(line))
solve(board)
for row in board:
    print("".join(map(str, row)))