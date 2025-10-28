import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

MAXV = 1000
cntA = [0] * (MAXV + 2)
cntB = [0] * (MAXV + 2)
for x in A: cntA[x] += 1
for x in B: cntB[x] += 1

score = 0
p = 0
for v in range(1, MAXV + 1):
    if p < v - 1:
        p = v - 1
    while cntA[v] and p >= 1:
        if cntB[p]:
            take = min(cntA[v], cntB[p])
            cntA[v] -= take
            cntB[p] -= take
            score += 2 * take
        else:
            p -= 1

for v in range(1, MAXV + 1):
    if cntA[v] and cntB[v]:
        take = min(cntA[v], cntB[v])
        cntA[v] -= take
        cntB[v] -= take
        score += take

print(score)
