def min_et_max(tab):
    dic = {"min": tab[0], "max": tab[0]}
    for element in tab:
        if element < dic["min"]:
            dic["min"] = element

        if element > dic["max"]:
            dic["max"] = element
    return dic

