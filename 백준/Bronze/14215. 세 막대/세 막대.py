arr = list(map(int, input().split()))
arr.sort()
(a, b, c) = (arr[0], arr[1], arr[2])
while a+b <= c:
    c -= 1
print(a+b+c)