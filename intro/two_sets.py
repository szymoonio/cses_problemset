def solve(n: int) -> None:
    sum = 0
    for i in range(1, n + 1):
        sum += i
    if sum % 2 != 0:
        print('NO')
        return
    print('YES')
    target = sum // 2
    curr = 0
    set1 = []
    set2 = []
    for i in range(n, 0, -1):
        if curr + i <= target:
            curr += i
            set1.append(i)
        else:
            set2.append(i)
    print(len(set1))
    print(' '.join(map(str, set1)))
    print(len(set2))
    print(' '.join(map(str, set2)))

n = int(input())
solve(n)