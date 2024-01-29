name = input()

alphabets = [0] * 26

for c in name:
    alphabets[ord(c) - ord("A")] += 1

front = ""
back = ""
mid = ""

for i, n in enumerate(alphabets):
    front = front + chr(i + ord("A")) * (n // 2)
    back = chr(i + ord("A")) * (n // 2) + back
    mid = mid + chr(i + ord("A")) * (n % 2)

if len(mid) > 1:
    print("I'm Sorry Hansoo")
else:
    print(front + mid + back)
