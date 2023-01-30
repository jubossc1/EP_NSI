def verifie(tab:list):
    x = tab[0]
    for i in tab:
        if i < x:
            return False
        x = i
    return True
