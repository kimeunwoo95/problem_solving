n, k = map(int, input().split())
temps = list(map(int, input().split()))

answer = sum(temps[:k])
summation = sum(temps[:k])

for i, t in enumerate(temps[k:]):
    summation = summation - temps[i] + t
    answer = max(answer, summation)

print(answer)
