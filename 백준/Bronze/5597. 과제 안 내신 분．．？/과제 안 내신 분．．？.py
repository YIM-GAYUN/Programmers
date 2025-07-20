arr = [0]*30
for i in range(28):
    n = int(input())
    arr[n-1] = 1
for j in range(30):
    if arr[j] == 0:
        print(j+1, end=' ')