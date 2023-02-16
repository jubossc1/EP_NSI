#Programme Faux
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
       

#Solution valable
def recherche(tab:list, n:int):
    if n not in tab:
        return -1
    min = 0
    max = len(tab)
    while True:
        m = min + (max - min) // 2 + len(tab) % 2
        if tab[m] > n:
            max = m
        elif tab[m] < n:
            min = n
        else:
            return m

