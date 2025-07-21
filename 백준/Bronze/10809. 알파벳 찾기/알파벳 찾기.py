alp = [-1]*26
s = input()
for i in range(len(s)):
    if alp[ord(s[i])-97] == -1:
        alp[ord(s[i])-97] = i
print(*alp)