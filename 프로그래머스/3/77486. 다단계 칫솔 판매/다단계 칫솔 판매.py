def solution(enroll, referral, seller, amount):
    # 1.계산/트리구조  2.-  3.배열4개  4.딕셔너리
    parent = dict(zip(enroll, referral))
    
    total = {name: 0 for name in enroll}
    
    for i in range(len(seller)):
        money = amount[i] * 100
        cur_name = seller[i]
        
        while money > 0 and cur_name != "-":
            total[cur_name] += money - money // 10
            cur_name = parent[cur_name]
            money //= 10
    return [total[name] for name in enroll]
