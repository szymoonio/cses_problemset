def solve(seq: str) -> int:
    res = 1
    cur = 1
    for i in range(1, len(seq)):
        if seq[i] != seq[i - 1]:
            cur = 0
        cur += 1
        res = max(res, cur)
    return res

seq = input()
print(solve(seq))