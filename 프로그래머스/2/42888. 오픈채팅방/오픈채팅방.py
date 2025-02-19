def solution(record):
    '''1.공백으로 나눠서 저장/ 닉네임 바뀔 시 변경/ 변경한대로 출력  2.x  3.문자열 배열  4.방을 개설한 사람이 보게 되는 메시지  5.해시..?
    '''
    answer = []
    new = []
    rec_len = len(record)
    for i in range(rec_len):
        split_str = record[i].split(" ")
        new.append(split_str)
    
    dic = {}
    for j in range(rec_len):
        if new[j][0] == "Enter":
            dic[new[j][1]] = new[j][2]
        elif new[j][0] == "Change":
            dic[new[j][1]] = new[j][2]

    for k in range(rec_len):
        if new[k][0] == "Enter":
            string = dic[new[k][1]] + "님이 들어왔습니다."
            answer.append(string)
        elif new[k][0] == "Leave":
            string = dic[new[k][1]] + "님이 나갔습니다."
            answer.append(string)
    return answer