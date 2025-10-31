def bT(index, cur):
    global minAns
    global maxAns

    if index == N - 1:
        if cur < minAns: minAns = cur
        if cur > maxAns: maxAns = cur
        return

    nxt = numArr[index + 1]

    for i in range(4):
        if operator[i] == 0:
            continue

        tmp = cur  # 복구용
        if i == 0:          # +
            cur = cur + nxt
        elif i == 1:        # -
            cur = cur - nxt
        elif i == 2:        # *
            cur = cur * nxt
        else:               # /
            if cur < 0:
                cur = - (abs(cur) // nxt)  # 0쪽으로 버림
            else:
                cur = cur // nxt

        operator[i] -= 1
        bT(index + 1, cur)
        operator[i] += 1
        cur = tmp  # 값 복구

N = int(input())
numArr = list(map(int, input().split()))
operator = list(map(int, input().split()))
minAns = float('inf')
maxAns = float('-inf')

bT(0, numArr[0])
print(maxAns)
print(minAns)
