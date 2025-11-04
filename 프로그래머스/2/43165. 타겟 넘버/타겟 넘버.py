def solution(numbers, target):
    def dfs(i, sum_):
        if i == len(numbers):
            if sum_ == target:
                return 1
            else:
                return 0
        return dfs(i+1, sum_ + numbers[i]) + dfs(i+1, sum_ - numbers[i])
    
    return dfs(0,0)