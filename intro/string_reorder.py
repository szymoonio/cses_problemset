def solve(s: str) -> str:
    occurences = [0 for _ in range(26)]
    total = len(s)
    for i in range(len(s)):
        occurences[ord(s[i]) - ord('A')] += 1
    ans = ['0']
    while True:
        empty = True
        top = max(occurences)
        for i in range(26):
            if occurences[i] > (total + 1) // 2:
                return ''
            if top > total // 2 and top != occurences[i]:
                continue
            if occurences[i] > 0 and ans[-1] != chr(i + ord('A')):
                occurences[i] -= 1
                ans.append(chr(i + ord('A')))
                total -= 1
                empty = False
                break
        if empty:
            return ans[1:]
        
ans = solve(input())
if ans:
    print("".join(ans))
else:
    print(-1)
    