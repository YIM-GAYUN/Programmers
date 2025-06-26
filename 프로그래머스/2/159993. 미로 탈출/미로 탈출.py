from collections import deque

# 이동 가능한 좌표인지 판단
def is_valid_move(ny, nx, n, m, maps):
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X"

# 방문한 적 없으면 큐에 넣고 방문 표시
def append_to_queue(ny, nx, k, time, visited, q):
    if not visited[ny][nx][k]:
        visited[ny][nx][k] = True
        q.append((ny, nx, k, time + 1)) # 시간 추가 반영
        
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    # 위, 아래, 왼쪽, 오른쪽 이동 방향
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()
    end_y, end_x = -1, -1
    
    # 시작점과 도착점 큐에 넣고 방문 표시
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                q.append((i, j, 0, 0)) # 시작점
                visited[i][j][0] = True
            if maps[i][j] == "E":
                end_y, end_x = i, j
                
    while q:
        y, x, k, time = q.popleft() # k는 레버 당김 여부
        
        # 도착점에 도달하면 결과 반환
        if y == end_y and x == end_x and k == 1:
            return time
        
        # 네 방향으로 이동
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 이동 가능한 좌표인 때에만 큐에 넣음
            if not is_valid_move(ny, nx, n, m, maps):
                continue
            
            # 레버일 경우
            if maps[ny][nx] == "L":
                append_to_queue(ny, nx, 1, time, visited, q)
            else:
                append_to_queue(ny, nx, k, time, visited, q)
        
    # 도착점에 도달 못 할 경우
    return -1