def convertir(tab):
    nb = 0
    l = len(tab)
    for i in range(len(tab)):
        if tab[i] == 1:
            nb += 2 ** (l - i - 1)
    return nb

def convertir(tab):
    resultat = 0
    indice = len(tab) - 1
    for element in tab:
        resultat += element * (2 ** indice)
        indice -= 1
    return resultat
