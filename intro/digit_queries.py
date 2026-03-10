def solve(n: int) -> int:
    x = 0
    # figure out how many digits we have - 1 digit: indices 1 - 9, 2 digits: indices 10 - 189, ...
    while n - (9 * 10 ** x) * (x + 1) > 0:
        n -= (9 * 10 ** x) * (x + 1)
        x += 1
    n -= 1 # !! very important to make math easier
    # what number from our base does the index point to
    num = 10 ** x + n // (x + 1)
    digit = (num // 10 ** (x - n % (x + 1))) % 10
    return digit

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for x in nums:
    print(solve(x))
    