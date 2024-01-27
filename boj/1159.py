n = int(input())

names = {}
for _ in range(n):
    name = input()
    names[name[0]] = names.get(name[0], 0) + 1
answer = ""
for k, v in names.items():
    if v >= 5:
        answer += k
answer = "".join(sorted(list(answer)))
if answer:
    print(answer)
else:
    print("PREDAJA")
