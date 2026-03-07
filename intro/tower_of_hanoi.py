def solve(n: int, source: str, spare: str, destination: str, path: list[str]) -> None:
    if n == 1:
        path.append(f'{source} {destination}')
        return
    solve(n - 1, source, destination, spare, path)
    path.append(f'{source} {destination}')
    solve(n - 1, spare, source, destination, path)

path = []
n = int(input())
solve(n, '1', '2', '3', path)
print(len(path))
for el in path:
    print(el)


