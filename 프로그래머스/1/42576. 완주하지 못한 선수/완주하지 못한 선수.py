'''
1. X    2. 동명이인 - 번호 부여    3. 배열    4. 한 명 제외    5. 해시
'''
def solution(participant, completion):
    dic = {} # 해시 테이블
    
    # 참가자 추가
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    
    # 완주자 키 값 1씩 감소
    for c in completion:
        dic[c] -= 1
    
    # 남이 있는 선수 반환
    for key in dic.keys():
        if dic[key] > 0:
            return key
    return 0