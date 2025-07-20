n,m = map(int, input().split())
arr = [0] + [i for i in range(1, n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a:b+1] = arr[a:b+1][::-1]
print(*arr[1:])