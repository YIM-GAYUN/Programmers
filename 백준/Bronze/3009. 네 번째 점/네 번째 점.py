import math

lst_x = []
lst_y = []
X, Y = 0, 0

for _ in range(3):
    x, y = map(int, input().split())
    lst_x.append(x)
    lst_y.append(y)
    
for x in lst_x:
    if lst_x.count(x) == 1:
        X = x

for y in lst_y:
    if lst_y.count(y) == 1:
        Y = y
       
print(f'{X} {Y}')
    