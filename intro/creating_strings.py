def make_list(letters: list[str], length: int, curr_length: int, word: str, words: list[str]) -> None:
    if curr_length == length:
        words.append(word)
        return
    for i in range(26):
        if letters[i]:
            letters[i] -= 1
            make_list(letters, length, curr_length + 1, word + chr(i + ord('a')), words)
            letters[i] += 1



def solve(s: str) -> list[str]:
    letters = [0 for _ in range(26)]
    for i in range(len(s)):
        letters[ord(s[i]) - ord('a')] += 1
    words = []
    make_list(letters, len(s), 0, '', words)
    return words

s = input()
words = solve(s)
print(len(words))
for word in words:
    print(word)