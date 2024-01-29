nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

for n in nums:
    i = len(str(n))
    while i:
        if int("1" * i) % n == 0:
            print(i)
            break
        i += 1
