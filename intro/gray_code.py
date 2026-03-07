def solve(n: int, code: list[str]) -> None:
    if n == 1:
        code[0] = '0'
        code[1] = '1'
        return
    solve(n - 1, code)
    first_half = code[:2 ** (n - 1)]
    second_half = []
    for i in range(len(first_half) - 1, -1, -1):
        second_half.append(first_half[i])
    for i in range(2 ** (n - 1)):
        code[i] = '0' + first_half[i]
        code[i + 2 ** (n - 1)] = '1' + second_half[i]
    
n = int(input())
code = ['' for _ in range(2 ** n)]
solve(n, code)
for i in range(2 ** n):
    print(code[i])

        
        


