def solution(numbers):
    answer = ''
    temp = sorted(numbers, key=lambda x: str(x)*3, reverse=True)
    for num in temp:
        answer += str(num)
    
    if temp[0] == 0:
        return "0"
    return answer