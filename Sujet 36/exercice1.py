def couples_consecutifs(tab:list)->list:
    consecutifs = []
    for i in range(len(tab)):
        if i+1 <= len(tab)-1:
            if tab[i] == tab[i+1] - 1:
                consecutifs.append((tab[i],tab[i+1]))
    return consecutifs
