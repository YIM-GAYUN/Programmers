n = int(input())
for _ in range(n):
    R, S = map(str, input().split())
    new = ''
    for j in range(len(S)):
        new += S[j] * int(R)
    print(new)