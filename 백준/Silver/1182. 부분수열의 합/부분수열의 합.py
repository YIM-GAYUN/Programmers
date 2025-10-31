import sys
input = sys.stdin.readline

def dfs(idx, cur):
    global answer
    if idx == n:
        if cur == s:
            answer += 1
        return
    # 현재 원소를 포함
    dfs(idx + 1, cur + arr[idx])
    
    # 현재 원소를 미포함
    dfs(idx + 1, cur)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

dfs(0, 0)

# 비어 있지 않은 부분수열만 카운트 → 합이 0이면 공집합 1개 제외
if s == 0:
    answer -= 1

print(answer)
