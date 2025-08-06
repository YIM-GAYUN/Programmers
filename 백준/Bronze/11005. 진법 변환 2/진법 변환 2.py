answer = ''
N, B = map(int, input().split())
while (N > 0):
    per = N % B
    if per < 0 or per > 9:
        per = chr(per + 55)
    answer = str(per) + answer
    N = N // B
print(answer)