M = int(input())
N = int(input())
total = 0
nums = []

for i in range(M, N+1):
    if i == 1:
        continue
    is_ = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_ = False
            break
    if is_:
        total += i
        nums.append(i)
    
if total == 0:
    print(-1)
else:
    print(total)
    print(min(nums))