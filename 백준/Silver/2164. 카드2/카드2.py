from collections import deque
N = int(input())
q = deque(range(1, N+1))
while len(q) > 1:
    a = q.popleft()
    if len(q) == 1:
        break
    b = q.popleft()
    q.append(b)
print(q[0])