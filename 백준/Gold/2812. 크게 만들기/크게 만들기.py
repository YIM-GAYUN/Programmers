n, k = map(int, input().split())
number = list(input())

ans = []
cnt = k
for num in number:
    while ans and cnt > 0 and ans[-1] < num:
        del ans[-1]
        cnt -= 1
    ans.append(num)
    
print(''.join(ans[:n-k]))