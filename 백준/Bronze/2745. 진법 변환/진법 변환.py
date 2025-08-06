ans = 0
N, B = input().split()
B = int(B)
for i in range(len(N)):
    ch = N[i]
    if '0' <= ch <= '9':
        num = int(ch)
    else:
        num = ord(ch) - ord('A') + 10
    ans += num * (B**(len(N)-1-i))
print(ans)