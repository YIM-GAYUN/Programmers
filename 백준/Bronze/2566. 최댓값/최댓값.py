A = [list(map(int, input().split())) for _ in range(9)]
maxi, n, m = -1, -1, -1
for i in range(9):
    for j in range(9):
        if A[i][j] > maxi:
            maxi = A[i][j]
            n, m = i, j
print(maxi)
print(f'{n+1} {m+1}')
