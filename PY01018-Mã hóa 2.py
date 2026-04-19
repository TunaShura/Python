P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    data = input().split()
    k = int(data[0])

    if k == 0:
        break

    s=data[1]
    res = ""
    for c in s:
        pos = P.index(c)
        newpos = (pos + k) % 28
        res += P[newpos]
    print(res[::-1])
