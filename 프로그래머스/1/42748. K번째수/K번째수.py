def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        num = commands[i][2]
        
        new = array[start:end]
        set_new = sorted(new)
        ans = set_new[num - 1]
        answer.append(ans)
    return answer