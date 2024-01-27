n = int(input())
pattern = input()

before = ""
after = ""
cnt = 0

for c in pattern:
    if c == "*":
        cnt += 1
    elif cnt < 1:
        before += c
    elif cnt == 1:
        after += c

words = []
for _ in range(n):
    words.append(input())

for word in words:
    if (
        len(word) >= len(before)
        and word[: len(before)] == before
        and len(word[len(before) :]) >= len(after)
        and word[len(before) :][-len(after) :] == after
    ):
        print("DA")
    else:
        print("NE")
