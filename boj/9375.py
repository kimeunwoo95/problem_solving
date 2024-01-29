N = int(input())
answers = []
for _ in range(N):
    n = int(input())
    closet = {}
    for __ in range(n):
        item, category = input().split()
        closet[category] = closet.get(category, 0) + 1
    answer = 1
    for k, v in closet.items():
        answer *= v + 1
    answers.append(answer - 1)

for answer in answers:
    print(answer)
