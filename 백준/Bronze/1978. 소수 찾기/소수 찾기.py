N = int(input())
nums = list(map(int, input().split()))
cnt = 0
for num in nums:
    if num == 1:
        continue
    is_ = True
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            is_ = False
            break
    if is_:
        cnt += 1
print(cnt)