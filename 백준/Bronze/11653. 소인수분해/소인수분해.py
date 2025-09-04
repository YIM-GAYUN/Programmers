N = int(input())
nums = []
while N > 1:
    for i in range(2, N+1):
        if N % i == 0:
            nums.append(i)
            N //= i
            break
for num in nums:
    print(num)