W, H = map(int, input().split())
w, h = map(int, input().split())
x = max(W, H)
y = max(w, h)
if x < y:
    ans = -1
else:
    ans = 0
    while x != y:
        if y > x // 2:
            x = y
        else:
            x -= x // 2
        ans += 1
    x = min(W, H)
    y = min(w, h)
    while x != y:
        if y > x // 2:
            x = y
        else:
            x -= x // 2
        ans += 1
print(ans)

