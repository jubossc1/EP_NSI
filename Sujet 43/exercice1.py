def ecriture_binaire_entier_positif(n:int):
    tab = []
    while n != 0:
        tab.append(n % 2)
        n = n // 2
    tab.reverse()
    return tab
