def recherche(caractere:str, chaine:str)->int:
    assert 0 < len(caractere) <= 1
    occurence = 0
    for lettre in chaine:
        if lettre == caractere:
            occurence += 1
    return occurence
