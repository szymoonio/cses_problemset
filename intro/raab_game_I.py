def solve(n: int, score1: int, score2: int) -> None:
    if score1 + score2 > n:
        print("NO")
        return
    if score1 > 0 and score2 == 0 or score2 > 0 and score1 == 0:
        print("NO")
        return
    print("YES")
    draws = n - (score1 + score2)
    line1 = [0 for _ in range(n)]
    line2 = [0 for _ in range(n)]
    i = 1
    while i <= draws:
        line1[i - 1] = i
        line2[i - 1] = i
        i += 1
    for k in range(score1):
        line2[i - 1 + k] = i + k
        line1[i - 1 + k] = i + k + score2
    for k in range(score2):
        line1[i - 1 + k + score1] = i + k
        line2[i - 1 + k + score1] = i + k + score1
    print(" ".join(map(str, line1)))
    print(" ".join(map(str, line2)))

n = int(input())
input_data = []
for _ in range(n):
    input_data.append([int(c) for c in input().split()])
for i in range(n):
    solve(input_data[i][0], input_data[i][1], input_data[i][2])
    