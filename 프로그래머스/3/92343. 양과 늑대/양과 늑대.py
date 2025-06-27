from collections import deque

def solution(info, edges):
    # 트리 생성
    def build(info, edges):
        tree = [[] for _ in range(len(info))]
        for edge in edges:
            tree[edge[0]].append(edge[1]) # 부모 노드에 자식 노드 할당
        return tree
    
    tree = build(info, edges)
    max_sheep = 0
    
    # BFS 하기 위한 큐 생성, 초기화
    # 순서대로 (현재 위치, 양의 수, 늑대의 수, 방문한 노드 집합)
    q = deque([(0, 1, 0, set())])
    
    # BFS
    while q:
        current, s_cnt, w_cnt, visited = q.popleft()
        # 양의 수 업데이트
        max_sheep = max(max_sheep, s_cnt)
        visited.update(tree[current])
        
        # 인접 노드 탐색
        for next_node in visited:
            if info[next_node]: # 1, 즉 늑대일 경우
                if s_cnt != w_cnt + 1:
                    q.append((next_node, s_cnt, w_cnt + 1, visited - {next_node}))
            else: # 양일 경우
                q.append((next_node, s_cnt + 1, w_cnt, visited - {next_node}))
                
    return max_sheep