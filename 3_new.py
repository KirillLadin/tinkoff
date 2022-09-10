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
doors = [0]*n
for j in range(0, k):
    for i in range(0, n):
        if doors[i] == 0:
            k = 1
            res = 0
            for t in range(1, n):
                if doors[(i + t) % n] == 0:
                    res += k * l[(i + t) % n]
                    k += 1
                else:
                    k = 1
            m = min(m, res)
            if m == res:
                m_i = i
    doors[m_i] = 1
print(m)
