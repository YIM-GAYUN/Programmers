def solution(n,a,b):
    # 1.- 2.부전승 X 3.토너먼트, 몇 번째 라운드 4. 트리
    answer = 0
    while a != b:
        if a%2 == 0:
            a = a/2
        else:
            a = (a+1)/2
        if b%2 == 0:
            b = b/2
        else:
            b = (b+1)/2
        answer += 1

    return answer