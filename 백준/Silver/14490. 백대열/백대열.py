n, m = map(int, input().split(':'))
def GCD(a, b):
    if b % a: return GCD(b%a, a)
    else: return a
        
ans = GCD(n, m)
print(f"{n//ans}:{m//ans}")