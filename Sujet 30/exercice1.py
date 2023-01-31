def moyenne(tab:list)->float:
    total = 0
    for chiffre in tab:
        total += chiffre
    moyenne = total/len(tab)
    return moyenne
