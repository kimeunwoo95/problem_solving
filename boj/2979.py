fee = [0] + list(map(int, input().split()))

schedule = []
for _ in range(3):
    park, leave = map(int, input().split())
    schedule.append((park, "park"))
    schedule.append((leave, "leave"))
schedule.sort(key=lambda x: x[0])

answer = 0
now = 1
last_time = schedule[0][0]
for time, action in schedule[1:]:
    answer += (time - last_time) * fee[now] * now
    last_time = time
    if action == "park":
        now += 1
    elif action == "leave":
        now -= 1
print(answer)
