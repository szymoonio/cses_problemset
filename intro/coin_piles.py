def solve(n: int, m: int) -> str:
    if (n + m) % 3 != 0:
        return 'NO'
    if n < m // 2 or m < n // 2:
        return 'NO'
    return 'YES'

c = int(input())
for _ in range(c):
    n, m = [int(c) for c in input().split()]
    print(solve(n, m))
    