def solve(path: str, moves: dict, index: int, visited: list[list[bool]], row: int, col: int) -> int:
    if row == 7 and col == 1 and index == 48:
        return 1
    if index >= 48:
        return 0
    if row == 7 and col == 1 and index != 48:
        return 0
    for key in moves:
        mr, mc = moves[key]
        if visited[row + mr][col + mc] and visited[row - mr][col - mc] and not visited[row + mc][col + mr] and not visited[row - mc][col - mr]:
            return 0
    total = 0
    for key in moves:
        if path[index] != '?' and path[index] != key:
            continue
        mr, mc = moves[key]
        if 1 <= row + mr < 8 and 1 <= col + mc < 8 and not visited[row + mr][col + mc]:
            visited[row + mr][col + mc] = True
            total += solve(path, moves, index + 1, visited, row + mr, col + mc)
            visited[row + mr][col + mc] = False
    return total

path = input()
moves = {
    'D': (1, 0),
    'U': (-1, 0),
    'L': (0, -1),
    'R': (0, 1),
}
visited = [[False for _ in range(9)] for _ in range(9)]
for i in range(9):
    visited[0][i] = True
    visited[i][0] = True
    visited[8][i] = True
    visited[i][8] = True
visited[1][1] = True
print(solve(path, moves, 0, visited, 1, 1))
