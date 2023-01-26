def nombre_occurrences(chaine):
    dic = dict()
    for c in chaine:
        l = c
        occ = 0
        for i in range(len(chaine)):
            if l == chaine[i]:
                occ+=1
        if c not in dic.keys():
            dic[c] = occ
    return dic
