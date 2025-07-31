word = input()
word = word.upper()
alp = [0] * 26
max_num = 0
max_alp = 'A'
for i in range(26):
    alp[i] = word.count(chr(65+i))
    if (alp[i] > max_num):
        max_num = alp[i]
        max_alp = chr(65+i)
    elif max_num >= 1 and alp[i] == max_num:
        max_alp += chr(65+i)
if (len(max_alp) > 1):
    print("?")
else:
    print(max_alp)

