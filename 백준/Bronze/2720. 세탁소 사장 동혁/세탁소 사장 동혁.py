Q, D, N, P = 0, 0, 0, 0
n = int(input())
for _ in range(n):
    money = int(input())
    Q, money = money // 25, money % 25
    D, money = money // 10, money % 10
    N, money = money // 5, money % 5
    P = money
    print(f'{Q} {D} {N} {P}')