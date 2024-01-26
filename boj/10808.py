S = input()

num = [0] * len("abcdefghijklmnopqrstuvwxyz")

for c in S:
    num[ord(c) - ord("a")] += 1
for n in num[:-1]:
    print(n, end=" ")
print(num[-1])
