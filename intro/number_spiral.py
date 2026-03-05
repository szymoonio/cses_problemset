def solve(row: int, col: int) -> int:
    if row >= col:
        if row % 2 == 0:
            return row ** 2 + 1 - col
        else:
            return (row - 1) ** 2 + col
    else:
        if not col % 2 == 0:
            return col ** 2 + 1 - row
        else:
            return (col - 1) ** 2 + row
        
n = int(input())
for i in range(n):
    a, b = [int(c) for c in input().split()]
    print(solve(a, b))