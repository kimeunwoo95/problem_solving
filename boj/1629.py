a, b, c = map(int, input().split())


b = bin(b)
dp = [a % c] * (len(b) - 2)
for i in range(1, len(b) - 2):
    dp[i] = (dp[i - 1] ** 2) % c


answer = 1
for i in range(0, len(b) - 2):
    if b[-(i + 1)] == "1":
        answer *= dp[i]
        answer = answer % c

print(answer)
