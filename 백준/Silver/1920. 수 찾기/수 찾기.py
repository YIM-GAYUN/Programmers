N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()

def bS(target):
    s = 0
    e = N-1
    while s<=e:
        mid = (s+e)//2
        if A[mid] == target:
            print(1)
            return
        elif A[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    print(0)
    return
            
for i in range(M):
    bS(B[i])
    