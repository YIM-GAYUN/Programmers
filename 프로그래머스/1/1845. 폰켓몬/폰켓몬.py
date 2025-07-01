def solution(nums):
    answer = 0
    set_nums = set(nums)
    poss = len(nums) // 2
    if len(set_nums) < poss:
        answer = len(set_nums)
    else:
        answer = poss
    return answer