def solve(n: int) -> None:
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i][j] = i ^ j
    for row in grid:
        print(" ".join(map(str, row)))

n = int(input())
solve(n)