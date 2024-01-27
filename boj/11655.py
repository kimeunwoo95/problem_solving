s = input()

answer = ""
for c in s:
    if ord("A") <= ord(c) <= ord("Z"):
        answer += chr((ord(c) - ord("A") + 13) % 26 + ord("A"))
    elif ord("a") <= ord(c) <= ord("z"):
        answer += chr((ord(c) - ord("a") + 13) % 26 + ord("a"))
    else:
        answer += c

print(answer)
