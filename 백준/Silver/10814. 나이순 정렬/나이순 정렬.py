import sys

N = int(input())
member = list(sys.stdin.readline().split() for _ in range(N))
member.sort(key = lambda x: int(x[0]))

for i in range(N):
    print(member[i][0], member[i][1])