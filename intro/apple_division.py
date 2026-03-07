def solve(weights: list[str], index: int, diff: int) -> int:
    if index == len(weights):
        return diff
    # adding the apple to the "heavier" group, so diff gets bigger or the "lighter" group, so diff gets smaller
    return min(solve(weights, index + 1, diff + weights[index]), solve(weights, index + 1, abs(weights[index] - diff)))

n = int(input())
weights = [int(c) for c in input().split()]
print(solve(weights, 0, 0))