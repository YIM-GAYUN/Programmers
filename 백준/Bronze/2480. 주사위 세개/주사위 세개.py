a, b, c = map(int, input().split())
if a==b==c:
    prize = 10000 + a*1000
elif a==b and a!=c:
    prize = 1000 + a*100
elif a==c and a!=b:
    prize = 1000 + a*100
elif b==c and a!=b:
    prize = 1000 + b*100
else:
    temp = max(a,b,c)
    prize = temp*100

print(prize)