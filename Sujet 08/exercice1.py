def max_dico(dico:dict):
    max = -1
    for key, values in dico.items():
        if values > max:
            max = values
            name = key
    return name, max
