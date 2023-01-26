def recherche(elt:int, tab:list):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return -1
