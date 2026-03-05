def solve(n: int) -> None:
    x = 1
    while x <= n:
        all_combis = (x ** 2 * (x ** 2 - 1)) // 2
        disallowed = ((x - 3 + 1) * (x - 2 + 1)) * 2 * 2
        print(all_combis - disallowed)
        x += 1
n = int(input())
solve(n)
