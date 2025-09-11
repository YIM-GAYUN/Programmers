lst_x, lst_y = [], []
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    lst_x.append(x)
    lst_y.append(y)
m_x, max_x = min(lst_x), max(lst_x)
m_y, max_y = min(lst_y), max(lst_y)
print((max_x - m_x)*(max_y - m_y))   