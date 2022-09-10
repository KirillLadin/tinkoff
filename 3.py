n, k = map(int, input().split())
l = []
res = 0
for j in range(0, n):
    i = int(input())
    l.append(i)
    res += i * j
s = sum(l)
m = res
m_i = 0
for i in range(1, n):
    res = res - s + n * l[i - 1]
    print(res)
    m = min(m, res)
    if m == res:
        m_i = i
print('res: ', m, ' ', m_i)
