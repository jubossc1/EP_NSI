def enumere(lst):
    dic = {}
    for element in lst:
        if element not in dic:
            dic[element] = [i for i in range(len(lst)) if lst[i] == element]
    return dic
