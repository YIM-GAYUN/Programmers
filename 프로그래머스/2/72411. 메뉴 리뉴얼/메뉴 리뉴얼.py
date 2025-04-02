from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        combi_list = []

        # 각 주문에서 조합 뽑기
        for order in orders:
            if len(order) >= c:
                combi = combinations(sorted(order), c)
                combi_list += combi
        
        # 조합별 등장 횟수 세기
        counter = Counter(combi_list)
        
        # 2번 이상 주문된 조합 중 최다 등장 조합만 추가
        if counter:
            max_count = max(counter.values())
            if max_count >= 2:
                for combi in counter:
                    if counter[combi] == max_count:
                        answer.append(''.join(combi))

    return sorted(answer)
