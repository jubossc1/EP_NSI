def nb_repetitions(elt,tab):
    total = 0
    for element in tab:
        if element == elt:
            total += 1
    return total
