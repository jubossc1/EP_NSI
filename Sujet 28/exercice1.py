def moyenne(tab:list)->float:
    tot = 0
    for note in tab:
        tot += note
    moyenne = tot/len(tab)
    return moyenne

assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5
