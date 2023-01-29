def max_et_indice(tab):
    max = tab[0]
    indice = 0
    for i in range(len(tab)):
        if tab[i] > max:
            max = tab[i]
            indice = i
    return max, indice
