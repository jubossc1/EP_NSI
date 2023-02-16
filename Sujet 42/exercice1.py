def tri_selection(tab:list):
    for i in range(len(tab)):
        min = i
        for j in range(i, len(tab)):
            if tab[j] < tab[min]:
                min = j
        tab[i], tab[min] = tab[min], tab[i]
    return tab
