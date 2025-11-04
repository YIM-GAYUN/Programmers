def solution(clothes):
    dic = {}
    result = 1
    
    for i in range(len(clothes)):
        if clothes[i][1] in dic:
            dic[clothes[i][1]] += 1
        else:
            dic[clothes[i][1]] = 1
            
    for value in dic.values():
        result *= (value + 1)
        
    return (result - 1)