N = int(input())
M = int(input())
materials = list(map(int, input().split()))

memory = {}
answer = 0
for m in materials:
    if m in memory:
        answer += 1
        memory.pop(m)
    else:
        memory[M - m] = True
print(answer)
