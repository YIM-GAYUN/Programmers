h, m = map(int,input().split(" "))
H, M = 0, 0
if h==0 and m<45:
    H = 23
    M = m+15
elif m<45:
    H = h-1
    M = m+15
else:
    H = h
    M = m-45
print(str(H)+" "+str(M))