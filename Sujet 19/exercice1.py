def recherche(tab:list,n:int):
    if n < tab[0] or n > tab[-1] or n not in tab:
        return -1
    m = len(tab)//2
    while True:
        if n > tab[m]:
            m += 1
        elif n <tab[m]:
            m-=1
        else:
            return m
