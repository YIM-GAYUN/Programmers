X = int(input())
outcome, i, a, b = 0, 0, 0, 0

while X > outcome:
    i += 1
    outcome += i

a = outcome - X + 1
b = i + 1 - a

if i % 2 == 0:
    print(f"{b}/{a}")
else:
    print(f"{a}/{b}")