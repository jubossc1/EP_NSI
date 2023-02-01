def rangement_valeur(notes_eval:list):
    notes = [0] * 11
    for i in notes_eval:
        notes[i] += 1
    return notes


def notes_triees(notes:list):
    tab = []
    x = 0
    for i in notes:
        for j in range(i):
            tab.append(x)
        x += 1
    return tab
