def multiplication(n1,n2):
    res = 0
    if n1 > 0:
        for i in range(n1):
            res += n2
    elif n2 > 0:
        for i in range(n2):
            res += n1
    else:
        for i in range(-n1):
            res -= n2
    return res
