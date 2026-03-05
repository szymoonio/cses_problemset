def solve(arr: list[int]) -> int:
    end = [0 for _ in range(len(arr) + 1)]
    for num in arr:
        end[num - 1] = 1
    for i in range(len(end)):
        if end[i] == 0:
            return i + 1

n = int(input())
str = input()
print(solve([int(c) for c in str.split(' ')]))
