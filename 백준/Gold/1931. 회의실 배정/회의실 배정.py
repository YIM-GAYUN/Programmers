N = int(input())
conf = []

for _ in range(N):
    s, f = map(int, input().split())
    conf.append([s, f])
    
conf.sort(key=lambda x: (x[1], x[0]))

ans = 0
next_ = 0

for i in range(len(conf)):
    if next_ <= conf[i][0]:
        next_ = conf[i][1]
        ans += 1

print(ans)