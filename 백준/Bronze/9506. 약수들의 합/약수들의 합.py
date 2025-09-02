while True:
    n = int(input())
    if n == -1:
        break
    nums = []
    for i in range(1, n):
        if n % i == 0:
            nums.append(i)
    total = 0
    for j in range(len(nums)):
        total += nums[j]
    string = ""
    if total == n:
        for k in range(len(nums)-1):
            string = string + str(nums[k]) + " + "
        string += str(nums[-1])
        print(f"{n} = {string}")
    else:
        print(f"{n} is NOT perfect.")