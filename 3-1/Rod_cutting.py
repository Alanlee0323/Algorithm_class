def Bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


n = int(input())
p = [0] * 50000

while True:
    length, price = map(int, input().split())
    if length == 0 and price == 0:
        break
    p[length] = price

result = Bottom_up_cut_rod(p, n)
print(result)