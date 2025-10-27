import sys
import heapq

n = int(input())
heap = []
ans = 0
for i in range(n):
    x = int(sys.stdin.readline())
    heapq.heappush(heap, x)
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans += (a+b)
    heapq.heappush(heap, a+b)

print(ans)
    