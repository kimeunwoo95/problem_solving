import sys

input = sys.stdin.readline

n = int(input())

answer = 0
for _ in range(n):
    word = input().rstrip()
    stack = []
    for c in word:
        if len(stack) > 0 and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if len(stack) == 0:
        answer += 1
print(answer)
