s = input()

answer = 1
for i, c in enumerate(s):
    if c != s[-(1 + i)]:
        answer = 0
        break
print(answer)
