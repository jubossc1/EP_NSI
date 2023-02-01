def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m, j)
    elif tab[m] > n:
        return chercher(tab, n, j, i)
    else:
        return m
