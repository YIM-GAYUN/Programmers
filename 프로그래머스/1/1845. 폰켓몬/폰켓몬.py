def solution(nums):
    answer = 0
    max_nums = len(nums) / 2
    only = len(set(nums))
    if max_nums >= only:
        answer = only
    else:
        answer = max_nums
    return answer