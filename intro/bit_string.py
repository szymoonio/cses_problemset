def solve(n: int) -> int:
    return (2 ** n) % (10 ** 9 + 7)

n = int(input())
print(solve(n))