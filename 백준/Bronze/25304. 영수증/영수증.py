total = int(input())
num = int(input())
ans = 0
for i in range(num):
    a, b = map(int, input().split())
    ans += a * b
if ans == total: print("Yes")
else: print("No")