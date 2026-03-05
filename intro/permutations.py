def solve(n: int) -> str:
    if n == 1:
        return '1'
    if n <= 3:
        return "NO SOLUTION"
    base = [0 for _ in range(n)]
    for i in range(n):
        num = i + 1
        if  num % 2 == 0:
            base[i // 2] = num
        else:
            base[n // 2 + i // 2] = num
    return ' '.join(map(str, base))

n = int(input())
print(solve(n))