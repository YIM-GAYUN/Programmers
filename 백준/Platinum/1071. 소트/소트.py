import sys

input = sys.stdin.readline

N = int(input())
csort = [0] * 1002
nums = list(map(int, input().split()))
for v in nums:
    csort[v] += 1

out = []
while True:
    tof = False
    for i in range(1001):
        if csort[i]:
            tof = True
            if csort[i + 1]:
                k = -1
                # 1001도 포함하려면 1002까지
                for j in range(i + 2, 1002):
                    if csort[j]:
                        k = j
                        break
                if k != -1:
                    cnt = csort[i]
                    if cnt:
                        out.extend([str(i)] * cnt)
                        csort[i] = 0
                    out.append(str(k))
                    csort[k] -= 1
                    break
                else:
                    out.append(str(i + 1))
                    csort[i + 1] -= 1
                    break
            else:
                cnt = csort[i]
                if cnt:
                    out.extend([str(i)] * cnt)
                    csort[i] = 0
                break
    if not tof:
        break

print(' '.join(out))