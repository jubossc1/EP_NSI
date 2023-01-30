def recherche_min(tab:list)->int:
    min, indice = tab[0], 0
    for i in range(len(tab)):
        if tab[i] < min:
            min = tab[i]
            indice = i
    return indice
