a = str(input())
b = str(input())
c = str(input())
d = str(input())
e = str(input())
f = str(input())


def cal(z, x, v, b, n, m):
    vit, per, res = 0, 0, 0
    if z == 'V':
        vit += 1
    else:
        per += 1
    if x == 'V':
        vit += 1
    else:
        per += 1
    if v == 'V':
        vit += 1
    else:
        per += 1
    if b == 'V':
        vit += 1
    else:
        per += 1
    if n == 'V':
        vit += 1
    else:
        per += 1
    if m == 'V':
        vit += 1
    else:
        per += 1
    ############
    if vit == 5 or vit == 6:
        res = 1
    elif vit == 3 or vit == 4:
        res = 2
    elif vit == 1 or vit == 2:
        res = 3
    elif vit == 0:
        res = -1
    return res


loc = cal(a, b, c, d, e, f)
print(loc)