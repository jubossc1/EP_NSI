def liste_puissances(a,n):
    l = [a]
    for i in range(1,n):
        num = a
        for j in range(i):
            num *= a
        l.append(num)
    return l

def liste_puisssances_borne(a, borne):
    res = []
    if a >= 2:
        l = liste_puissances(a,borne)
        for element in l:
            if element < borne:
                res.append(element)
    else:
        raise IndexError()
    return res
