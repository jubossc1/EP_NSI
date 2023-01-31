def recherche(tab:list, n:int):
    if not n in tab:
        return len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            x = i
    return x
