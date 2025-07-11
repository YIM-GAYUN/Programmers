maxnum = 0
for i in range(9):
    n = int(input())
    if n > maxnum:
        maxnum = n
        idx = i+1
print(maxnum)
print(idx)