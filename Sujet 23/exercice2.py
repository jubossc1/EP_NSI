def trouver_intrus(tab, g, d):
    if g == d:
        return tab[g]
    else:
        nombre_de_triplets =  (d-g)//3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] != tab[indice+1]:
            return trouver_intrus(tab,g,d-3)
        else:
            return trouver_intrus(tab,g+3,d)

