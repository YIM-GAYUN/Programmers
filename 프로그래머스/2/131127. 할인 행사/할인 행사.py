def solution(want, number, discount):
    '''1.x  2.열흘이상일치, 하루에 하나씩만  3.배열3개  4.연속으로일치  5.해시'''
    # want를 딕셔너리로
    wants = {}
    for i in range(len(want)):
        wants[want[i]] = number[i]
    
    day = 0 # 총 일수
    
    # i일에 회원가입 시 할인받는 제품 체크
    for i in range(len(discount) - 9):
        dis_10 = {}
        
        for j in range(i, i + 10):
            if discount[j] in wants:
                dis_10[discount[j]] = dis_10.get(discount[j], 0) + 1 # 없으면 기본값 0 가져오고 가져온 값에서 1 증가
        
        if dis_10 == wants:
            day += 1
    

    return day