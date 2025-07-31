num = int(input())
for i in range(1, num+1):
    print(' ' * (num-i) + '*' * (i*2-1))
for j in range(1, num):
    print(' ' * j + '*' * (num*2 - (j*2 + 1)))