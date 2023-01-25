def convertir(tab):
    nb = 0
    l = len(tab)
    for i in range(len(tab)):
        if tab[i] == 1:
            nb += 2 ** (l - i - 1)
    return nb
