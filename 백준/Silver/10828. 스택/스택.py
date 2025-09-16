N = int(input())
arr = []
for _ in range(N):
    line = input()
    if line[:2] == 'pu':
        arr.append(int(line[5:]))
    elif line[:2] == 'po':
        if len(arr) == 0:
            print(-1)
        else:
            cur = arr.pop()
            print(cur)
    elif line[:2] == 'si':
        print(len(arr))
    elif line[:2] == 'em':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif line[:2] == 'to':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
        
        