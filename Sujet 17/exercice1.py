def moyenne(liste_notes):
    tot_notes = 0
    tot_coef = 0
    for i in liste_notes:
        note, coef = i
        tot_coef += coef
        tot_notes += note * coef
    return tot_notes / tot_coef
