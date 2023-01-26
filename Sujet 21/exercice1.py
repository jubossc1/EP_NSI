def delta(tab:list):
    l = [tab[0]]
    for i in range(len(tab)):
        if i+1 < len(tab):
            l.append(tab[i+1]-tab[i])
    return l

