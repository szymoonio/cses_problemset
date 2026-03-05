def solve(arr: list[int]) -> int:
    sum = 0
    for i in range(1, len(arr)):
        diff = min(0, arr[i] - arr[i - 1])
        sum -= diff
        arr[i] -= diff
    return sum

n = int(input())
str = input()
print(solve([int(c) for c in str.split(' ')]))