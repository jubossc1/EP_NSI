def recherche_indices_classement(elt, tab):
    l1 = []
    l2 = []
    l3 = []
    for i in range(len(tab)):
        if tab[i] > elt:
            l3.append(i)
        elif tab[i] == elt:
            l2.append(i)
        else:
            l1.append(i)
    return l1, l2, l3
