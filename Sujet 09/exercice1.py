def multiplication(a:int, b:int):
    tot = 0
    if a < 0:
        a = -a
        tot += 1
    if b < 0:
        b = -b
        tot += 1
    x = 0
    for i in range(b):
        x += a
    if tot == 1:
        return -x
    return x
