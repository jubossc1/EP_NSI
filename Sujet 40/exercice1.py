def nombre_de_mots(phrase:str)->int:
    nb_mots = 0
    charactere = [" ",".",",", "?","!"]
    for element in range(len(phrase)):
        if phrase[element] in charactere and element != len(phrase)-2:
            nb_mots += 1

    return nb_mots
