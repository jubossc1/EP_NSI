def renverse(mot:str):
    inverse = ""
    for i in range(1, len(mot) + 1):
        inverse += mot[-i]
    return inverse
