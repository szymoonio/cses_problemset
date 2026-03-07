def solve(n: str) -> str:
    base = ord('A')
    alph = [0 for _ in range(26)]
    for i in range(len(n)):
        alph[ord(n[i]) - base] += 1
    isOdd = -1
    for i in range(26):
        if alph[i] % 2 != 0:
            if isOdd >= 0:
                return 'NO SOLUTION'
            isOdd = i
    solution = ''
    if isOdd >= 0:
        solution += alph[isOdd] * chr(isOdd + base)
    for i in range(26):
        if i == isOdd:
            continue
        solution = (alph[i] // 2) * chr(i + base) + solution + (alph[i] // 2) * chr(i + base)
    return solution

n = input()
print(solve(n))
    
    