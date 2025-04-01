def solution(id_list, report, k):
    '''
    1. 중복 제거 / split으로 쪼개어 두번째거 id_list별로 딕셔너리로 저장
    2. 소문자로만 / 공백 하나로 구분 / 중복은 하나로  
    3. 배열, 배열, 수  4. k번 이상
    5. 딕셔너리
    '''
    answer = []
    much = {} # 경고 받은 수 딕셔너리
    mail = {} # 메일 보낼 수 딕셔너리
    set_report = list(set(report)) # 중복 신고는 하나로 처리
    
    for user in id_list: # 초기화
        much[user] = 0
        mail[user] = 0
    
    # 경고 받은 수 업데이트
    for j in range(len(set_report)):
        temp = set_report[j].split(' ')
        much[temp[1]] += 1
    
    # 경고가 K개 이상인 user 리스트
    bad_user = []
    for bad in much:
        if much[bad] >= k:
            bad_user.append(bad)
    
    # 메일 보낼 수 업데이트
    for p in range(len(set_report)):
        temp = set_report[p].split(' ')
        if temp[1] in bad_user:
            mail[temp[0]] += 1

    for user in id_list:
        answer.append(mail[user])
        
    return answer