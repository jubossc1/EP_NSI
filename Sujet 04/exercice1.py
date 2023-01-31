def a_doublon(tab:list)
    for i in range(1, len(tab)):
        if tab[i] == tab[i - 1]:
            return True
    return False
