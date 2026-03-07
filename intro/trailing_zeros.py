def solve(n: int) -> int:
    count = 0
    flat_fives = n // 5
    i = 5
    exp = 2
    while i <= n:
        i = 5 ** exp
        count += (n // i)
        exp += 1
    return count + flat_fives

n = int(input())
print(solve(n))
        
        