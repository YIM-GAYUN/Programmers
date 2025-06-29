h, m = map(int, input().split(" "))
time = int(input())
H, M = 0, 0

if time < 60:
    if m + time < 60:
        H = h
        M = m + time
    else:
        H = h + 1
        M = m + time - 60
else:
    add_h = time // 60
    add_m = time % 60
    if m + add_m < 60:
        H = h + add_h
        M = m + add_m
    else:
        H = h + add_h + 1
        M = m + add_m - 60

if H>=24:
    H = H-24
    
print(str(H)+" "+str(M))