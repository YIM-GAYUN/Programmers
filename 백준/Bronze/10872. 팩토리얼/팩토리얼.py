def fac(n):
    if(n>1):
        return n * fac(n-1)
    else:
        return 1

N = int(input())
print(fac(N))
    
    