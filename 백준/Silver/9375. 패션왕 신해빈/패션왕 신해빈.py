test_num = int(input())
for _ in range(test_num):
    clothes = {}
    answer = 1
    num = int(input())
    for _ in range(num):
        name, kind = input().split()
        if not kind in clothes:
            clothes[kind] = 1
        else:
            clothes[kind] += 1
    
    for key in clothes:
        answer *= (clothes[key] + 1)
    print(answer - 1)