s = input()
result = len(s)
for i in range(len(s)):
    if s[i] in 'ABC': result += 2
    elif s[i] in 'DEF': result += 3
    elif s[i] in 'GHI': result += 4
    elif s[i] in 'JKL': result += 5
    elif s[i] in 'MNO': result += 6
    elif s[i] in 'PQRS': result += 7
    elif s[i] in 'TUV': result += 8
    elif s[i] in 'WXYZ': result += 9
print(result)
