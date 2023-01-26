def insere(a, tab):
    """ Insère l'élément a (int) dans le tableau tab (list) trié par ordre croissant
    à sa place et renvoie le nouveau tableau. """
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(tab) - 1
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l
