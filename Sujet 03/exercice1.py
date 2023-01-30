def moyenne(tab:list):
    tot = 0
    coefs = 0
    for note, coef in tab:
        tot += note * coef
        coefs += coef
    if coefs == 0:
        return None
    return tot / coefs
